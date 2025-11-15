# Minimal local vector store adapter (PoC)
from pathlib import Path
import json
STORAGE = Path("/data/vector_store")
STORAGE.mkdir(parents=True, exist_ok=True)

def add_vector(doc_id: str, vector, metadata: dict):
    p = STORAGE / f"{doc_id}.json"
    with open(p, "w") as f:
        json.dump({"vector": vector, "metadata": metadata}, f)
    return True
