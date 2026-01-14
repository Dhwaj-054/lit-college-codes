import pandas as pd

def load_raw_data(file_path):
    """Load the raw dataset from the specified CSV file."""
    try:
        # Try different encodings
        encodings = ['utf-8', 'latin1', 'iso-8859-1', 'cp1252']
        for encoding in encodings:
            try:
                data = pd.read_csv(file_path, encoding=encoding)
                return data
            except UnicodeDecodeError:
                continue
        # If none of the encodings work, try with default encoding
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def load_processed_data(file_path):
    """Load the processed dataset from the specified CSV file."""
    return load_raw_data(file_path)