from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import os
from ela_transform import perform_ela
from predict import make_prediction

app = FastAPI()


UPLOAD_FOLDER = "uploads"
ELA_FOLDER = "ela_output"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(ELA_FOLDER, exist_ok=True)

@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())
    return {"message": "File uploaded successfully!", "file_path": file_path}

@app.post("/predict")
async def predict_image(file_path: str):
    ela_path = perform_ela(file_path, output_dir=ELA_FOLDER)
    prediction, confidence = make_prediction(ela_path)
    return JSONResponse(content={"prediction": prediction, "confidence": confidence, "ela_path": ela_path})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
