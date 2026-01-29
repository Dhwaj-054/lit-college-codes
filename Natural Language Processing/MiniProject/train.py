"""
Training pipeline for the movie genre classification system.
Trains multiple models and saves the best performing one.
"""

import pandas as pd
import numpy as np
import pickle
import os
from utils.data_loader import load_movie_data, save_preprocessed_data, split_data
from utils.nlp_utils import download_nltk_data
from models.preprocessor import TextPreprocessor
from models.feature_extractor import FeatureExtractor
from models.classifier import MovieGenreClassifier
from models.evaluator import ModelEvaluator, evaluate_model_performance, compare_model_results


def main():
    """Main training pipeline."""
    print("Starting movie genre classification training pipeline...")
    
    # Download required NLTK data
    print("Downloading NLTK data...")
    download_nltk_data()
    
    # Load data
    print("Loading movie data...")
    df = load_movie_data()
    print(f"Loaded {len(df)} movie samples")
    
    # Preprocess text
    print("Preprocessing text data...")
    # Only remove very generic movie words, keep genre-important terms
    preprocessor = TextPreprocessor(
        custom_stopwords={'film', 'movie'}  # Reduced to keep more context
    )
    
    # Apply preprocessing
    df_processed = preprocessor.preprocess_dataframe(
        df, 
        'description',
        tokenize=False,  # We'll tokenize in the vectorizer
        remove_stopwords=True,
        stem=False,  # We'll compare stemming vs lemmatization separately
        lemmatize=True
    )
    
    # Extract features
    print("Extracting features...")
    extractor = FeatureExtractor()
    
    # Use preprocessed text for feature extraction
    texts = df_processed['description_preprocessed'].tolist()
    labels = df['genre'].tolist()
    
    # Extract TF-IDF features
    tfidf_features = extractor.extract_tfidf_features(texts, fit=True)
    
    # Initialize classifier
    print("Training models...")
    classifier = MovieGenreClassifier()
    
    # Prepare labels for multi-label classification
    y = classifier.prepare_labels(labels)
    
    # Compare models
    results = classifier.compare_models(tfidf_features, y, cv=3)
    
    # Print results
    print("\nModel Performance Comparison:")
    print("-" * 50)
    for model_name, metrics in results.items():
        print(f"{model_name}:")
        print(f"  Accuracy: {metrics['accuracy']:.4f} (+/- {metrics['accuracy_std']*2:.4f})")
        print()
    
    # Get the best model
    best_model_name = max(results, key=lambda x: results[x]['accuracy'])
    print(f"Best model: {best_model_name} with accuracy: {results[best_model_name]['accuracy']:.4f}")
    
    # Save the best model
    print("Saving the best model...")
    model_save_path = 'models/best_model.pkl'
    classifier.save_model(model_save_path)
    print(f"Model saved to {model_save_path}")
    
    # Save feature extractor
    with open('models/feature_extractor.pkl', 'wb') as f:
        pickle.dump(extractor, f)
    print("Feature extractor saved to models/feature_extractor.pkl")
    
    # Save preprocessor
    with open('models/preprocessor.pkl', 'wb') as f:
        pickle.dump(preprocessor, f)
    print("Preprocessor saved to models/preprocessor.pkl")
    
    # Save processed data
    processed_data = {
        'texts': texts,
        'labels': labels,
        'tfidf_features': tfidf_features,
        'multi_label_binarizer': classifier.mlb
    }
    save_preprocessed_data(processed_data)
    print("Processed data saved to data/preprocessed_data.pkl")
    
    # Evaluate best model in detail
    print("\nDetailed evaluation of best model...")
    X_train, X_test, y_train, y_test = split_data(tfidf_features, y, test_size=0.2, random_state=42)
    
    # Train best model on full training set
    best_model = classifier.train_model(X_train, y_train, best_model_name)
    
    # Make predictions on test set
    y_pred = best_model.predict(X_test)
    
    # Convert back to genre labels for evaluation
    y_test_labels = classifier.mlb.inverse_transform(y_test)
    y_pred_labels = classifier.mlb.inverse_transform(y_pred)
    
    # Evaluate performance
    evaluation_results = evaluate_model_performance(y_test_labels, y_pred_labels)
    
    print("\nDetailed Performance Metrics:")
    print("-" * 40)
    print(f"Overall Accuracy: {evaluation_results['overall']['accuracy']:.4f}")
    print(f"Precision: {evaluation_results['overall']['precision']:.4f}")
    print(f"Recall: {evaluation_results['overall']['recall']:.4f}")
    print(f"F1-Score: {evaluation_results['overall']['f1_score']:.4f}")
    
    print("\nPer-Class Performance:")
    print("-" * 30)
    for class_name, metrics in evaluation_results['per_class'].items():
        print(f"{class_name}:")
        print(f"  Precision: {metrics['precision']:.4f}")
        print(f"  Recall: {metrics['recall']:.4f}")
        print(f"  F1-Score: {metrics['f1_score']:.4f}")
    
    print("\nTraining pipeline completed successfully!")


if __name__ == "__main__":
    main()