from fastapi import APIRouter, UploadFile, File, BackgroundTasks
from pathlib import Path
import uuid, shutil

router = APIRouter()
UPLOAD_DIR = Path("/data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@router.post("/upload")
async def upload_document(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    fn = UPLOAD_DIR / f"{uuid.uuid4()}_{file.filename}"
    with open(fn, "wb") as f:
        shutil.copyfileobj(file.file, f)
    # In PoC we'd enqueue background processing; here we'll just acknowledge
    return {"filename": file.filename, "path": str(fn)}
