# File: test_face_model.py
"""
SIMPLE TEST FOR FACE MODEL
"""

import sys
import os

print("🚀 Testing Face Model")
print("="*50)

# Add current directory to path
sys.path.append('.')

try:
    from models.face_model import FaceModel
    print("✅ Model imported successfully!")
except Exception as e:
    print(f"❌ Import failed: {e}")
    print("Make sure models/face_model.py exists")
    sys.exit(1)

# Create model
model = FaceModel()
print(f"📊 Model has {model.get_count()} faces")

# Check for your photos
photos = []
ashmita_dir = "test_images/Ashmita"
if os.path.exists(ashmita_dir):
    for file in os.listdir(ashmita_dir):
        if file.lower().endswith(('.jpg', '.jpeg', '.png')):
            photos.append(os.path.join(ashmita_dir, file))

print(f"\n📸 Found {len(photos)} photos of Ashmita")

if photos:
    print(f"\n1. First photo: {photos[0]}")
    
    # Register
    print("\n2. Registering Ashmita...")
    result = model.register_person(
        photos[0],
        name="Ashmita",
        email="ashmita@example.com",
        phone="1234567890"
    )
    print(f"   Result: {result}")
    
    # Recognize same photo
    print("\n3. Recognizing same photo...")
    result = model.recognize_face(photos[0])
    print(f"   Result: {result}")
    
    # Try different photo
    if len(photos) > 1:
        print(f"\n4. Recognizing different photo: {photos[1]}")
        result = model.recognize_face(photos[1])
        print(f"   Result: {result}")
    
    # List people
    print("\n5. All registered people:")
    people = model.list_people()
    for person in people:
        print(f"   👤 {person['name']} (ID: {person['id']})")
    
    # Webcam test
    print("\n" + "="*50)
    print("📹 Test with webcam? (y/n)")
    choice = input("> ").strip().lower()
    
    if choice == 'y':
        print("\n🔍 Looking at webcam... Press 'q' in window to quit")
        model.test_with_webcam()
    
else:
    print("❌ No photos found. Make sure you ran capture.py")

print("\n" + "="*50)
print("✅ Test complete!")
print(f"📁 Data saved to: {model.data_file}")
print(f"👥 Total faces: {model.get_count()}")