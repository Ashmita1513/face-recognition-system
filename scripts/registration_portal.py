# File: registration_portal.py
"""
Registration portal for new members
Organized face capture and storage
"""

import cv2
import os
import json
import time
from datetime import datetime

class RegistrationPortal:
    def __init__(self, data_dir="face_data"):
        self.data_dir = data_dir
        self.attendee_counter = self._get_next_id()
        
    def _get_next_id(self):
        """Get next available ID"""
        max_id = 0
        
        for root, dirs, files in os.walk(self.data_dir):
            for file in files:
                if file.startswith("attendee_") and file.endswith("_info.json"):
                    try:
                        attendee_id = int(file.split("_")[1])
                        max_id = max(max_id, attendee_id)
                    except:
                        pass
        
        return max_id + 1
    
    def capture_new_member(self):
        """Capture photos for new member"""
        print("🎪 NEW MEMBER REGISTRATION")
        print("="*50)
        
        # Get member details
        print("\n📝 Enter member details:")
        name = input("  Full Name: ").strip()
        email = input("  Email: ").strip()
        phone = input("  Phone: ").strip()
        
        if not name:
            print("❌ Name is required")
            return
        
        # Create attendee ID
        attendee_id = self.attendee_counter
        self.attendee_counter += 1
        
        print(f"\n📸 Member ID: {attendee_id}")
        print("  Please look at the camera. We'll take 5 photos.")
        print("  Press 'c' to capture, 'q' to quit early")
        
        # Create directory for this member
        member_dir = os.path.join(self.data_dir, "pending", "photos", f"attendee_{attendee_id}")
        os.makedirs(member_dir, exist_ok=True)
        
        # Start webcam
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("❌ Cannot open webcam")
            return
        
        photos_taken = 0
        max_photos = 5
        
        while photos_taken < max_photos:
            ret, frame = cap.read()
            if not ret:
                break
            
            # Display
            display = frame.copy()
            cv2.putText(display, f"{name} - Photo {photos_taken+1}/{max_photos}", 
                       (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(display, "Press 'c' to capture", 
                       (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            
            cv2.imshow("Registration - Capture Photos", display)
            
            key = cv2.waitKey(1) & 0xFF
            
            if key == ord('c'):
                # Save photo
                timestamp = datetime.now().strftime("%H%M%S")
                filename = f"attendee_{attendee_id}_photo_{photos_taken+1}_{timestamp}.jpg"
                filepath = os.path.join(member_dir, filename)
                
                cv2.imwrite(filepath, frame)
                print(f"  ✅ Saved: {filename}")
                photos_taken += 1
            
            elif key == ord('q'):
                print("  ⏹️ Early quit")
                break
        
        cap.release()
        cv2.destroyAllWindows()
        
        if photos_taken == 0:
            print("❌ No photos captured")
            # Clean up empty directory
            try:
                os.rmdir(member_dir)
            except:
                pass
            return
        
        # Save metadata
        metadata = {
            "attendee_id": attendee_id,
            "name": name,
            "email": email,
            "phone": phone,
            "status": "pending",
            "registration_date": datetime.now().isoformat(),
            "photos_taken": photos_taken,
            "photos_directory": member_dir,
            "requires_approval": True
        }
        
        meta_file = os.path.join(self.data_dir, "pending", "metadata", 
                               f"attendee_{attendee_id}_info.json")
        with open(meta_file, "w") as f:
            json.dump(metadata, f, indent=2)
        
        print(f"\n✅ REGISTRATION COMPLETE!")
        print(f"   Name: {name}")
        print(f"   ID: {attendee_id}")
        print(f"   Photos: {photos_taken} saved")
        print(f"   Status: Pending approval")
        print(f"   Data saved to: {member_dir}")
        
        return attendee_id
    
    def list_pending_registrations(self):
        """List all pending registrations"""
        pending_dir = os.path.join(self.data_dir, "pending", "metadata")
        
        if not os.path.exists(pending_dir):
            print("📭 No pending registrations")
            return []
        
        pending = []
        for file in os.listdir(pending_dir):
            if file.endswith("_info.json"):
                with open(os.path.join(pending_dir, file), "r") as f:
                    data = json.load(f)
                    pending.append(data)
        
        print(f"\n📋 PENDING REGISTRATIONS ({len(pending)}):")
        print("="*50)
        
        for i, reg in enumerate(pending, 1):
            print(f"\n{i}. {reg['name']} (ID: {reg['attendee_id']})")
            print(f"   Email: {reg.get('email', 'N/A')}")
            print(f"   Phone: {reg.get('phone', 'N/A')}")
            print(f"   Photos: {reg.get('photos_taken', 0)}")
            print(f"   Registered: {reg.get('registration_date', 'N/A')}")
        
        return pending
    
    def approve_registration(self, attendee_id):
        """Approve a pending registration"""
        from models.organized_model import OrganizedFaceModel
        
        model = OrganizedFaceModel()
        result = model.approve_attendee(attendee_id)
        
        if "error" in result:
            print(f"❌ Error: {result['error']}")
        else:
            print(f"✅ Approved! {result['message']}")
        
        return result

if __name__ == "__main__":
    portal = RegistrationPortal()
    
    while True:
        print("\n" + "="*50)
        print("🎪 EVENT REGISTRATION PORTAL")
        print("="*50)
        print("1. Register New Member")
        print("2. View Pending Registrations")
        print("3. Approve Registration")
        print("4. Exit")
        
        choice = input("\nSelect option: ").strip()
        
        if choice == "1":
            portal.capture_new_member()
        
        elif choice == "2":
            portal.list_pending_registrations()
        
        elif choice == "3":
            try:
                attendee_id = int(input("Enter attendee ID to approve: "))
                portal.approve_registration(attendee_id)
            except ValueError:
                print("❌ Please enter a valid ID number")
        
        elif choice == "4":
            print("👋 Goodbye!")
            break
        
        else:
            print("❌ Invalid option")