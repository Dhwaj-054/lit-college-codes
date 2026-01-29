# Movie Poster Setup Checklist

Follow this checklist to enable movie posters in your application.

## ☑️ Pre-Setup Check

- [ ] Application currently runs without errors
- [ ] You can see movie recommendations (even without posters)
- [ ] You have internet connection
- [ ] You have ~5 minutes for setup

---

## 📝 Step 1: Get TMDB Account & API Key

### 1.1 Create Account
- [ ] Go to https://www.themoviedb.org/signup
- [ ] Fill out registration form
- [ ] Verify email address (check spam folder if needed)
- [ ] Log in to TMDB

### 1.2 Request API Key
- [ ] Click your profile icon (top-right)
- [ ] Select "Settings"
- [ ] Click "API" in left sidebar
- [ ] Click "Create" or "Request an API Key"
- [ ] Choose "Developer" option
- [ ] Accept terms and conditions

### 1.3 Fill Application Form
- [ ] Application Name: `Movie Genre Classifier` (or your choice)
- [ ] Application URL: `http://localhost:5000`
- [ ] Application Summary: `Movie recommendation system` (or similar)
- [ ] Submit form

### 1.4 Copy API Key
- [ ] Find your API Key (v3 auth) - NOT the v4 token
- [ ] Copy it to clipboard
- [ ] It should be ~32 characters long
- [ ] Keep this tab open for reference

**Your API Key looks like:** `abc123def456ghi789jkl012mno345pq`

---

## 🔧 Step 2: Configure Your Project

### 2.1 Create .env File
- [ ] Open terminal/command prompt
- [ ] Navigate to project root directory:
  ```bash
  cd path/to/nlp-miniproject
  ```
- [ ] Check you're in the right place (should see `app/` folder):
  ```bash
  dir    # Windows
  ls     # Mac/Linux
  ```
- [ ] Copy the example file:
  ```bash
  copy .env.example .env     # Windows CMD
  cp .env.example .env       # Windows PowerShell / Mac / Linux
  ```
- [ ] Verify .env was created:
  ```bash
  dir .env    # Windows
  ls .env     # Mac/Linux
  ```

### 2.2 Add Your API Key
- [ ] Open `.env` file in text editor (Notepad, VS Code, etc.)
- [ ] Find the line: `TMDB_API_KEY=your_api_key_here`
- [ ] Replace `your_api_key_here` with your actual API key
- [ ] Should look like: `TMDB_API_KEY=abc123def456ghi789jkl012mno345pq`
- [ ] **Important:** No spaces, no quotes around the key
- [ ] Save the file
- [ ] Close the editor

### 2.3 Verify File Contents
- [ ] Reopen `.env` to double-check
- [ ] Confirm API key is correct
- [ ] No extra spaces or characters
- [ ] File is in project root (not in `app/` folder)

---

## 📦 Step 3: Install Dependencies

### 3.1 Update Dependencies
- [ ] Make sure you're in project directory
- [ ] Run:
  ```bash
  pip install -r requirements.txt
  ```
- [ ] Wait for installation to complete
- [ ] Check for any error messages

### 3.2 Verify Installation
- [ ] Check if python-dotenv installed:
  ```bash
  pip show python-dotenv
  ```
- [ ] Should show version info
- [ ] If not found, install manually:
  ```bash
  pip install python-dotenv
  ```

---

## 🧪 Step 4: Test Configuration

### 4.1 Run Test Script
- [ ] In project directory, run:
  ```bash
  python test_tmdb_api.py
  ```

### 4.2 Check Results
- [ ] Should see: `✓ API key found`
- [ ] Should see: `✓ API connection successful`
- [ ] Should see: `✓ Movie search successful`
- [ ] Should see: `✅ ALL TESTS PASSED!`

### 4.3 If Test Fails
- [ ] Read error message carefully
- [ ] Common issues:
  - **API key not found:** Check .env file location and contents
  - **Invalid API key:** Verify you copied the correct key from TMDB
  - **Connection error:** Check internet connection
- [ ] Fix issue and run test again
- [ ] Don't proceed until test passes

---

## 🚀 Step 5: Start Application

### 5.1 Launch Application
- [ ] Run:
  ```bash
  python app/app.py
  ```

### 5.2 Check Console Output
- [ ] Look for: `✓ Movie poster service initialized with TMDB API`
- [ ] Should see: `Model components loaded successfully!`
- [ ] Should **NOT** see: `⚠ Warning: TMDB_API_KEY not found`
- [ ] Note the URL (usually `http://localhost:5000`)

### 5.3 If You See Warning
- [ ] Stop the application (Ctrl+C)
- [ ] Verify .env file is in correct location
- [ ] Check .env file contents
- [ ] Run test script again
- [ ] Restart application

---

## ✅ Step 6: Verify Posters Display

### 6.1 Open Browser
- [ ] Go to `http://localhost:5000`
- [ ] Page should load without errors

### 6.2 Test Recommendations
- [ ] Enter a movie description (e.g., "A thief steals secrets through dreams")
- [ ] Click "Analyze Genre"
- [ ] Wait for results to load

### 6.3 Check Similar Movies Section
- [ ] Scroll down to "Similar Movies" section
- [ ] You should see:
  - [ ] Movie poster images (not gray placeholders)
  - [ ] Movie titles
  - [ ] Star ratings (e.g., ⭐ 8.8)
  - [ ] Match percentages
  - [ ] Genre labels

### 6.4 Interact with Cards
- [ ] Hover over a movie card
- [ ] Should see hover effects (zoom, overlay)
- [ ] Cards should look professional
- [ ] Images should load (may take a moment)

---

## 🎉 Success Indicators

You're all set if you see:

✅ **Console:**
```
✓ Movie poster service initialized with TMDB API
Model components loaded successfully!
Starting Flask application...
```

✅ **Browser:**
- Real movie posters displaying
- Star ratings showing
- Smooth animations
- Professional appearance

✅ **Test Script:**
```
✅ ALL TESTS PASSED!
Your TMDB API key is configured correctly.
Movie posters will be displayed in your application.
```

---

## 🐛 Troubleshooting

### Issue: No posters showing
**Symptoms:** Gray placeholder boxes instead of posters

**Solutions:**
- [ ] Check console for "⚠ Warning" message
- [ ] Verify .env file location (project root, not in app/ folder)
- [ ] Open .env and check API key has no extra spaces
- [ ] Restart the application
- [ ] Run `python test_tmdb_api.py`

---

### Issue: Some posters missing
**Symptoms:** Some movies show posters, others don't

**This is normal!** Reasons:
- Movie not in TMDB database
- Title doesn't match exactly
- API rate limiting (temporary)

**Not a problem:** System shows placeholder for missing posters.

---

### Issue: Test script fails
**Symptoms:** Red ❌ messages

**Check:**
- [ ] Internet connection working?
- [ ] API key copied correctly?
- [ ] Used v3 API Key (not v4 Read Access Token)?
- [ ] .env file in right location?
- [ ] python-dotenv installed?

---

### Issue: "Module not found" error
**Symptoms:** `ModuleNotFoundError: No module named 'dotenv'`

**Solution:**
```bash
pip install python-dotenv
```

---

## 📚 Additional Resources

- **Quick Start:** [QUICK_START_POSTERS.md](QUICK_START_POSTERS.md)
- **Detailed Guide:** [SETUP_MOVIE_POSTERS.md](SETUP_MOVIE_POSTERS.md)
- **Before/After:** [BEFORE_AFTER.md](BEFORE_AFTER.md)
- **Summary:** [CHANGES_SUMMARY.md](CHANGES_SUMMARY.md)

---

## 🎯 Final Check

Before you consider setup complete:

- [ ] Test script passes ✅
- [ ] Application starts without warnings ✅
- [ ] Posters display in browser ✅
- [ ] Hover effects work ✅
- [ ] Multiple recommendations show ✅
- [ ] No console errors ✅

---

## ⏱️ Time Tracking

- [ ] Account creation: ~2 min
- [ ] API key request: ~1 min
- [ ] Configure .env: ~1 min
- [ ] Install deps: ~1 min
- [ ] Test & verify: ~1 min
- **Total:** ~5-6 minutes

---

## 💾 Save This Checklist

Keep this checklist for:
- Setting up on new machines
- Helping team members
- Future reference
- Troubleshooting

---

## 🎊 You're Done!

Congratulations! Your movie recommendation system now shows beautiful posters.

**Enjoy your enhanced application!** 🎬🍿
