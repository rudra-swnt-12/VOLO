from ultralytics import YOLO
from src.exceptions import ImageSegmentationError, ModelLoadError

IMAGE_PATH = 'data/input/street.png'

try:
    model = YOLO('yolov8n-seg.pt')
except Exception as e:
    raise ModelLoadError(f"Error loading YOLO model: {e}")

def run_segmentation(image_path: str):
    try:
        results = model.predict(image_path, verbose=False)
        return results
    except Exception as e:
        raise ObjectDetectionError(f"Error during object detection: {e}")
        return None

