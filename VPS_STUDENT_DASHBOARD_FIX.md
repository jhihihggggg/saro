# 🚨 VPS Student Dashboard Fix Guide

## Problem
Student dashboard showing "Loading exams..." and not displaying:
- Monthly Exams & Results
- Online Resources
- AI Solver

## Root Cause
The VPS database hasn't been migrated to include the new features. The API endpoint `/api/students/me/batches` is failing because the database structure is outdated.

---

## ✅ SOLUTION (Follow these steps on your VPS)

### Step 1: SSH to your VPS
```bash
ssh root@vmi2823196.contaboserver.net
# Or use your SSH key/password
```

### Step 2: Navigate to your app directory
```bash
cd /var/www/saroyarsir
# OR
cd /var/www/saro
```

### Step 3: Test what's wrong (Optional but recommended)
```bash
source venv/bin/activate
python3 test_student_dashboard.py
```

This will show you exactly what's missing.

### Step 4: Run the database migration script
```bash
bash fix_vps_database.sh
```

This script will:
- ✅ Add missing database columns (mother_name, archive fields)
- ✅ Create the documents table
- ✅ Reset all student passwords to phone last 4 digits
- ✅ Restart the service automatically

### Step 5: Verify the fix
After the script completes, try:

1. **Login as a student:**
   - Phone: Student's full phone number (e.g., 01912345678)
   - Password: Last 4 digits (e.g., 5678)

2. **Check the dashboard:**
   - Click "Monthly Exams" - Should show exams or "no exams" message (not stuck loading)
   - Click "Online Resources" - Should show uploaded PDFs
   - Click "AI Solver" - Should show AI question interface

---

## 🔍 If Still Not Working

### Check Browser Console
1. Open browser developer tools (F12)
2. Go to Console tab
3. Look for red errors
4. Copy the error message

### Check Flask Logs
```bash
sudo journalctl -u saro -n 100 --no-pager
```

Look for Python errors or API failures.

### Test API Endpoint Directly
```bash
# This should return JSON with batches or an auth error
curl -i http://localhost:5000/api/students/me/batches
```

### Verify Service is Running
```bash
sudo systemctl status saro
```

Should show "active (running)" in green.

---

## 📊 What Each Section Does

### 1. Monthly Exams (Read-Only)
- Shows all monthly exams for student's batch
- Displays subject-wise marks
- Shows ranking if teacher generated it
- **Student CANNOT edit** - view only

### 2. Online Resources (Download Only)
- Shows all PDFs uploaded by teachers
- Organized by: Online Books & Question Bank
- Filter by class, subject, chapter
- **Student CANNOT upload** - download only

### 3. AI Solver (Praggo AI)
- Student can ask questions
- Supports subjects: Math, Physics, Chemistry, Biology
- Shows question history
- Uses Praggo AI API (or demo mode if not configured)

---

## 🆘 Emergency Fallback

If the script fails, run migrations manually:

```bash
cd /var/www/saroyarsir
source venv/bin/activate

# Run each migration
python3 migrate_add_archive_fields.py
python3 migrate_add_mother_name.py
python3 migrate_add_documents.py

# Reset passwords
python3 reset_all_student_passwords.py

# Restart service
sudo systemctl restart saro
```

---

## ✅ Success Indicators

You'll know it's fixed when:
1. ✅ Student login works with last 4 digits
2. ✅ "Monthly Exams" page loads (shows content or "no exams")
3. ✅ "Online Resources" shows PDF list
4. ✅ "AI Solver" shows question form
5. ✅ No "Loading exams..." stuck message

---

## 📝 Notes

- Students use: **Phone + Last 4 Digits** as password
- Example: Phone `01912345678` → Password `5678`
- Teachers still use hashed passwords (unchanged)
- All student data is **read-only** (they can view but not edit)

---

**After running the fix script, the student dashboard will work perfectly! 🎉**
