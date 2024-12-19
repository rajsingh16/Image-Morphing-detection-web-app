# Image Morphing Detection Web Application

This web application detects image morphing or manipulation using Error Level Analysis (ELA) and a VGG16-based deep learning model. Users can upload images, process them using ELA, and receive predictions on whether the image is authentic or tampered. The application is designed for use in digital forensics, journalism, and cybersecurity.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Future Improvements](#future-improvements)
- [License](#license)

---

## Overview
This project uses Error Level Analysis (ELA) to highlight discrepancies caused by multiple compressions or pixel alterations. The VGG16 model is fine-tuned to classify images as authentic or tampered based on ELA-transformed images.

---

## Features
- **Image Upload**: Users can upload images for analysis.
- **ELA Transformation**: Highlights compression discrepancies in the uploaded image.
- **Prediction**: Classifies the image as authentic or tampered with a confidence score.
- **Download Option**: Allows downloading the ELA-transformed image.
- **User-Friendly Interface**: Easy-to-use web interface for all features.

---

## Technologies
- **Backend**: FastAPI
- **Frontend**: HTML, CSS, JavaScript
- **Model**: TensorFlow (VGG16) / ELA
- **Libraries**: OpenCV, NumPy, Pillow
- **Deployment**: Docker, AWS/Heroku

---

## Installation

### Prerequisites
- Python 3.7+
- Node.js (if using a frontend framework like React.js)
- Docker (optional for containerized deployment)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/image-morphing-detection-webapp.git
   cd image-morphing-detection-web app
   ```

2. Install backend dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the frontend:
   If using React.js, navigate to the frontend folder and run:
   ```bash
   npm install
   npm run build
   ```

4. Start the backend server:
   ```bash
   uvicorn main:app --reload
   ```

5. Access the application at `http://127.0.0.1:8000`.

---

## Usage
1. Navigate to the web application in your browser.
2. Upload an image using the provided interface.
3. View the original image, ELA-transformed image, and prediction result with confidence score.
4. Optionally download the ELA-transformed image.

---

## Endpoints

### `/upload`
- **Method**: POST
- **Description**: Uploads an image for analysis.
- **Parameters**: None
- **Response**: JSON with the uploaded image URL.

### `/predict`
- **Method**: POST
- **Description**: Classifies the uploaded image as authentic or tampered.
- **Parameters**: Image file (multipart/form-data).
- **Response**: JSON containing the prediction result and confidence score.

---

## Future Improvements
- **Additional Forensic Techniques**: Integrate noise and shadow analysis for better tamper detection.
- **Real-Time Processing**: Optimize for edge AI deployment.
- **Authentication**: Add user login and access control.
- **Batch Processing**: Enable analysis of multiple images at once.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
