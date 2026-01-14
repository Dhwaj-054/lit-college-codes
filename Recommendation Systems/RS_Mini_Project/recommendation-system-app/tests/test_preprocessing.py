import pytest
import pandas as pd
from src.data.preprocess import preprocess_data

def test_preprocess_data():
    # Load the raw dataset
    raw_data = pd.read_csv('data/raw/dataset.csv')
    
    # Preprocess the data
    processed_data = preprocess_data(raw_data)
    
    # Check if the processed data is a DataFrame
    assert isinstance(processed_data, pd.DataFrame), "Processed data should be a DataFrame"
    
    # Check for missing values in the processed data
    assert processed_data.isnull().sum().sum() == 0, "Processed data should not contain missing values"
    
    # Check if the expected columns are present in the processed data
    expected_columns = ['column1', 'column2', 'column3']  # Replace with actual column names
    for column in expected_columns:
        assert column in processed_data.columns, f"{column} should be in the processed data"
    
    # Check if the shape of the processed data is as expected
    assert processed_data.shape[0] > 0, "Processed data should have rows"
    assert processed_data.shape[1] == len(expected_columns), "Processed data should have the correct number of columns"