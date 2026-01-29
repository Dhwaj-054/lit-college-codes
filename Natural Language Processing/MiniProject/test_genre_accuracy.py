"""
Quick test script to verify genre classification accuracy after improvements.
Run this after training to see if the model correctly identifies genres.
"""

import pickle
from models.preprocessor import TextPreprocessor
from models.feature_extractor import FeatureExtractor

print("="*70)
print("Genre Classification Accuracy Test")
print("="*70)

# Test cases with obvious genre indicators
test_cases = [
    {
        "description": "Intense action movie with explosions, car chases, and epic fight scenes",
        "expected": "Action"
    },
    {
        "description": "Terrifying horror film about a haunted house filled with ghosts and monsters",
        "expected": "Horror"
    },
    {
        "description": "Hilarious comedy with funny jokes and laugh-out-loud humor throughout",
        "expected": "Comedy"
    },
    {
        "description": "Space exploration mission encounters alien life forms on a distant planet",
        "expected": "Sci-Fi"
    },
    {
        "description": "Romantic love story between two people who fall in love despite obstacles",
        "expected": "Romance"
    },
    {
        "description": "Suspenseful thriller with mystery and detective investigating serial crimes",
        "expected": "Thriller"
    },
    {
        "description": "Emotional drama about family dealing with serious personal challenges",
        "expected": "Drama"
    }
]

try:
    # Load trained models
    print("\n1. Loading trained models...")
    
    with open('models/best_model.pkl', 'rb') as f:
        model_data = pickle.load(f)
        classifier = model_data['best_model']
        mlb = model_data['mlb']
    
    with open('models/feature_extractor.pkl', 'rb') as f:
        extractor = pickle.load(f)
    
    with open('models/preprocessor.pkl', 'rb') as f:
        preprocessor = pickle.load(f)
    
    print("✓ Models loaded successfully")
    
    # Test each case
    print("\n2. Testing genre classification...")
    print("="*70)
    
    correct = 0
    total = len(test_cases)
    
    for i, test in enumerate(test_cases, 1):
        description = test['description']
        expected = test['expected']
        
        # Preprocess
        preprocessed = preprocessor.preprocess(
            description,
            tokenize=False,
            remove_stopwords=True,
            stem=False,
            lemmatize=True
        )
        
        # Extract features
        features = extractor.tfidf_vectorizer.transform([preprocessed])
        
        # Predict
        prediction = classifier.predict(features)
        predicted_genres = mlb.inverse_transform(prediction)[0]
        
        # Check if expected genre is in predictions
        is_correct = expected in predicted_genres or expected.lower() in [g.lower() for g in predicted_genres]
        
        if is_correct:
            correct += 1
            status = "✓ PASS"
            color_start = ""
            color_end = ""
        else:
            status = "✗ FAIL"
            color_start = ""
            color_end = ""
        
        print(f"\nTest {i}: {status}")
        print(f"  Description: {description[:60]}...")
        print(f"  Expected: {expected}")
        print(f"  Predicted: {', '.join(predicted_genres) if predicted_genres else 'None'}")
        print(f"  Preprocessed: {preprocessed[:50]}...")
    
    # Summary
    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)
    accuracy = (correct / total) * 100
    print(f"Correct: {correct}/{total}")
    print(f"Accuracy: {accuracy:.1f}%")
    
    if accuracy >= 85:
        print("\n✅ EXCELLENT! Model is working great.")
    elif accuracy >= 70:
        print("\n✓ GOOD! Model is working well.")
    elif accuracy >= 50:
        print("\n⚠ OK! Model needs improvement.")
    else:
        print("\n✗ POOR! Model needs retraining with improvements.")
    
    print("\n" + "="*70)
    
    # Check if genre keywords are preserved
    print("\n3. Checking if genre keywords are preserved...")
    test_text = "action fight horror scary comedy funny"
    preprocessed_test = preprocessor.preprocess(
        test_text,
        tokenize=True,
        remove_stopwords=True,
        stem=False,
        lemmatize=False
    )
    
    keywords_preserved = [word for word in ['action', 'fight', 'horror', 'scary', 'comedy', 'funny'] 
                         if word in preprocessed_test]
    
    print(f"  Input: {test_text}")
    print(f"  After preprocessing: {' '.join(preprocessed_test)}")
    print(f"  Keywords preserved: {len(keywords_preserved)}/6")
    
    if len(keywords_preserved) >= 5:
        print("  ✅ Genre keywords are properly preserved!")
    else:
        print("  ⚠ Warning: Some genre keywords were removed by preprocessing")
        print("  This might affect accuracy. Check preprocessor.py")
    
except FileNotFoundError as e:
    print(f"\n✗ Error: Model files not found!")
    print(f"  {e}")
    print("\nPlease train the model first:")
    print("  python train.py")
except Exception as e:
    print(f"\n✗ Error: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "="*70)
print("Test complete!")
print("="*70)
