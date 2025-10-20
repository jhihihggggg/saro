# 🧪 Local Testing Guide - Student Dashboard

## 🚀 Quick Start

### 1. Start the Flask Server
```bash
cd /workspaces/saro
.venv/bin/python app.py
```

Server will start on: **http://127.0.0.1:5000**

### 2. Open in Browser
Navigate to: **http://localhost:5000**

---

## 👨‍🎓 Test Student Login

### Default Test Student Credentials:
- **Phone:** `01712345678`
- **Password:** `5678` (last 4 digits of phone)

### Creating More Test Students:
```bash
.venv/bin/python create_test_student.py
```

---

## ✅ What to Test - Student Dashboard Features

### 1. **Dashboard (Home)**
- ✅ Shows overview stats
- ✅ Total exams count
- ✅ Average score
- ✅ Attendance percentage
- ✅ Pending fees

### 2. **Monthly Exams** 📊
**Location:** Click "Monthly Exams" in sidebar

**What You Should See:**
- ✅ Loading indicator appears first
- ✅ If student has batches: Shows exams list grouped by month
- ✅ If no batches: Shows "You are not enrolled in any batch" message
- ✅ Click on an exam card to see:
  - Subject-wise marks
  - Total marks
  - Percentage
  - Ranking (if teacher generated it)
- ✅ **READ-ONLY** - Student cannot edit anything

**Expected Behavior:**
```
Loading exams...
↓
[Fetches /api/students/me/batches]
↓
[Fetches /api/monthly-exams/ filtered by student's batch]
↓
Displays exams or "no exams" message
```

### 3. **Online Resources** 📚
**Location:** Click "Online Resources" in sidebar

**What You Should See:**
- ✅ Category filters: All Documents, Online Books, Question Bank
- ✅ Search filters: Class, Subject, Chapter
- ✅ PDF list with:
  - Category badge (📖 Book or ❓ Question)
  - Class, Subject, Chapter info
  - File size
  - Upload date
  - Download count
- ✅ **Download button ONLY** (no upload/delete for students)
- ✅ Click download → PDF downloads

**Expected Behavior:**
```
Loading documents...
↓
[Fetches /api/documents/?include_inactive=true]
↓
Displays PDF cards with download buttons
```

### 4. **AI Solver** 🤖
**Location:** Click "AI Solver" in sidebar

**What You Should See:**
- ✅ Question input textarea
- ✅ Subject selector (Mathematics, Physics, Chemistry, Biology)
- ✅ Difficulty selector (Easy, Medium, Hard)
- ✅ "Get Answer" button
- ✅ Question history section
- ✅ Answer display with:
  - Question echo
  - Step-by-step solution
  - Final answer
  - Copy/Share buttons

**Expected Behavior:**
```
Enter question → Select subject/difficulty → Click "Get Answer"
↓
[Sends POST to /api/ai/ask-question]
↓
Shows answer with solution steps
↓
Saves to local storage history
```

**Note:** If Praggo AI API is not configured, it runs in **demo mode** with mock answers.

### 5. **Attendance** 📅
- ✅ Shows attendance records
- ✅ Present/Absent indicators
- ✅ Date-wise listing
- ✅ **READ-ONLY**

### 6. **Fees** 💰
- ✅ Shows fee records
- ✅ Paid/Unpaid status
- ✅ Amount details
- ✅ **READ-ONLY**

### 7. **Profile** 👤
- ✅ Shows student information
- ✅ Name, phone, email
- ✅ Class, batch info
- ✅ Guardian details
- ✅ **READ-ONLY**

---

## 🐛 Debugging Issues

### Issue: "Loading exams..." Stuck

**Check Browser Console (F12):**
```javascript
// Look for errors like:
Failed to fetch
TypeError: Cannot read property
401 Unauthorized
```

**Check Flask Logs:**
```bash
# In the terminal where Flask is running, look for:
GET /api/students/me/batches HTTP/1.1" 401
GET /api/monthly-exams/ HTTP/1.1" 500
```

**Solution:**
- Check if student is logged in (session active)
- Check if `/api/students/me/batches` endpoint exists
- Verify database has batches table
- Run migrations if needed

### Issue: Online Resources Empty

**Check:**
1. Are there PDFs uploaded? (Login as teacher and upload)
2. Check browser console for API errors
3. Verify `/api/documents/` endpoint returns data

**Test API Directly:**
```bash
curl http://localhost:5000/api/documents/?include_inactive=true
```

### Issue: AI Solver Not Working

**Expected Behavior:**
- If Praggo AI not configured → Shows demo answers
- If configured → Shows real AI answers

**Check:**
```python
# In config.py or settings, check:
PRAGGO_AI_API_KEY = os.getenv('PRAGGO_AI_API_KEY', None)
```

If `None` → Demo mode (this is normal for testing)

---

## 📊 API Endpoints to Test

### 1. Get Student Batches
```bash
curl -H "Cookie: session=..." http://localhost:5000/api/students/me/batches
```

**Expected Response:**
```json
{
  "success": true,
  "data": {
    "batches": [
      {
        "id": 1,
        "name": "HSC Science Batch",
        "subject": "Chemistry"
      }
    ]
  }
}
```

### 2. Get Monthly Exams
```bash
curl http://localhost:5000/api/monthly-exams/
```

**Expected Response:**
```json
{
  "success": true,
  "data": {
    "exams": [
      {
        "id": 1,
        "title": "October Monthly Exam",
        "batch_id": 1,
        "month": "October",
        "year": 2025
      }
    ]
  }
}
```

### 3. Get Documents
```bash
curl http://localhost:5000/api/documents/?include_inactive=true
```

**Expected Response:**
```json
{
  "success": true,
  "data": {
    "documents": [
      {
        "id": 1,
        "file_name": "chemistry_chapter1.pdf",
        "class_name": "HSC Science",
        "book_name": "Chemistry",
        "chapter_name": "Chapter 1"
      }
    ]
  }
}
```

---

## 🎯 Success Checklist

After testing, confirm these work:

- [ ] Student can login with phone + last 4 digits
- [ ] Dashboard shows overview stats
- [ ] Monthly Exams page loads (shows exams or "no batch" message)
- [ ] Online Resources page loads (shows PDFs or "no documents")
- [ ] AI Solver page loads and accepts questions
- [ ] Attendance page loads
- [ ] Fees page loads
- [ ] Profile page loads
- [ ] No "Upload PDF" button in Online Resources (student view)
- [ ] No "Edit" buttons in Monthly Exams (read-only)
- [ ] Navigation menu shows 7 items:
  1. Dashboard
  2. Monthly Exams
  3. Online Resources
  4. AI Solver
  5. Attendance
  6. Fees
  7. Profile
- [ ] **NO "Online Exams" menu item** (this was removed)

---

## 🔧 Common Fixes

### Clear Browser Cache
```
Ctrl + Shift + R (Windows/Linux)
Cmd + Shift + R (Mac)
```

### Reset Database
```bash
rm instance/app.db
.venv/bin/python setup_db.py
.venv/bin/python create_test_student.py
```

### Restart Flask
```bash
# Stop: Ctrl+C in terminal
# Start: .venv/bin/python app.py
```

---

## 📝 Notes

- **Port:** Flask runs on port 5000 by default
- **Database:** SQLite at `instance/app.db`
- **Sessions:** Stored in memory (lost on restart)
- **Student Password:** Always last 4 digits of phone number
- **Teacher Password:** Hashed (use bcrypt)
- **Demo Mode:** AI Solver works without Praggo API (shows mock answers)

---

## 🎉 Ready for VPS Deployment?

If everything works locally, deploy to VPS:

1. **Commit changes:**
   ```bash
   git add .
   git commit -m "Student dashboard tested and working"
   git push origin main
   ```

2. **On VPS:**
   ```bash
   cd /var/www/saroyarsir
   bash force_update_vps.sh
   ```

3. **Clear browser cache** and test on VPS!

---

**Happy Testing! 🚀**
