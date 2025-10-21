# 👁️ VOLO: Vision Operated Learning Output

A computer vision project demonstrating high-performance object detection and instance segmentation using state-of-the-art deep learning models. VOLO processes images to identify and outline objects with precision.

-----

## ✨ Features Implemented

1.  **High-Performance Object Detection:**

* Uses the YOLOv8n model to rapidly detect and draw bounding boxes around various objects (people, cars, traffic lights, etc.) in an image.
* Outputs an annotated image showing the detected objects, their class labels, and confidence scores.

2.  **Instance Segmentation:**

* Uses the YOLOv8n-seg model to go beyond bounding boxes and generate pixel-perfect masks outlining the exact shape of each individual object instance.
* Outputs an annotated image with colored masks overlaid on detected objects.

-----

## 🛠️ Tech Stack

  * 🐍 **Python 3.10+**
  * ⚡ **uv** (Package Manager)
  * 🚀 **Ultralytics (YOLOv8)**: Core library for object detection and segmentation models.
  * 🧠 **PyTorch (`torch`)**: Deep learning framework backend.
  * 🖼️ **OpenCV (`opencv-python-headless`)**: For reading images and writing annotated output images.
  * 📷 **Pillow (PIL)**: Used internally by some libraries for image handling.

-----

## 📦 Installation & Setup

1.  **Clone the repository:**

    ```sh
    git clone https://github.com/your-username/VOLO.git
    cd VOLO
    ```

2.  **Create and activate the virtual environment:**

    ```sh
    uv venv
    source .venv/bin/activate
    # On Windows: .venv\Scripts\activate
    ```

3.  **Install dependencies:**
    This project uses `pyproject.toml` and `uv.lock`. Sync the environment using:

    ```sh
    uv sync
    ```

4.  **Add your data:**

* Place images you want to test in the `data/input/` folder (e.g., `data/input/street.jpg`).

-----

## 🏃 How to Run

Make sure your virtual environment is activated.

### 1\. Run Object Detection:

Modify the `INPUT_PATH` variable in `run_detector.py` to point to your desired image. Then run:

```sh
python run_detector.py
```

The annotated image will be saved in the `data/output/` folder (e.g., `data/output/detected_street.jpg`).

### 2\. Run Instance Segmentation:

Modify the `INPUT_PATH` variable in `run_segmentation.py` to point to your desired image. Then run:

```sh
python run_segmentation.py
```

The segmented image with masks will be saved in the `data/output/` folder (e.g., `data/output/segmented_street.png`).

-----

## 📁 Project Structure

```text
VOLO/
│
├── .venv/                     
│
├── data/
│   ├── input/                 
│   └── output/                
│
├── src/
│   ├── __init__.py
│   ├── exceptions.py        
│   ├── object_detector.py     
│   └── segmenter.py           
│
├── .gitignore
├── run_detector.py            
├── run_segmentation.py        
├── pyproject.toml             
├── README.md                
└── uv.lock                    
```