"""
Prediction script for the movie genre classification system.
Allows making predictions on new movie descriptions.
"""

import pickle
import sys
import os
import numpy as np
from utils.nlp_utils import download_nltk_data


def load_model_components():
    """
    Load all required model components.
    
    Returns:
        tuple: (classifier, extractor, preprocessor, mlb)
    """
    try:
        # Load classifier
        with open('models/best_model.pkl', 'rb') as f:
            classifier_data = pickle.load(f)
            classifier = classifier_data['best_model']
            mlb = classifier_data['mlb']
        
        # Load feature extractor
        with open('models/feature_extractor.pkl', 'rb') as f:
            extractor = pickle.load(f)
        
        # Load preprocessor
        with open('models/preprocessor.pkl', 'rb') as f:
            preprocessor = pickle.load(f)
            
        return classifier, extractor, preprocessor, mlb
    except FileNotFoundError as e:
        print(f"Model files not found. Please run 'python train.py' first to train the models.")
        print(f"Error: {e}")
        return None, None, None, None


def preprocess_text(text, preprocessor):
    """
    Preprocess text using the trained preprocessor.
    
    Args:
        text (str): Input text
        preprocessor: Trained preprocessor
        
    Returns:
        str: Preprocessed text
    """
    return preprocessor.preprocess(
        text, 
        tokenize=False,
        remove_stopwords=True,
        stem=False,
        lemmatize=True
    )


def predict_genre(description, classifier, extractor, preprocessor, mlb):
    """
    Predict genre for a movie description.
    
    Args:
        description (str): Movie description
        classifier: Trained classifier
        extractor: Trained feature extractor
        preprocessor: Trained preprocessor
        mlb: Multi-label binarizer
        
    Returns:
        list: Predicted genres
    """
    # Preprocess the description
    preprocessed_text = preprocess_text(description, preprocessor)
    
    # Extract features
    features = extractor.tfidf_vectorizer.transform([preprocessed_text])
    
    # Make prediction
    prediction = classifier.predict(features)
    
    # Get prediction probabilities if available
    try:
        probabilities = classifier.predict_proba(features)
        # For multi-output, we need to handle differently
        if hasattr(classifier, 'estimators_'):
            # MultiOutputClassifier
            prob_list = []
            for i, estimator in enumerate(classifier.estimators_):
                if hasattr(estimator, 'predict_proba'):
                    proba = estimator.predict_proba(features)
                    if proba.shape[1] == 2:
                        prob_list.append(proba[0][1])  # Probability of positive class
                    else:
                        prob_list.append(np.max(proba[0]))  # Max probability
                else:
                    prob_list.append(0.5)  # Default probability
        else:
            # Single estimator
            if hasattr(classifier, 'predict_proba'):
                proba = classifier.predict_proba(features)
                prob_list = proba[0] if proba.shape[0] > 0 else [0.5] * len(mlb.classes_)
            else:
                prob_list = [0.5] * len(mlb.classes_) if mlb else [0.5]
    except:
        prob_list = [0.5] * len(mlb.classes_) if mlb else [0.5]
    
    # Convert prediction to list of genres
    if len(prediction) > 0:
        # Handle different prediction formats
        if isinstance(prediction[0], (list, tuple, np.ndarray)):
            # Multi-label prediction
            if hasattr(prediction[0], '__len__') and len(prediction[0]) > 0:
                # Convert binary array to genre labels
                genres = mlb.inverse_transform(prediction)[0] if mlb else []
            else:
                genres = []
        else:
            # Single label prediction
            genres = [prediction[0]]
    else:
        genres = []
    
    return genres, prob_list


def main():
    """Main prediction function."""
    # Download required NLTK data
    download_nltk_data()
    
    # Load model components
    classifier, extractor, preprocessor, mlb = load_model_components()
    
    if classifier is None:
        return
    
    # Get input description
    if len(sys.argv) > 1:
        description = ' '.join(sys.argv[1:])
    else:
        description = input("Enter a movie description: ")
    
    if not description.strip():
        print("No description provided.")
        return
    
    # Make prediction
    genres, probabilities = predict_genre(description, classifier, extractor, preprocessor, mlb)
    
    # Display results
    print("\nPrediction Results:")
    print("-" * 20)
    print(f"Description: {description}")
    
    # Handle genres output
    if genres is not None and len(genres) > 0:
        # If genres is a tuple or list of arrays, flatten it
        if isinstance(genres[0], (list, tuple, np.ndarray)):
            flat_genres = []
            for item in genres:
                if isinstance(item, (list, tuple)):
                    flat_genres.extend(item)
                elif isinstance(item, np.ndarray):
                    flat_genres.extend(item.tolist())
                else:
                    flat_genres.append(item)
            genres = flat_genres
        print(f"Predicted Genres: {', '.join(map(str, genres)) if genres else 'None'}")
    else:
        print("Predicted Genres: None")
    
    if mlb and len(probabilities) == len(mlb.classes_):
        print("\nGenre Probabilities:")
        for genre, prob in zip(mlb.classes_, probabilities):
            print(f"  {genre}: {prob:.4f}")


if __name__ == "__main__":
    main()