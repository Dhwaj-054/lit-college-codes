# Configuration settings for the recommendation system application

import os

# Base directory of the project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Data paths
RAW_DATA_PATH = os.path.join(BASE_DIR, 'data', 'raw', 'dataset.csv')
PROCESSED_DATA_PATH = os.path.join(BASE_DIR, 'data', 'processed', 'processed_data.csv')

# Model path
MODEL_PATH = os.path.join(BASE_DIR, 'models', 'best_model.pkl')

# Streamlit configuration
STREAMLIT_PORT = 8501
STREAMLIT_TITLE = "Recommendation System"

# Other configurations can be added as needed
