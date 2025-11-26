#!/usr/bin/env python3
"""
Backend API Tests for Deep Night Ludo Club
Testing all backend endpoints as specified in the review request
"""

import requests
import json
import sys
from datetime import datetime

# Get backend URL from frontend .env
BACKEND_URL = "https://groupmsg-bot.preview.emergentagent.com/api"

def test_health_check():
    """Test GET /api/ - Health check endpoint"""
    print("\n=== Testing Health Check Endpoint ===")
    try:
        response = requests.get(f"{BACKEND_URL}/")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        
        if response.status_code == 200:
            print("✅ Health check endpoint working")
            return True
        else:
            print("❌ Health check endpoint failed")
            return False
    except Exception as e:
        print(f"❌ Health check endpoint error: {str(e)}")
        return False

def test_bot_health():
    """Test GET /api/health - Bot configuration check"""
    print("\n=== Testing Bot Health Endpoint ===")
    try:
        response = requests.get(f"{BACKEND_URL}/health")
        print(f"Status Code: {response.status_code}")
        data = response.json()
        print(f"Response: {data}")
        
        if response.status_code == 200:
            print(f"✅ Bot health endpoint working")
            print(f"Bot configured: {data.get('bot_configured', False)}")
            print(f"Database connected: {data.get('database_connected', False)}")
            return True
        else:
            print("❌ Bot health endpoint failed")
            return False
    except Exception as e:
        print(f"❌ Bot health endpoint error: {str(e)}")
        return False

def test_send_table_request():
    """Test POST /api/send-table with sample data"""
    print("\n=== Testing Send Table Request Endpoint ===")
    
    # Sample data as specified in review request
    test_data = {
        "username": "TestUser",
        "amount": "2000",
        "type": "Full",
        "gamePlus": "7+",
        "options": {
            "freshId": False,
            "codeAapDoge": False,
            "noIPhone": True,
            "noKingPass": False,
            "autoLoss": False
        }
    }
    
    try:
        response = requests.post(
            f"{BACKEND_URL}/send-table",
            json=test_data,
            headers={"Content-Type": "application/json"}
        )
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        
        # Expected to fail with 500 due to missing Telegram credentials
        if response.status_code == 500:
            response_data = response.json()
            if "Telegram" in response_data.get("detail", ""):
                print("✅ Expected failure - Telegram credentials not configured")
                return True
            else:
                print(f"❌ Unexpected error: {response_data.get('detail')}")
                return False
        elif response.status_code == 200:
            print("✅ Table request sent successfully (unexpected - credentials should not be set)")
            return True
        else:
            print(f"❌ Unexpected status code: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Send table request error: {str(e)}")
        return False

def test_get_tables():
    """Test GET /api/tables - Get all table requests"""
    print("\n=== Testing Get Tables Endpoint ===")
    try:
        response = requests.get(f"{BACKEND_URL}/tables")
        print(f"Status Code: {response.status_code}")
        data = response.json()
        print(f"Response: {data}")
        
        if response.status_code == 200:
            print("✅ Get tables endpoint working")
            tables = data.get("tables", [])
            print(f"Number of tables retrieved: {len(tables)}")
            
            # Check if our test data was stored (even if Telegram send failed)
            if tables:
                latest_table = tables[0]  # Should be sorted by timestamp desc
                print(f"Latest table: {latest_table}")
                if latest_table.get("username") == "TestUser":
                    print("✅ Database storage working - test data found")
                else:
                    print("⚠️ Test data not found in latest entry")
            else:
                print("⚠️ No tables found in database")
            return True
        else:
            print("❌ Get tables endpoint failed")
            return False
    except Exception as e:
        print(f"❌ Get tables endpoint error: {str(e)}")
        return False

def test_error_handling():
    """Test error handling with missing required fields"""
    print("\n=== Testing Error Handling ===")
    
    # Test with missing required fields
    invalid_data = {
        "username": "TestUser",
        # Missing amount, type, gamePlus, options
    }
    
    try:
        response = requests.post(
            f"{BACKEND_URL}/send-table",
            json=invalid_data,
            headers={"Content-Type": "application/json"}
        )
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        
        if response.status_code == 422:  # Validation error
            print("✅ Proper validation error handling")
            return True
        else:
            print(f"❌ Expected 422 validation error, got {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error handling test error: {str(e)}")
        return False

def main():
    """Run all backend tests"""
    print("🎲 Deep Night Ludo Club Backend API Tests")
    print("=" * 50)
    
    results = []
    
    # Run all tests
    results.append(("Health Check", test_health_check()))
    results.append(("Bot Health", test_bot_health()))
    results.append(("Send Table Request", test_send_table_request()))
    results.append(("Get Tables", test_get_tables()))
    results.append(("Error Handling", test_error_handling()))
    
    # Summary
    print("\n" + "=" * 50)
    print("🎯 TEST SUMMARY")
    print("=" * 50)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name}: {status}")
        if result:
            passed += 1
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed!")
        return 0
    else:
        print("⚠️ Some tests failed - see details above")
        return 1

if __name__ == "__main__":
    sys.exit(main())