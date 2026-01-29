"""
Test script to verify IMDB dataset loads correctly.
Run this before train.py to check data format.
"""

import pandas as pd
from utils.data_loader import load_movie_data

print("="*60)
print("Testing IMDB Dataset Loading")
print("="*60)

try:
    # Load data
    print("\n1. Loading data from imdb_top_1000.csv...")
    df = load_movie_data('data/imdb_top_1000.csv')
    
    print(f"✓ Loaded {len(df)} movies")
    
    # Check columns
    print("\n2. Checking required columns...")
    required_columns = ['title', 'description', 'genre']
    optional_columns = ['poster_url', 'IMDB_Rating']
    
    for col in required_columns:
        if col in df.columns:
            non_null = df[col].notna().sum()
            print(f"   ✓ {col}: {non_null}/{len(df)} non-null values")
        else:
            print(f"   ✗ {col}: MISSING")
    
    for col in optional_columns:
        if col in df.columns:
            non_null = df[col].notna().sum()
            print(f"   • {col}: {non_null}/{len(df)} non-null values (optional)")
    
    # Show sample data
    print("\n3. Sample movies:")
    print("-" * 60)
    for idx in range(min(3, len(df))):
        row = df.iloc[idx]
        print(f"\nMovie {idx+1}:")
        print(f"  Title: {row.get('title', 'N/A')}")
        print(f"  Genre: {row.get('genre', 'N/A')}")
        print(f"  Description: {str(row.get('description', 'N/A'))[:80]}...")
        if 'poster_url' in df.columns:
            poster = row.get('poster_url', 'N/A')
            print(f"  Poster: {poster if pd.notna(poster) else 'None'}")
        if 'IMDB_Rating' in df.columns:
            rating = row.get('IMDB_Rating', 'N/A')
            print(f"  Rating: {rating if pd.notna(rating) else 'None'}")
    
    # Check for issues
    print("\n" + "="*60)
    print("Data Validation:")
    print("="*60)
    
    issues = []
    
    # Check required columns exist
    for col in required_columns:
        if col not in df.columns:
            issues.append(f"Missing required column: {col}")
    
    # Check for null values in required columns
    for col in required_columns:
        if col in df.columns:
            null_count = df[col].isna().sum()
            if null_count > 0:
                issues.append(f"{null_count} null values in '{col}' column")
    
    # Check description length
    if 'description' in df.columns:
        short_desc = df[df['description'].str.len() < 10]
        if len(short_desc) > 0:
            issues.append(f"{len(short_desc)} movies with very short descriptions")
    
    if issues:
        print("\n⚠ Issues found:")
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("\n✅ All checks passed! Data is ready for training.")
    
    print("\n" + "="*60)
    print("Summary:")
    print("="*60)
    print(f"Total movies: {len(df)}")
    print(f"Has descriptions: {df['description'].notna().sum() if 'description' in df.columns else 0}")
    print(f"Has genres: {df['genre'].notna().sum() if 'genre' in df.columns else 0}")
    print(f"Has posters: {df['poster_url'].notna().sum() if 'poster_url' in df.columns else 0}")
    
    if not issues:
        print("\n✓ Ready to run: python train.py")
    else:
        print("\n⚠ Fix issues above before training")
    
except FileNotFoundError:
    print("\n✗ Error: data/imdb_top_1000.csv not found!")
    print("\nPlease ensure the file exists in the data/ directory.")
except Exception as e:
    print(f"\n✗ Error loading data: {e}")
    import traceback
    traceback.print_exc()
