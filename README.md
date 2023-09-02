## Potato Disease Detector App

Welcome to the Potato Disease Detector. This FastAPI-based application is designed to help you identify the health status of potato plants. By uploading an image of a potato plant's leaves, you can receive predictions about whether the plant is healthy or if it is suffering from one of two common diseases: Early Blight or Late Blight.

# Prerequisites
Before running the Potato Disease Detector API, ensure that you have the following components installed on your system:

- Python (version 3.7 or later)
- TensorFlow (for deep learning)
- FastAPI (for creating the API)
- Uvicorn (for running the FastAPI application)
- Pillow (PIL, for image processing)
- NumPy (for numerical operations)


# Install the dependencies from the requirements.txt file
pip install -r requirements.txt


## Run the FastAPI Application

To start the Potato Disease Detector API, navigate to the directory containing your FastAPI application code (typically in a subfolder named `app`) and run the following command:

    ```bash
    uvicorn app:app --reload


## Interpretation of Results

The Potato Disease Detector App will provide you with a JSON response containing the following information:

- `"prediction"`: This field indicates the predicted class, which can be one of the following:
  - `"Potato___Early_blight"`: Indicates the presence of Early Blight disease.
  - `"Potato___Late_blight"`: Indicates the presence of Late Blight disease.
  - `"Potato___healthy"`: Indicates that the potato plant appears to be healthy.

- `"confidence"`: This field provides a floating-point value representing the confidence level of the prediction. It indicates how certain the model is about its prediction, with higher values indicating greater confidence.

Example JSON response:

```json
{
    "prediction": "Potato___Early_blight",
    "confidence": 0.873
}
