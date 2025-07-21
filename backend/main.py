from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
from pathlib import Path
import os
from models import create_db_and_tables

app = FastAPI(title="MTG AI Vision", version="0.1")

@app.on_event("startup")
async def on_startup():
    """Create database tables on startup"""
    create_db_and_tables()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@app.get("/")
async def root():
    return {"message: MTG AI Vision"}

@app.post("/upload-card")
async def upload_card(file: UploadFile = File(...)):
    """Upload and process card image"""

    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File type not image.")
    
    file_path = UPLOAD_DIR / file.filename

    try:
        with open(file_path, "wb") as buffer:
            content = await file.read()
            buffer.write(content)

            return {
                "message": "Image uploaded sucessfully",
                "filename": file.filename,
                "size": len(content)
            }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing image: {str(e)}")
    
    finally:
        if file_path.exists():
            file_path.unlink()

@app.get("/health")
async def health_check():
    return{"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)