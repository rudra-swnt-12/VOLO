from src.segmentation import run_segmentation
from src.exceptions import ImageSegmentationError, ModelLoadError
import cv2 

INPUT_PATH = "data/input/street.png"
OUTPUT_PATH = "data/output/segmented_street.png"

def main():
    try:
        results = run_segmentation(INPUT_PATH)
    except Exception as e:
        raise ImageSegmentationError("Error occurred:", e)

    try:
        cv2.imwrite(OUTPUT_PATH, results[0].plot())
    except Exception as e:
        raise ImageSegmentationError(f"Error saving output image: {e}")

if __name__ == "__main__":
    main()
