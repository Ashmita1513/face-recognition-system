# File: organize_data.py
"""
Organize face data structure for events
"""

import os
import shutil
import json
from datetime import datetime

class FaceDataOrganizer:
    def __init__(self, base_dir="face_data"):
        self.base_dir = base_dir
        self.create_structure()
    
    def create_structure(self):
        """Create organized folder structure"""
        folders = [
            "registered",      # For registered attendees
            "pending",         # For pending/awaiting approval
            "test",           # For testing/debugging
            "backup",         # Backup of encodings
            "exports",        # Exported data
            "logs"           # System logs
        ]
        
        subfolders = [
            "registered/photos",
            "registered/encodings",
            "registered/metadata",
            "pending/photos",
            "pending/encodings",
            "test/sample_faces",
            "backup/daily",
            "backup/weekly",
            "exports/json",
            "exports/csv"
        ]
        
        print("📁 Creating organized structure...")
        
        # Create main directory
        os.makedirs(self.base_dir, exist_ok=True)
        
        # Create all folders
        for folder in folders:
            path = os.path.join(self.base_dir, folder)
            os.makedirs(path, exist_ok=True)
            print(f"  ✅ {folder}/")
        
        # Create subfolders
        for subfolder in subfolders:
            path = os.path.join(self.base_dir, subfolder)
            os.makedirs(path, exist_ok=True)
            print(f"  📂 {subfolder}/")
        
        # Create readme
        self.create_readme()
        
        print(f"\n✅ Organized structure created at: {self.base_dir}/")
    
    def create_readme(self):
        """Create README for the structure"""
        readme_content = ""