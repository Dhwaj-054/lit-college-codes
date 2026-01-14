import pytest
from src.models.train import train_model
from src.models.predict import make_predictions
import pandas as pd

def test_train_model():
    # Load sample processed data
    data = pd.read_csv('data/processed/processed_data.csv')
    
    # Train the model
    model = train_model(data)
    
    # Check if the model is trained (not None)
    assert model is not None, "Model should be trained and not None"

def test_make_predictions():
    # Load sample processed data
    data = pd.read_csv('data/processed/processed_data.csv')
    
    # Train the model
    model = train_model(data)
    
    # Make predictions
    predictions = make_predictions(model, data)
    
    # Check if predictions are returned
    assert predictions is not None, "Predictions should not be None"
    assert len(predictions) == len(data), "Number of predictions should match number of input samples"