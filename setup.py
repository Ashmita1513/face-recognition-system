# File: setup.py
"""
SETUP SCRIPT - Run this to install everything
"""

import subprocess
import sys
import os

print("🔧 SETTING UP FACE RECOGNITION SYSTEM")
print("="*50)

# Check if we're in virtual environment
if not hasattr(sys, 'real_prefix') and not sys.base_prefix != sys.prefix:
    print("⚠️  Not in virtual environment!")
    print("Please activate your venv first:")
    print("  source venv/bin/activate")
    sys.exit(1)

# Install requirements
print("\n📦 Installing requirements...")
requirements = [
    "face_recognition",
    "opencv-python",
    "numpy",
    "pillow"
]

for package in requirements:
    print(f"  Installing {package}...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"  ✅ {package} installed")
    except subprocess.CalledProcessError:
        print(f"  ❌ Failed to install {package}")

# Try to install face_recognition_models
print("\n📦 Installing face recognition models...")
try:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 
                          "git+https://github.com/ageitgey/face_recognition_models"])
    print("✅ Face recognition models installed")
except:
    print("⚠️  Could not install from git, trying alternative...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "face_recognition_models"])
        print("✅ Face recognition models installed (alternative)")
    except:
        print("❌ Could not install face recognition models")
        print("You may need to install manually:")
        print("pip install git+https://github.com/ageitgey/face_recognition_models")

# Create necessary directories
print("\n📁 Creating directories...")
directories = ["data", "models", "test_images", "logs"]
for directory in directories:
    os.makedirs(directory, exist_ok=True)
    print(f"  ✅ Created: {directory}/")

# Create requirements.txt
print("\n📝 Creating requirements.txt...")
with open("requirements.txt", "w") as f:
    f.write("""face_recognition>=1.3.0
opencv-python>=4.8.0
numpy>=1.24.0
pillow>=10.0.0
""")
print("✅ requirements.txt created")

print("\n" + "="*50)
print("✅ SETUP COMPLETE!")
print("\nNext steps:")
print("1. Run: python quick_test.py")
print("2. If face_recognition still fails, run the manual fix below")