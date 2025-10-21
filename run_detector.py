from src.object_detector import run_detector
from src.exceptions import ObjectDetectionError, ModelLoadError
import cv2 

INPUT_PATH = "data/input/street.png"
OUTPUT_PATH = "data/output/detected_street.png"

def main():
    try:
        results = run_detector(INPUT_PATH)
    except Exception as e:
        raise ObjectDetectionError("Error occurred:", e)

    try:
        cv2.imwrite(OUTPUT_PATH, results[0].plot())
    except Exception as e:
        raise ObjectDetectionError(f"Error saving output image: {e}")

if __name__ == "__main__":
    main()
