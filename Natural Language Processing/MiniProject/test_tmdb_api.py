"""
Test script to verify TMDB API key is working correctly.
Run this to check your API configuration before starting the main application.
"""

import os
from dotenv import load_dotenv
import requests

def test_tmdb_api():
    """Test TMDB API key configuration."""
    print("\n" + "="*60)
    print("TMDB API Configuration Test")
    print("="*60 + "\n")
    
    # Load environment variables
    load_dotenv()
    
    # Check if API key exists
    api_key = os.getenv('TMDB_API_KEY')
    
    if not api_key:
        print("❌ FAILED: TMDB_API_KEY not found in environment variables")
        print("\nTo fix this:")
        print("1. Create a .env file in the project root")
        print("2. Add: TMDB_API_KEY=your_actual_api_key")
        print("3. See QUICK_START_POSTERS.md for detailed instructions")
        return False
    
    print(f"✓ API key found: {api_key[:8]}...{api_key[-4:]}")
    print(f"  (Length: {len(api_key)} characters)\n")
    
    # Test API connection
    print("Testing API connection...")
    test_url = f"https://api.themoviedb.org/3/configuration"
    
    try:
        response = requests.get(
            test_url,
            params={'api_key': api_key},
            timeout=10
        )
        
        if response.status_code == 200:
            print("✓ API connection successful!")
            data = response.json()
            
            # Test movie search
            print("\nTesting movie search...")
            search_url = "https://api.themoviedb.org/3/search/movie"
            search_response = requests.get(
                search_url,
                params={
                    'api_key': api_key,
                    'query': 'Inception'
                },
                timeout=10
            )
            
            if search_response.status_code == 200:
                search_data = search_response.json()
                results = search_data.get('results', [])
                
                if results:
                    print(f"✓ Movie search successful! Found {len(results)} results")
                    print(f"\nSample movie: {results[0]['title']}")
                    if results[0].get('poster_path'):
                        poster_url = f"https://image.tmdb.org/t/p/w500{results[0]['poster_path']}"
                        print(f"Poster URL: {poster_url}")
                    print("\n" + "="*60)
                    print("✅ ALL TESTS PASSED!")
                    print("="*60)
                    print("\nYour TMDB API key is configured correctly.")
                    print("Movie posters will be displayed in your application.")
                    return True
                else:
                    print("⚠ Warning: API works but no results found")
                    return False
            else:
                print(f"❌ Movie search failed: {search_response.status_code}")
                print(f"Response: {search_response.text[:200]}")
                return False
                
        elif response.status_code == 401:
            print("❌ FAILED: Invalid API key")
            print("\nThe API key is invalid or has been revoked.")
            print("Please check your API key at: https://www.themoviedb.org/settings/api")
            return False
            
        elif response.status_code == 403:
            print("❌ FAILED: Access forbidden")
            print("\nYour API key may not have the required permissions.")
            return False
            
        else:
            print(f"❌ FAILED: Unexpected status code {response.status_code}")
            print(f"Response: {response.text[:200]}")
            return False
            
    except requests.exceptions.Timeout:
        print("❌ FAILED: Connection timeout")
        print("Check your internet connection and try again.")
        return False
        
    except requests.exceptions.ConnectionError:
        print("❌ FAILED: Cannot connect to TMDB API")
        print("Check your internet connection.")
        return False
        
    except Exception as e:
        print(f"❌ FAILED: Unexpected error: {str(e)}")
        return False

if __name__ == "__main__":
    try:
        success = test_tmdb_api()
        exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\nTest cancelled by user.")
        exit(1)
