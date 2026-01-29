# Quick Start: Enable Movie Posters (2 Minutes)

## 🎬 Get Your Free API Key

1. **Go to:** https://www.themoviedb.org/signup
2. **Create account** and verify email
3. **Navigate to:** Profile → Settings → API → Create
4. **Choose:** Developer (free)
5. **Copy** your API Key (v3 auth)

## 🔧 Configure Your Project

### Step 1: Create .env file
```bash
# In project root directory
cp .env.example .env
```

### Step 2: Add your API key
Open `.env` and replace with your actual key:
```
TMDB_API_KEY=your_actual_api_key_here
```

### Step 3: Install dependencies
```bash
pip install python-dotenv
```

### Step 4: Restart the app
```bash
python app/app.py
```

## ✅ Test It

1. Open http://localhost:5000
2. Enter a movie description
3. Click "Analyze Genre"
4. **See posters** in the "Similar Movies" section!

## ❌ Not Working?

- Check `.env` file is in project root (same level as `app/` folder)
- Remove any extra spaces around API key
- Make sure you copied the **v3 API Key**, not v4 token
- Restart the application after adding the key

## 📖 Need More Help?

See detailed guide: `SETUP_MOVIE_POSTERS.md`
