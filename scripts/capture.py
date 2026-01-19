# File: capture.py
"""
Capture faces from webcam for testing
"""

import cv2
import os

def capture_faces():
    print("📸 FACE CAPTURE UTILITY")
    print("=" * 40)
    
    # Get person name
    name = input("Enter person's name: ").strip()
    if not name:
        name = "Unknown"
    
    # Create folder
    save_dir = f"test_images/{name}"
    os.makedirs(save_dir, exist_ok=True)
    
    # Start webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ Cannot open webcam")
        return
    
    print(f"\n📹 Ready! Looking at {name}")
    print("Commands:")
    print("  Press 'c' to capture photo")
    print("  Press 'q' to quit")
    print(f"  Photos will save to: {save_dir}/")
    
    count = 0
    while count < 10:  # Max 10 photos
        ret, frame = cap.read()
        if not ret:
            break
        
        # Show frame with instructions
        display = frame.copy()
        cv2.putText(display, f"{name} - Photo {count+1}/10", 
                   (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(display, "Press 'c' to capture, 'q' to quit", 
                   (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        cv2.imshow("Capture Face", display)
        
        key = cv2.waitKey(1) & 0xFF
        
        if key == ord('c'):
            # Save photo
            filename = f"{save_dir}/face_{count+1:02d}.jpg"
            cv2.imwrite(filename, frame)
            print(f"  ✅ Saved: {filename}")
            count += 1
        
        elif key == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    
    print(f"\n✅ Captured {count} photos of {name}")
    print(f"📁 Saved in: {save_dir}")

if __name__ == "__main__":
    capture_faces()