import pandas as pd

def create_features(df):
    # Example feature engineering: creating a 'rating' feature based on existing columns
    df['rating'] = df['likes'] / (df['likes'] + df['dislikes'] + 1)  # Avoid division by zero
    df['engagement'] = df['likes'] + df['comments'] + df['shares']  # Total engagement metric

    # Additional feature engineering can be added here
    return df

def load_and_process_data(file_path):
    # Load the dataset
    df = pd.read_csv(file_path)
    
    # Perform feature engineering
    df = create_features(df)
    
    return df

# Example usage
if __name__ == "__main__":
    processed_data = load_and_process_data('../data/processed/processed_data.csv')
    print(processed_data.head())