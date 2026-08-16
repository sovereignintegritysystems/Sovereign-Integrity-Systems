"""Bounded read-only acquisition probe for current public GDI institutional reports.

Exact GDI allowlist only. No caller-supplied URLs, credentials, mutation, outreach,
application submission, or semantic authority.
"""
from __future__ import annotations
from http.server import BaseHTTPRequestHandler
from io import BytesIO
import hashlib, json
from urllib.parse import parse_qs, urlparse
from urllib.request import Request, urlopen
from pypdf import PdfReader

MAX_BYTES = 65_000_000
MAX_PAGE_TEXT = 120_000
MAX_MATCHES = 80
DOCS = {
    "annual-2024-25": "https://gdins.org/me/uploads/2026/05/GDI-Annual-Report-2024-25.pdf",
    "operations-2024-25": "https://gdins.org/me/uploads/2025/09/GDI-Training-Employment-Operations-Report-2024-2025.pdf",
    "financial-2025-26": "https://gdins.org/me/uploads/2026/08/2025-26-Gabriel-Dumont-Institute-Training-and-Employment-Inc.-Financial-Statement.pdf",
    "gdi-financial-2025-26": "https://gdins.org/me/uploads/2026/08/2025-26-Gabriel-Dumont-Institute-of-Native-Studies-and-Applied-Research-Inc.-Financial-Statement.pdf",
    "strategic-2022-27": "https://gdins.org/me/uploads/2022/05/Strategic-Plan-2022-2027.pdf",
}
ALLOWED_HOSTS = {"gdins.org", "www.gdins.org"}

def _fetch(doc_id: str):
    url = DOCS[doc_id]
    req = Request(url, headers={"User-Agent":"SIS-public-document-acquisition/1.1"})
    with urlopen(req, timeout=60) as response:  # exact allowlisted HTTPS URLs only
        final_url=response.geturl(); p=urlparse(final_url)
        if p.scheme != "https" or p.hostname not in ALLOWED_HOSTS: raise ValueError("non-allowlisted redirect")
        ct=response.headers.get("Content-Type","application/octet-stream"); declared=response.headers.get("Content-Length")
        if declared is not None and int(declared)>MAX_BYTES: raise ValueError("document exceeds configured maximum")
        data=response.read(MAX_BYTES+1)
        if len(data)>MAX_BYTES: raise ValueError("document exceeds configured maximum")
    if not data.startswith(b"%PDF-"): raise ValueError("source is not a PDF")
    return data,ct,final_url

def _page_text(reader,page_index):
    if page_index<0 or page_index>=len(reader.pages): raise ValueError("page out of range")
    return (reader.pages[page_index].extract_text() or "")[:MAX_PAGE_TEXT]

class handler(BaseHTTPRequestHandler):
    def _json(self,status,payload):
        body=json.dumps(payload,ensure_ascii=False,sort_keys=True).encode("utf-8")
        self.send_response(status); self.send_header("Content-Type","application/json; charset=utf-8"); self.send_header("Content-Length",str(len(body))); self.send_header("Cache-Control","no-store"); self.send_header("X-Robots-Tag","noindex"); self.end_headers(); self.wfile.write(body)
    def _raw_pdf(self,data,doc_id,digest):
        self.send_response(200); self.send_header("Content-Type","application/pdf"); self.send_header("Content-Length",str(len(data))); self.send_header("Content-Disposition",f'attachment; filename="{doc_id}.pdf"'); self.send_header("Cache-Control","no-store"); self.send_header("X-Robots-Tag","noindex"); self.send_header("X-SIS-Source-SHA256",digest); self.end_headers(); self.wfile.write(data)
    def do_GET(self):
        parsed=urlparse(self.path)
        if parsed.path.rstrip("/") not in {"","/","/api/gdi_report_probe"}: return self._json(404,{"status":"REJECTED","reason":"NOT_FOUND"})
        qs=parse_qs(parsed.query,keep_blank_values=False); doc_id=(qs.get("doc") or [""])[0]; mode=(qs.get("mode") or ["meta"])[0]
        if doc_id not in DOCS: return self._json(400,{"status":"REJECTED","reason":"UNKNOWN_DOCUMENT","documents":sorted(DOCS)})
        if mode not in {"meta","page","search","raw"}: return self._json(400,{"status":"REJECTED","reason":"UNKNOWN_MODE"})
        try:
            data,ct,final_url=_fetch(doc_id); digest=hashlib.sha256(data).hexdigest()
            if mode=="raw": return self._raw_pdf(data,doc_id,digest)
            reader=PdfReader(BytesIO(data)); base={"status":"PASS","authority":"NONE","document_id":doc_id,"source_url":DOCS[doc_id],"final_url":final_url,"sha256":digest,"bytes":len(data),"content_type":ct,"pages":len(reader.pages),"source_bytes_observed_in_runtime":True,"source_bytes_persisted_by_endpoint":False}
            if mode=="meta": return self._json(200,base)
            if mode=="page":
                page_number=int((qs.get("page") or ["1"])[0]); text=_page_text(reader,page_number-1); base.update({"page":page_number,"text":text,"text_sha256":hashlib.sha256(text.encode("utf-8")).hexdigest()}); return self._json(200,base)
            query=(qs.get("q") or [""])[0].strip()
            if not query or len(query)>120: raise ValueError("search query required and must be <=120 characters")
            qfold=query.casefold(); matches=[]
            for index,page in enumerate(reader.pages):
                text=page.extract_text() or ""; folded=text.casefold(); start=0
                while len(matches)<MAX_MATCHES:
                    pos=folded.find(qfold,start)
                    if pos<0: break
                    lo=max(0,pos-400); hi=min(len(text),pos+len(query)+800); matches.append({"page":index+1,"snippet":" ".join(text[lo:hi].split())}); start=pos+max(1,len(query))
                if len(matches)>=MAX_MATCHES: break
            base.update({"query":query,"matches":matches,"match_count":len(matches),"truncated":len(matches)>=MAX_MATCHES}); return self._json(200,base)
        except Exception as exc:
            return self._json(502,{"status":"FINDING","authority":"NONE","document_id":doc_id,"reason":type(exc).__name__,"detail":str(exc)[:500]})
