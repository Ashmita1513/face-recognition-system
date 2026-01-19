# 🎭 Face Recognition System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.8-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Active-success)

**AI-powered face recognition system for event management and attendance**

[![GitHub stars](https://img.shields.io/github/stars/ashmita/face-recognition-system?style=social)](https://github.com/ashmita/face-recognition-system)
[![GitHub forks](https://img.shields.io/github/forks/ashmita/face-recognition-system?style=social)](https://github.com/ashmita/face-recognition-system)

</div>

## 🏗️ Project Structure

```
event-face-model/
├── 📁 models/              # Core ML models
│   ├── face_model_fixed.py
│   ├── organized_model.py
│   └── stable_recognizer.py
├── 📁 scripts/             # Utility scripts
├── 📁 data/               # Face encodings storage
├── �� logs/               # System logs
├── 📁 test_images/        # Test images
├── capture.py             # Image capture script
├── organize_data.py       # Data organization script
├── registration_portal.py # Registration interface
├── requirements.txt       # Dependencies
├── setup.py              # Package setup
├── test_face_model.py    # Model tests
└── test_stable.py        # Stable recognizer tests
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- OpenCV
- face_recognition library

### Installation
```bash
# Clone repository
git clone https://github.com/ashmita/face-recognition-system.git
cd face-recognition-system

# Create virtual environment
python -m venv venv

# Activate (Linux/Mac)
source venv/bin/activate
# Activate (Windows)
venv\Scriptsctivate

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage
```python
from models.stable_recognizer import FaceRecognizer

# Initialize system
recognizer = FaceRecognizer('data/face_data.pkl')

# Register new face
recognizer.register_face('John Doe', image_array)

# Recognize face
name, confidence = recognizer.recognize_face(image_array)
```

## 📡 API Integration

### For Backend Developers:
```python
# Expected endpoints:
POST /api/v1/faces/register    # Register new face
POST /api/v1/faces/recognize   # Recognize from image
GET  /api/v1/faces/list        # List registered faces
```
## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

---

<div align="center">
</div>
