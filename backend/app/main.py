from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import auth, indexes, documents, query

app = FastAPI(title="RAG Study Buddy - PoC")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(indexes.router, prefix="/api/indexes", tags=["indexes"])
app.include_router(documents.router, prefix="/api/documents", tags=["documents"])
app.include_router(query.router, prefix="/api/query", tags=["query"])

@app.get("/")
def root():
    return {"status": "ok"}
