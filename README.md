# 👁️ Face Detection Project

A beginner-friendly real-time face detection project built with **Python** and **OpenCV**, supporting both static image detection and live webcam streaming.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green?logo=opencv)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📸 Demo

| Image Detection | Webcam Detection |
|---|---|
| Detects faces in any `.jpg` / `.png` image | Real-time detection via webcam feed |
| Draws bounding boxes with confidence score | Shows live face count on screen |
| Saves result as `output.jpg` | Press `q` to quit |

---

## 🚀 Features

- ✅ Detect faces in static images
- ✅ Real-time face detection via webcam
- ✅ Two detection modes: Haar Cascade (fast) and DNN-based (accurate)
- ✅ Confidence score displayed on each detected face
- ✅ Auto-downloads DNN model weights on first run
- ✅ Output image saved automatically

---

## 📁 Project Structure

```
face_detection_project/
├── detect_image.py                      # Detect faces in a static image
├── detect_webcam.py                     # Real-time webcam face detection
├── deploy.prototxt                      # DNN model config (auto-downloaded)
├── face_model.caffemodel                # DNN model weights (auto-downloaded)
├── requirements.txt                     # Project dependencies
├── output.jpg                           # Result image (auto-generated)
└── README.md                            # Project documentation
```

---

## 🛠️ Tech Stack

- **Language:** Python 3.8+
- **Library:** OpenCV (`opencv-python`)
- **Detection Models:**
  - Haar Cascade Classifier (built into OpenCV)
  - DNN-based SSD Face Detector (ResNet-10 backbone)

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/face-detection-project.git
cd face-detection-project
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv

# Activate on Windows:
venv\Scripts\activate

# Activate on Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### Detect Faces in an Image

1. Place your image (e.g., `photo.jpg`) in the project folder
2. Update the filename at the bottom of `detect_image.py`:
   ```python
   detect_faces("photo.jpg", confidence_threshold=0.7)
   ```
3. Run the script:
   ```bash
   python detect_image.py
   ```
   - A window displays the image with bounding boxes
   - Result is saved as `output.jpg`
   - Press any key to close

### Real-Time Webcam Detection

```bash
python detect_webcam.py
```
- Your webcam opens with live face detection
- Press **`q`** to quit

---

## 🎛️ Configuration

You can tune detection accuracy using the `confidence_threshold` parameter in `detect_image.py`:

| Value | Behaviour |
|---|---|
| `0.5` | More detections, higher chance of false positives |
| `0.7` | Balanced — recommended default |
| `0.85` | Strict — only high-confidence faces detected |
| `0.9` | Very strict — may miss partial or angled faces |

For Haar Cascade (in `detect_webcam.py`), tune these parameters:

| Parameter | Default | Recommendation |
|---|---|---|
| `minNeighbors` | `5` | Increase to `8–10` to reduce false positives |
| `minSize` | `(30,30)` | Increase to `(60,60)` for fewer false detections |

---

## 📦 Requirements

Create a `requirements.txt` with:

```
opencv-python
```

Or install directly:
```bash
pip install opencv-python
```

---

## 🛠️ Troubleshooting

| Error | Cause | Fix |
|---|---|---|
| `ModuleNotFoundError: cv2` | OpenCV not installed | Run `pip install opencv-python` |
| `Error: Could not load image` | Wrong filename or path | Check the filename and confirm it's in the project folder |
| `Error: Cannot access webcam` | Webcam busy or blocked | Close other apps using the camera; try `VideoCapture(1)` |
| Window closes immediately | Script ends too fast | Ensure `cv2.waitKey(0)` is present |
| `python` not recognized | Python not in PATH | Use `python3` instead of `python` |
| Too many false detections | Low threshold or Haar Cascade | Increase `minNeighbors` or switch to DNN model |

---

## 🔼 Future Improvements

- [ ] Add face recognition (identify who the face belongs to)
- [ ] Emotion detection (happy, sad, surprised, etc.)
- [ ] Web interface using Flask
- [ ] Support for video file input
- [ ] Export detection logs to CSV

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

- [OpenCV](https://opencv.org/) — Computer vision library
- [OpenCV DNN Face Detector](https://github.com/opencv/opencv/tree/master/samples/dnn) — Pre-trained model

---

> Built with ❤️ using Python & OpenCV
# face_detection
