# File: test_stable.py
"""
Test the stable recognition for backend
"""

import sys
import os

print("🚀 Testing Stable Recognition for Backend")
print("="*60)

# Add current directory to path
sys.path.append('.')

try:
    from models.face_model_fixed import FaceModel
    print("✅ Model imported successfully!")
except Exception as e:
    print(f"❌ Import failed: {e}")
    print("Creating new model file...")
    # You might need to create the fixed file first
    sys.exit(1)

# Create model
model = FaceModel()

# Check for your photos
photos = []
ashmita_dir = "test_images/Ashmita"
if os.path.exists(ashmita_dir):
    for file in os.listdir(ashmita_dir):
        if file.lower().endswith(('.jpg', '.jpeg', '.png')):
            photos.append(os.path.join(ashmita_dir, file))

print(f"\n📸 Found {len(photos)} photos of Ashmita")

if not photos:
    print("❌ No photos found. Please run capture.py first")
    sys.exit(1)

print(f"\n1. Using photo: {photos[0]}")
print(f"2. Model has {model.get_count()} registered faces")

# Register if not already registered
if model.get_count() == 0:
    print("\n3. Registering Ashmita...")
    result = model.register_person(
        photos[0],
        name="Ashmita",
        email="ashmita@example.com",
        phone="1234567890"
    )
    if "error" in result:
        print(f"   ❌ Registration failed: {result['error']}")
        sys.exit(1)
    else:
        print(f"   ✅ Registered! Person ID: {result['person_id']}")

print(f"\n4. Testing STABLE recognition (what backend will see)...")
print("   This simulates what happens when user stands at check-in kiosk")
print("="*60)

# Test stable recognition multiple times
test_cases = [
    {"photo": photos[0], "description": "Same photo (should match perfectly)"},
    {"photo": photos[1] if len(photos) > 1 else photos[0], 
     "description": "Different photo (might have lower confidence)"}
]

for i, test in enumerate(test_cases):
    print(f"\n🧪 Test Case {i+1}: {test['description']}")
    print(f"   Photo: {test['photo']}")
    
    result = model.get_stable_recognition(
        test['photo'],
        min_confidence=75,
        max_attempts=5
    )
    
    print(f"\n   📊 RESULT FOR BACKEND:")
    print(f"   Status: {result['status']}")
    
    if result['status'] == 'success':
        print(f"   ✅ Match Index: {result.get('match_index', 'N/A')}")
        print(f"   ✅ Person ID: {result.get('person_id', 'N/A')}")
        print(f"   ✅ Name: {result.get('name', 'N/A')}")
        print(f"   ✅ Confidence: {result.get('confidence', 'N/A')}%")
        print(f"   ✅ Attempts: {result.get('attempts', 'N/A')}")
        
        # This is what backend would receive
        backend_data = {
            "found": True,
            "match_index": result.get('match_index'),
            "person_id": result.get('person_id'),
            "name": result.get('name'),
            "confidence": result.get('confidence')
        }
        print(f"\n   📨 Would send to backend: {backend_data}")
        
    elif result['status'] == 'low_confidence':
        print(f"   ⚠️  Name: {result.get('name', 'N/A')}")
        print(f"   ⚠️  Confidence: {result.get('confidence', 'N/A')}% (below threshold)")
        print(f"   ⚠️  Message: {result.get('message', 'N/A')}")
        
        # Backend might ask for confirmation
        print(f"\n   📨 Backend could: Ask for manual confirmation")
        
    else:
        print(f"   ❌ Message: {result.get('message', 'N/A')}")
        print(f"\n   📨 Backend would: Show 'Face not recognized'")

print(f"\n" + "="*60)
print("📹 Test with LIVE webcam? (y/n)")
print("This will show what happens in real event scenario")
choice = input("> ").strip().lower()

if choice == 'y':
    print(f"\n🎥 Starting webcam simulation...")
    print("Stand in front of camera like at check-in kiosk")
    print("Press 'q' in window to quit")
    print("="*60)
    
    model.recognize_from_webcam_stable(confidence_threshold=75)

print(f"\n" + "="*60)
print("✅ TEST COMPLETE!")
print(f"\n📋 Summary:")
print(f"- Your model now has {model.get_count()} registered faces")
print(f"- Stable recognition returns reliable results for backend")
print(f"- Backend will receive match_index for database lookup")
print(f"- Confidence threshold ensures only reliable matches are sent")
print(f"\n📁 Data saved to: {model.data_file}")