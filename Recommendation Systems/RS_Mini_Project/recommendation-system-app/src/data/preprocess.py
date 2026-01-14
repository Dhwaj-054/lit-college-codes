import pandas as pd

def load_data(file_path):
    """Load the dataset from the specified file path."""
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
    """Preprocess the car data by cleaning and transforming it."""
    if data is None:
        return None
        
    # 1. Handle missing values
    data = data.dropna()
    
    # 2. Remove the index column if it exists
    if '' in data.columns:
        data = data.drop('', axis=1)
    
    # 3. Convert numeric columns to appropriate types
    numeric_columns = ['vehicle_age', 'km_driven', 'mileage', 'engine', 'max_power', 'seats', 'selling_price']
    for col in numeric_columns:
        if col in data.columns:
            data[col] = pd.to_numeric(data[col], errors='coerce')
    
    # 4. Drop rows with invalid numeric values
    data = data.dropna()
    
    # 5. Sort by price (optional)
    if 'selling_price' in data.columns:
        data = data.sort_values('selling_price', ascending=True)
    
    return data
    
    return data

def save_processed_data(data, output_path):
    """Save the processed data to a specified output path."""
    data.to_csv(output_path, index=False)

# Example usage
if __name__ == "__main__":
    raw_data_path = '../data/raw/dataset.csv'
    processed_data_path = '../data/processed/processed_data.csv'
    
    raw_data = load_data(raw_data_path)
    processed_data = preprocess_data(raw_data)
    save_processed_data(processed_data, processed_data_path)