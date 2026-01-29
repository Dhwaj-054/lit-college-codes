# Using Posters from IMDB Dataset

Your system is now configured to load movie posters directly from your `imdb_top_1000.csv` dataset!

## What Was Changed

### 1. Data Loading (`utils/data_loader.py`)
- Updated to load `imdb_top_1000.csv` instead of `movies_dataset.csv`
- Maps IMDB columns to expected format:
  - `Overview` → `description`
  - `Series_Title` → `title`
  - `Poster_Link` → `poster_url`
  - `IMDB_Rating` → `vote_average`

### 2. Recommender (`models/recommender.py`)
- Now includes `poster_url` from dataset in recommendations
- Includes IMDB ratings (`vote_average`)
- No external API calls needed

### 3. Web App (`app/app.py`)
- Removed TMDB API dependencies
- Loads `imdb_top_1000.csv` dataset
- Posters come directly from the dataset

### 4. Dependencies (`requirements.txt`)
- Removed `python-dotenv` (no longer needed)
- Removed `requests` (no longer needed for API calls)

## How It Works

```
User enters description
         ↓
System predicts genres
         ↓
Recommender finds similar movies from IMDB dataset
         ↓
Returns movies with:
  - Title (from Series_Title)
  - Description (from Overview)
  - Genre
  - Poster URL (from Poster_Link)
  - Rating (from IMDB_Rating)
         ↓
Frontend displays movie cards with posters
```

## Dataset Requirements

Your `data/imdb_top_1000.csv` should have these columns:
- **Series_Title** - Movie title
- **Overview** - Movie description/plot
- **Genre** - Movie genre(s)
- **Poster_Link** - URL to movie poster image
- **IMDB_Rating** - Movie rating (optional)

## Training the Model

Train your model with the IMDB dataset:

```bash
python train.py
```

This will:
1. Load `data/imdb_top_1000.csv`
2. Preprocess movie descriptions
3. Train genre classifier
4. Save models to `models/` directory

## Running the App

```bash
python app/app.py
```

The app will:
1. Load trained models
2. Load IMDB dataset with poster URLs
3. Start web server on http://localhost:5000

## Viewing Recommendations

1. Enter a movie description
2. Click "Analyze Genre"
3. Scroll to "Similar Movies"
4. See recommendations with:
   - Movie posters (from Poster_Link column)
   - Movie titles
   - IMDB ratings
   - Similarity scores

## Cleanup Old API Files

To remove all the TMDB API documentation files:

```bash
python cleanup_api_files.py
```

This will remove:
- `.env.example`
- `test_tmdb_api.py`
- All API setup guide files
- Cleanup script itself

## No API Key Needed! ✨

- ✅ No external API required
- ✅ No API keys to manage
- ✅ No rate limits
- ✅ Works offline (after initial poster URL loading)
- ✅ Faster (no API calls)
- ✅ Simpler setup

## Poster URL Format

The `Poster_Link` column in your CSV should contain direct image URLs like:
```
https://m.media-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX67_CR0,0,67,98_AL_.jpg
```

These URLs are loaded from the dataset and passed directly to the frontend for display.

## Benefits

1. **Simpler** - No API configuration
2. **Faster** - No external API calls
3. **Reliable** - No network dependencies
4. **Consistent** - Always shows the same posters
5. **Offline** - Works without internet (after data loading)

## Next Steps

1. **Train the model:**
   ```bash
   python train.py
   ```

2. **Run the app:**
   ```bash
   python app/app.py
   ```

3. **Test recommendations:**
   - Open http://localhost:5000
   - Enter a movie description
   - See recommendations with posters!

4. **(Optional) Cleanup API files:**
   ```bash
   python cleanup_api_files.py
   ```

---

**Your movie recommendation system now uses posters directly from the IMDB dataset - no API needed!** 🎬✨
