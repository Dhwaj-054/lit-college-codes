"""
Script to remove API-related documentation files that are no longer needed.
Run this to clean up all the TMDB API documentation.
"""

import os

# Files to remove
files_to_remove = [
    '.env.example',
    'test_tmdb_api.py',
    'START_HERE.md',
    'QUICK_START_POSTERS.md',
    'SETUP_CHECKLIST.md',
    'SETUP_MOVIE_POSTERS.md',
    'TROUBLESHOOTING.md',
    'CHANGES_SUMMARY.md',
    'BEFORE_AFTER.md',
    'POSTER_DOCS_INDEX.md',
    'cleanup_api_files.py'  # Remove itself too
]

print("Cleaning up API-related files...")
print("-" * 50)

removed_count = 0
for file_name in files_to_remove:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            print(f"✓ Removed: {file_name}")
            removed_count += 1
        except Exception as e:
            print(f"✗ Error removing {file_name}: {e}")
    else:
        print(f"- Not found: {file_name}")

print("-" * 50)
print(f"\nRemoved {removed_count} files.")
print("\n✓ Cleanup complete!")
print("\nYour project now uses posters directly from the dataset.")
