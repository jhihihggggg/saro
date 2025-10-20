#!/usr/bin/env python3
"""
Test script to verify student dashboard functionality
Run this on your VPS to check what's wrong
"""

import sys
from app import create_app
from models import db, User, Batch

def test_student_dashboard():
    """Test student dashboard requirements"""
    app = create_app()
    
    with app.app_context():
        print("=" * 60)
        print("TESTING STUDENT DASHBOARD REQUIREMENTS")
        print("=" * 60)
        print()
        
        # 1. Check if students exist
        print("1️⃣  Checking for students in database...")
        students = User.query.filter_by(role='student').all()
        print(f"   ✅ Found {len(students)} students")
        
        if students:
            # Pick first student for testing
            test_student = students[0]
            print(f"   📝 Testing with: {test_student.name} (ID: {test_student.id})")
            print(f"   📞 Phone: {test_student.phone}")
            
            # 2. Check if student has batches
            print()
            print("2️⃣  Checking student's batch enrollment...")
            if hasattr(test_student, 'batches'):
                student_batches = test_student.batches
                print(f"   ✅ Student enrolled in {len(student_batches)} batch(es)")
                for batch in student_batches:
                    print(f"      - {batch.name} (ID: {batch.id})")
            else:
                print("   ❌ ERROR: Student model doesn't have 'batches' relationship!")
                print("      This means the database migration hasn't been run!")
                return False
            
            # 3. Check if Batch model exists
            print()
            print("3️⃣  Checking Batch model...")
            try:
                all_batches = Batch.query.all()
                print(f"   ✅ Found {len(all_batches)} total batches in system")
            except Exception as e:
                print(f"   ❌ ERROR: {e}")
                return False
            
            # 4. Test password format
            print()
            print("4️⃣  Checking student password format...")
            if test_student.phone and len(test_student.phone) >= 4:
                last_4 = test_student.phone[-4:]
                print(f"   📝 Student can login with:")
                print(f"      Phone: {test_student.phone}")
                print(f"      Password: {last_4} (last 4 digits)")
            else:
                print(f"   ⚠️  Student phone: {test_student.phone}")
            
        else:
            print("   ⚠️  No students found in database!")
        
        print()
        print("=" * 60)
        print("DIAGNOSIS COMPLETE")
        print("=" * 60)
        
        return True

if __name__ == '__main__':
    try:
        test_student_dashboard()
    except Exception as e:
        print(f"\n❌ CRITICAL ERROR: {e}")
        print("\nThis usually means:")
        print("1. Database hasn't been migrated")
        print("2. Missing required tables or columns")
        print("\n💡 SOLUTION: Run 'bash fix_vps_database.sh'")
        sys.exit(1)
