# RAG Study Buddy - Backend PoC

This is a minimal FastAPI PoC for the RAG Study Buddy.

Run locally with:
```bash
cd backend
docker-compose up --build
```

API:
- GET / -> health
- POST /api/auth/signup
- POST /api/auth/login
- POST /api/documents/upload
- POST /api/indexes
- GET /api/indexes
- GET /api/query?q=...
