# Troubleshooting Guide: Movie Posters

Complete troubleshooting guide for movie poster display issues.

---

## 🔍 Quick Diagnostics

Run these checks first:

```bash
# 1. Test API configuration
python test_tmdb_api.py

# 2. Check environment variables (Windows PowerShell)
$env:TMDB_API_KEY

# 3. Verify file exists
dir .env    # Windows
ls .env     # Mac/Linux
```

---

## ❌ Common Issues & Solutions

### Issue 1: "TMDB_API_KEY not found" Warning

**Symptoms:**
```
⚠ Warning: TMDB_API_KEY not found. Movie posters will not be displayed.
  See QUICK_START_POSTERS.md for setup instructions.
```

**Cause:** Application can't find your API key.

**Solutions:**

#### Solution A: Check .env File Location
```bash
# .env must be in PROJECT ROOT, not in app/ folder
# Correct:
nlp-miniproject/
  ├── .env          ← HERE
  ├── app/
  └── ...

# Wrong:
nlp-miniproject/
  ├── app/
  │   └── .env      ← NOT HERE
  └── ...
```

#### Solution B: Verify File Contents
- [ ] Open `.env` file
- [ ] Should contain: `TMDB_API_KEY=your_actual_key`
- [ ] No quotes around key
- [ ] No spaces before/after `=`
- [ ] Key should be ~32 characters

#### Solution C: Check File Name
- [ ] File must be named `.env` (with dot)
- [ ] Not `env.txt` or `.env.txt`
- [ ] Not `.env.example`
- [ ] On Windows, make sure "Hide extensions" is off to see real name

#### Solution D: Restart Application
```bash
# Stop app (Ctrl+C)
# Then restart
python app/app.py
```

---

### Issue 2: Placeholder Images Instead of Posters

**Symptoms:**
- Gray boxes saying "No Poster"
- Or blank images
- Movie info shows but no pictures

**Diagnostic Steps:**

#### Step 1: Check Console
Look for these messages:
```
✓ Movie poster service initialized with TMDB API  ← Good!
⚠ Warning: TMDB_API_KEY not found               ← Bad!
```

#### Step 2: Test API Key
```bash
python test_tmdb_api.py
```

Should see:
- `✓ API key found`
- `✓ API connection successful`
- `✅ ALL TESTS PASSED!`

#### Step 3: Check Browser Console (F12)
- Open Developer Tools (F12)
- Look for:
  - Network errors (red)
  - Failed image requests
  - CORS errors

**Solutions:**

#### If API Key Not Found:
- See "Issue 1" above

#### If API Key Invalid:
- [ ] Go to TMDB: https://www.themoviedb.org/settings/api
- [ ] Copy **API Key (v3 auth)** - NOT v4 Read Access Token
- [ ] Update `.env` file
- [ ] Restart application

#### If Some Posters Missing:
This is **normal**! Reasons:
- Movie title doesn't exactly match TMDB database
- Movie not in TMDB (rare, old, or very new movies)
- System shows placeholder automatically

---

### Issue 3: Test Script Fails

**Symptoms:**
```bash
python test_tmdb_api.py
❌ FAILED: ...
```

#### Error: "TMDB_API_KEY not found"

**Solution:**
```bash
# 1. Check .env exists in project root
dir .env    # Windows
ls .env     # Mac/Linux

# 2. Check contents
type .env   # Windows
cat .env    # Mac/Linux

# 3. Should see:
TMDB_API_KEY=your_key_here

# 4. If not, create it:
copy .env.example .env     # Windows
cp .env.example .env       # Mac/Linux

# 5. Edit and add your key
notepad .env  # Windows
```

#### Error: "Invalid API key" (401)

**Cause:** API key is wrong or revoked

**Solution:**
- [ ] Go to TMDB settings: https://www.themoviedb.org/settings/api
- [ ] Verify key is still valid
- [ ] Copy the correct key (v3, not v4)
- [ ] Update `.env`
- [ ] Ensure no extra spaces
- [ ] Test again

#### Error: "Connection timeout" or "Cannot connect"

**Cause:** Network issues

**Solutions:**
- [ ] Check internet connection
- [ ] Try opening https://www.themoviedb.org in browser
- [ ] Check firewall settings
- [ ] Try different network
- [ ] Wait and retry (TMDB might be down)

---

### Issue 4: "ModuleNotFoundError: No module named 'dotenv'"

**Symptoms:**
```python
ModuleNotFoundError: No module named 'dotenv'
```

**Cause:** `python-dotenv` not installed

**Solution:**
```bash
# Install the package
pip install python-dotenv

# Or install all requirements
pip install -r requirements.txt

# Verify installation
pip show python-dotenv
```

---

### Issue 5: Posters Load Slowly or Not at All

**Symptoms:**
- Long wait time
- Some posters never load
- Blank spaces

**Causes & Solutions:**

#### Slow Internet Connection
- **Solution:** Wait longer, images will load
- **Workaround:** Images are cached after first load

#### Rate Limiting
- **Cause:** Too many API requests too quickly
- **Solution:** Wait 30 seconds and try again
- **Note:** Free tier allows 40,000+ requests/day

#### CORS Issues
- **Symptom:** Browser console shows CORS errors
- **Solution:** This shouldn't happen, but if it does:
  - Clear browser cache
  - Try different browser
  - Restart application

---

### Issue 6: Application Won't Start

**Symptoms:**
```python
Error loading model components: ...
```

**Solutions:**

#### Missing Model Files
```bash
# Train the models first
python train.py

# This creates:
# - models/best_model.pkl
# - models/feature_extractor.pkl
# - models/preprocessor.pkl
```

#### Missing Data Files
```bash
# Ensure data file exists:
data/movies_dataset.csv
```

#### Import Errors
```bash
# Install all dependencies
pip install -r requirements.txt

# Or manually:
pip install flask pandas numpy scikit-learn nltk requests python-dotenv
```

---

### Issue 7: Wrong API Key Type Used

**Symptoms:**
- Test script fails with authentication error
- Console shows "Invalid API key"

**Problem:** Using v4 Read Access Token instead of v3 API Key

**Solution:**

On TMDB API page, you'll see TWO keys:

✅ **Use This:** API Key (v3 auth)
```
abc123def456ghi789jkl012mno345pq  ← ~32 characters
```

❌ **Don't Use This:** API Read Access Token (v4)
```
eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOi...  ← Very long, starts with "eyJ"
```

**Copy the SHORT one (v3 API Key)**

---

## 🔧 Advanced Diagnostics

### Check Environment Variable Loading

Create a test file `test_env.py`:
```python
import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv('TMDB_API_KEY')

if key:
    print(f"✓ Key found: {key[:8]}...{key[-4:]}")
    print(f"  Length: {len(key)}")
else:
    print("❌ Key not found")
    print(f"  Current directory: {os.getcwd()}")
    print(f"  .env exists: {os.path.exists('.env')}")
```

Run:
```bash
python test_env.py
```

Should show:
```
✓ Key found: abc123de...45pq
  Length: 32
```

---

### Manual API Test

Test API directly:
```bash
# Replace YOUR_KEY with your actual key
curl "https://api.themoviedb.org/3/movie/550?api_key=YOUR_KEY"
```

Should return JSON with movie data for "Fight Club"

---

### Check File Permissions

**Windows:**
```cmd
icacls .env
```

**Mac/Linux:**
```bash
ls -la .env
# Should be readable by you
chmod 600 .env  # If needed
```

---

## 📊 Diagnostic Checklist

Work through this systematically:

- [ ] `.env` file exists in project root
- [ ] `.env` file contains `TMDB_API_KEY=...`
- [ ] API key is v3 (32 characters, no spaces)
- [ ] `python-dotenv` is installed
- [ ] `test_tmdb_api.py` passes
- [ ] Application starts without warnings
- [ ] Internet connection is working
- [ ] Firewall allows Python to access internet
- [ ] TMDB website is accessible

---

## 🆘 Still Not Working?

### Collect Information

Gather this info for debugging:

1. **Operating System:**
   ```bash
   # Windows
   ver
   
   # Mac/Linux  
   uname -a
   ```

2. **Python Version:**
   ```bash
   python --version
   ```

3. **Installed Packages:**
   ```bash
   pip list
   ```

4. **Test Script Output:**
   ```bash
   python test_tmdb_api.py > test_output.txt 2>&1
   ```

5. **Application Console Output:**
   ```bash
   python app/app.py > app_output.txt 2>&1
   ```

6. **Browser Console Errors:**
   - Open Developer Tools (F12)
   - Copy any red errors

### Temporary Workaround

If you need the app running NOW without posters:

- Just don't set the API key
- System works normally without it
- Placeholders shown for posters
- All other features work fine

---

## 🎯 Success Criteria

You know it's working when:

✅ **Test script shows:**
```
✅ ALL TESTS PASSED!
```

✅ **Application console shows:**
```
✓ Movie poster service initialized with TMDB API
```

✅ **Browser shows:**
- Real movie posters
- Star ratings
- No gray placeholder boxes
- Smooth hover effects

---

## 📞 Getting More Help

1. **Read these guides:**
   - [QUICK_START_POSTERS.md](QUICK_START_POSTERS.md) - Quick setup
   - [SETUP_MOVIE_POSTERS.md](SETUP_MOVIE_POSTERS.md) - Detailed steps
   - [SETUP_CHECKLIST.md](SETUP_CHECKLIST.md) - Step-by-step checklist

2. **Run diagnostic commands:**
   ```bash
   python test_tmdb_api.py
   python test_env.py  # If you created it
   ```

3. **Check TMDB API Status:**
   - Visit: https://www.themoviedb.org/talk/category/5047958519c29526b50017d6

4. **Review TMDB Documentation:**
   - https://developers.themoviedb.org/3/getting-started/introduction

---

## 🐛 Reporting Issues

If you find a bug in the code:

Include:
- Operating system
- Python version  
- Full error message
- Steps to reproduce
- Output from `test_tmdb_api.py`
- Screenshot of issue

---

## ✅ Resolved? Great!

Once working:
- [ ] Test with different movie descriptions
- [ ] Check multiple recommendations
- [ ] Verify hover effects
- [ ] Enjoy your enhanced app! 🎉
