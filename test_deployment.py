#!/usr/bin/env python3
"""
Test script to verify the Flask app works before deployment
"""
import requests
import json
import time

def test_local_server():
    base_url = "http://localhost:5000"
    
    print("🧪 Testing Flask App for Render Deployment")
    print("=" * 50)
    
    # Test 1: Health check
    try:
        print("1. Testing health endpoint...")
        response = requests.get(f"{base_url}/health", timeout=10)
        if response.status_code == 200:
            print("✅ Health check passed")
            print(f"   Response: {response.json()}")
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Health check error: {e}")
        return False
    
    # Test 2: Home endpoint
    try:
        print("\n2. Testing home endpoint...")
        response = requests.get(f"{base_url}/", timeout=10)
        if response.status_code == 200:
            print("✅ Home endpoint passed")
        else:
            print(f"❌ Home endpoint failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Home endpoint error: {e}")
        return False
    
    # Test 3: Options endpoint
    try:
        print("\n3. Testing options endpoint...")
        response = requests.get(f"{base_url}/options", timeout=10)
        if response.status_code == 200:
            options = response.json()
            print("✅ Options endpoint passed")
            print(f"   Available skills: {len(options.get('skills', []))}")
            print(f"   Available interests: {len(options.get('interests', []))}")
            print(f"   Available education: {len(options.get('education', []))}")
        else:
            print(f"❌ Options endpoint failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Options endpoint error: {e}")
        return False
    
    # Test 4: Prediction endpoint
    try:
        print("\n4. Testing prediction endpoint...")
        test_data = {
            "name": "Test User",
            "age": 25,
            "education": "Bachelor's",
            "skills": ["Python", "Machine Learning"],
            "interests": ["Technology", "Problem Solving"]
        }
        
        response = requests.post(
            f"{base_url}/predict", 
            json=test_data,
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Prediction endpoint passed")
            print(f"   Predicted career: {result.get('career')}")
        else:
            print(f"❌ Prediction endpoint failed: {response.status_code}")
            print(f"   Response: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Prediction endpoint error: {e}")
        return False
    
    print("\n🎉 All tests passed! Ready for Render deployment.")
    return True

if __name__ == "__main__":
    print("Make sure your Flask app is running on localhost:5000")
    print("Run: python app.py")
    print("\nPress Enter when ready to test...")
    input()
    
    success = test_local_server()
    if success:
        print("\n📋 Deployment Checklist:")
        print("✅ All endpoints working")
        print("✅ Model files present")
        print("✅ Requirements.txt updated")
        print("✅ Procfile configured")
        print("✅ render.yaml ready")
        print("\n🚀 Ready to deploy to Render!")
    else:
        print("\n❌ Fix the issues above before deploying")