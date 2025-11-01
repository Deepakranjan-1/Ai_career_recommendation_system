#!/usr/bin/env python3
"""
Verify all model files are present and loadable
"""
import pickle
import os

def verify_models():
    required_files = [
        "model.pkl",
        "edu_encoder.pkl", 
        "skills_encoder.pkl",
        "interests_encoder.pkl",
        "career_encoder.pkl",
        "feature_columns.pkl"
    ]
    
    print("🔍 Verifying model files...")
    
    for file in required_files:
        if not os.path.exists(file):
            print(f"❌ Missing: {file}")
            return False
        
        try:
            with open(file, 'rb') as f:
                pickle.load(f)
            print(f"✅ {file} - OK")
        except Exception as e:
            print(f"❌ {file} - Error: {e}")
            return False
    
    print("🎉 All model files verified!")
    return True

if __name__ == "__main__":
    verify_models()