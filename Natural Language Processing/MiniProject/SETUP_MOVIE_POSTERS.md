# Setting Up Movie Posters Feature

This guide will help you enable movie poster display in your recommendations.

## Why You Need This

The movie recommendation system shows similar movies based on your input. To make the experience more visual and engaging, the system can display movie posters from The Movie Database (TMDB). However, this requires a free API key.

## Step-by-Step Setup

### 1. Create a TMDB Account

1. Go to [The Movie Database (TMDB)](https://www.themoviedb.org/)
2. Click **"Join TMDB"** in the top-right corner
3. Fill out the registration form
4. Verify your email address

### 2. Request an API Key

1. Once logged in, click on your **profile icon** in the top-right
2. Select **"Settings"**
3. In the left sidebar, click **"API"**
4. Click **"Create"** under "Request an API Key"
5. Choose **"Developer"** (this is free)
6. Accept the terms and conditions
7. Fill out the form:
   - **Application Name:** Your project name (e.g., "Movie Genre Classifier")
   - **Application URL:** You can use `http://localhost:5000` for local development
   - **Application Summary:** Brief description (e.g., "Movie recommendation system")
8. Submit the form

### 3. Copy Your API Key

1. After approval (usually instant), you'll see your **API Key** and **API Read Access Token**
2. Copy the **API Key (v3 auth)** - it looks like a long string of letters and numbers

### 4. Configure Your Project

#### Option A: Using .env File (Recommended)

1. In your project root directory, copy the example file:
   ```bash
   cp .env.example .env
   ```

2. Open the `.env` file in a text editor

3. Replace `your_api_key_here` with your actual API key:
   ```
   TMDB_API_KEY=abc123def456your_actual_key_here
   ```

4. Save the file

#### Option B: Using Environment Variable (Alternative)

You can also set it as a system environment variable:

**Windows (PowerShell):**
```powershell
$env:TMDB_API_KEY="your_actual_api_key_here"
```

**Windows (Command Prompt):**
```cmd
set TMDB_API_KEY=your_actual_api_key_here
```

**Linux/Mac:**
```bash
export TMDB_API_KEY="your_actual_api_key_here"
```

### 5. Install Required Dependencies

Make sure you have all dependencies installed:

```bash
pip install -r requirements.txt
```

This will install `python-dotenv` which loads the API key from your `.env` file.

### 6. Restart the Application

If the application is already running, restart it:

```bash
python app/app.py
```

## Verification

To verify the setup is working:

1. Open your browser to `http://localhost:5000`
2. Enter a movie description
3. Click **"Analyze Genre"**
4. Scroll down to the **"Similar Movies"** section
5. You should now see movie posters displayed for each recommendation

## Troubleshooting

### Posters Not Showing

**Problem:** You see placeholder images instead of actual posters

**Solutions:**
- Verify your API key is correct in the `.env` file
- Make sure there are no extra spaces around the API key
- Restart the Flask application after adding the key
- Check the console/terminal for any error messages

### "No TMDB API key provided" Warning

**Problem:** You see a warning in the console

**Solution:** Follow steps 4-5 above to configure your API key

### API Key Not Working

**Problem:** API key seems configured but still not working

**Solutions:**
- Verify the API key is the **v3 API Key**, not the v4 Read Access Token
- Make sure the `.env` file is in the project root directory (same level as `app/` folder)
- Check that `python-dotenv` is installed: `pip list | grep dotenv`
- Try restarting your terminal/command prompt

### Rate Limiting

**Problem:** Some posters load, but others show placeholders

**Solution:** TMDB has a rate limit. The application handles this gracefully by showing a placeholder when the limit is reached. Wait a few seconds and try again.

## Without API Key

The system will work without an API key, but:
- ❌ No movie posters will be displayed
- ❌ Recommendations will show placeholder images
- ✅ Movie recommendations will still work
- ✅ Genre classification will work normally

## Security Notes

- **Never commit your `.env` file** to version control (it's already in `.gitignore`)
- **Never share your API key** publicly
- **Keep your API key secure** - treat it like a password
- The free tier allows 40,000+ requests per day, which is more than enough for personal projects

## Additional Resources

- [TMDB API Documentation](https://developers.themoviedb.org/3)
- [TMDB API Support Forum](https://www.themoviedb.org/talk/category/5047958519c29526b50017d6)
- [API Usage Policy](https://www.themoviedb.org/documentation/api/terms-of-use)

## Need Help?

If you're still having issues:
1. Check the console output for error messages
2. Verify all setup steps were completed
3. Try using the example API key test: [TMDB API Test](https://api.themoviedb.org/3/movie/550?api_key=YOUR_KEY)
