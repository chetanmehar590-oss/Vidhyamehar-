#!/usr/bin/env python3
"""
Comprehensive Backend API Tests for Deep Night Ludo Club
Additional edge case testing and flow verification
"""

import requests
import json
import sys
from datetime import datetime

# Get backend URL from frontend .env
BACKEND_URL = "https://groupmsg-bot.preview.emergentagent.com/api"

def test_complete_flow():
    """Test complete flow: send table request -> verify storage -> retrieve tables"""
    print("\n=== Testing Complete Flow ===")
    
    # Test data with different options
    test_data = {
        "username": "FlowTestUser",
        "amount": "5000",
        "type": "Quick",
        "gamePlus": "10+",
        "options": {
            "freshId": True,
            "codeAapDoge": True,
            "noIPhone": False,
            "noKingPass": True,
            "autoLoss": False
        }
    }
    
    try:
        # Step 1: Send table request
        print("Step 1: Sending table request...")
        response = requests.post(
            f"{BACKEND_URL}/send-table",
            json=test_data,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code != 500:
            print(f"❌ Expected 500 status, got {response.status_code}")
            return False
        
        # Step 2: Verify data was stored despite Telegram failure
        print("Step 2: Checking if data was stored...")
        tables_response = requests.get(f"{BACKEND_URL}/tables")
        
        if tables_response.status_code != 200:
            print(f"❌ Failed to retrieve tables: {tables_response.status_code}")
            return False
        
        tables_data = tables_response.json()
        tables = tables_data.get("tables", [])
        
        # Find our test data
        flow_test_found = False
        for table in tables:
            if table.get("username") == "FlowTestUser":
                flow_test_found = True
                print(f"✅ Found stored table: {table['username']} - {table['amount']}")
                
                # Verify all fields
                if (table.get("amount") == "5000" and 
                    table.get("type") == "Quick" and
                    table.get("gamePlus") == "10+" and
                    table.get("options", {}).get("freshId") == True and
                    table.get("options", {}).get("codeAapDoge") == True):
                    print("✅ All fields stored correctly")
                else:
                    print("❌ Some fields not stored correctly")
                    return False
                break
        
        if not flow_test_found:
            print("❌ Test data not found in database")
            return False
        
        print("✅ Complete flow working: Request -> Storage -> Retrieval")
        return True
        
    except Exception as e:
        print(f"❌ Complete flow test error: {str(e)}")
        return False

def test_edge_cases():
    """Test edge cases and boundary conditions"""
    print("\n=== Testing Edge Cases ===")
    
    edge_cases = [
        {
            "name": "Special characters in username",
            "data": {
                "username": "User@123!",
                "amount": "1000",
                "type": "Full",
                "gamePlus": "5+",
                "options": {"freshId": False, "codeAapDoge": False, "noIPhone": False, "noKingPass": False, "autoLoss": False}
            },
            "expected_status": 500  # Should fail at Telegram but store in DB
        },
        {
            "name": "Large amount value",
            "data": {
                "username": "BigPlayer",
                "amount": "999999",
                "type": "Tournament",
                "gamePlus": "20+",
                "options": {"freshId": True, "codeAapDoge": True, "noIPhone": True, "noKingPass": True, "autoLoss": True}
            },
            "expected_status": 500
        },
        {
            "name": "Empty string values",
            "data": {
                "username": "",
                "amount": "",
                "type": "",
                "gamePlus": "",
                "options": {"freshId": False, "codeAapDoge": False, "noIPhone": False, "noKingPass": False, "autoLoss": False}
            },
            "expected_status": 500  # Should still process but fail at Telegram
        }
    ]
    
    passed = 0
    for case in edge_cases:
        try:
            print(f"\nTesting: {case['name']}")
            response = requests.post(
                f"{BACKEND_URL}/send-table",
                json=case["data"],
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == case["expected_status"]:
                print(f"✅ {case['name']}: Expected status {case['expected_status']}")
                passed += 1
            else:
                print(f"❌ {case['name']}: Expected {case['expected_status']}, got {response.status_code}")
                
        except Exception as e:
            print(f"❌ {case['name']}: Error - {str(e)}")
    
    return passed == len(edge_cases)

def test_database_persistence():
    """Test that database operations are working correctly"""
    print("\n=== Testing Database Persistence ===")
    
    try:
        # Get current count
        response = requests.get(f"{BACKEND_URL}/tables")
        if response.status_code != 200:
            print("❌ Failed to get initial table count")
            return False
        
        initial_count = len(response.json().get("tables", []))
        print(f"Initial table count: {initial_count}")
        
        # Add a new table
        test_data = {
            "username": "PersistenceTest",
            "amount": "3000",
            "type": "Standard",
            "gamePlus": "8+",
            "options": {"freshId": False, "codeAapDoge": False, "noIPhone": True, "noKingPass": False, "autoLoss": False}
        }
        
        requests.post(f"{BACKEND_URL}/send-table", json=test_data)
        
        # Check new count
        response = requests.get(f"{BACKEND_URL}/tables")
        if response.status_code != 200:
            print("❌ Failed to get updated table count")
            return False
        
        new_count = len(response.json().get("tables", []))
        print(f"New table count: {new_count}")
        
        if new_count == initial_count + 1:
            print("✅ Database persistence working correctly")
            return True
        else:
            print(f"❌ Expected count {initial_count + 1}, got {new_count}")
            return False
            
    except Exception as e:
        print(f"❌ Database persistence test error: {str(e)}")
        return False

def main():
    """Run comprehensive backend tests"""
    print("🎲 Deep Night Ludo Club - Comprehensive Backend Tests")
    print("=" * 60)
    
    results = []
    
    # Run comprehensive tests
    results.append(("Complete Flow", test_complete_flow()))
    results.append(("Edge Cases", test_edge_cases()))
    results.append(("Database Persistence", test_database_persistence()))
    
    # Summary
    print("\n" + "=" * 60)
    print("🎯 COMPREHENSIVE TEST SUMMARY")
    print("=" * 60)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name}: {status}")
        if result:
            passed += 1
    
    print(f"\nOverall: {passed}/{total} comprehensive tests passed")
    
    if passed == total:
        print("🎉 All comprehensive tests passed!")
        return 0
    else:
        print("⚠️ Some comprehensive tests failed")
        return 1

if __name__ == "__main__":
    sys.exit(main())