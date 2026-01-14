import streamlit as st
import pandas as pd
import os
import sys

# Add the project root directory to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.append(project_root)

from src.data.load_data import load_processed_data
from src.data.preprocess import preprocess_data

# Set page config
st.set_page_config(
    page_title="Car Recommendation System",
    page_icon="🚗",
    layout="wide"
)

# Custom CSS to improve the look and ensure visibility in dark mode
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stSelectbox {
        margin-bottom: 1rem;
    }
    .car-details {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    .car-details h3, .car-details h4 {
        color: #4CAF50 !important;
        margin-bottom: 1rem !important;
    }
    .car-details p, .car-details ul {
        color: var(--text-color, #ffffff) !important;
        margin-bottom: 0.5rem !important;
    }
    .car-details ul {
        list-style-type: none !important;
        padding-left: 0 !important;
    }
    .car-details li {
        margin-bottom: 0.3rem !important;
    }
    .car-details strong {
        color: #64B5F6 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Set the title of the app
st.title("🚗 Car Recommendation System")
st.write("Find your perfect car in just a few clicks!")

try:
    # Load and preprocess the data
    data_path = os.path.join(project_root, "data", "raw", "cardekho_dataset.csv")
    data = load_processed_data(data_path)
    
    if data is None:
        st.error("Error: Could not load the dataset. Please check if the data file exists.")
    else:
        processed_data = preprocess_data(data)
        
        # Step 1: Select Brand
        st.subheader("Step 1: Choose a Car Brand")
        brands = sorted(data['brand'].unique())
        selected_brand = st.selectbox("Select Brand", brands)
        
        # Filter data by selected brand
        brand_data = data[data['brand'] == selected_brand]
        
        # Step 2: Select Model
        st.subheader("Step 2: Choose a Model")
        models = sorted(brand_data['model'].unique())
        selected_model = st.selectbox("Select Model", models)
        
        # Create columns for filters and results
        filter_col, results_col = st.columns([1, 2])
        
        with filter_col:
            st.subheader("Step 3: Set Your Preferences")
            
            # Price Range
            price_range = brand_data['selling_price'].agg(['min', 'max']).astype(int)
            price_min, price_max = st.slider(
                "Price Range (₹)",
                min_value=int(price_range['min']),
                max_value=int(price_range['max']),
                value=(int(price_range['min']), int(price_range['max'])),
                step=50000
            )
            
            # Age Range
            max_age = int(brand_data['vehicle_age'].max())
            age_limit = st.slider(
                "Maximum Vehicle Age (Years)",
                min_value=0,
                max_value=max_age,
                value=max_age
            )
            
            # Fuel Type
            fuel_types = sorted(brand_data['fuel_type'].unique())
            selected_fuel = st.multiselect("Fuel Type", fuel_types, default=fuel_types)
            
            # Transmission
            transmission_types = sorted(brand_data['transmission_type'].unique())
            selected_transmission = st.multiselect("Transmission", transmission_types, default=transmission_types)
        
        with results_col:
            # Filter the data based on all selections
            filtered_data = brand_data[
                (brand_data['model'] == selected_model) &
                (brand_data['selling_price'].between(price_min, price_max)) &
                (brand_data['vehicle_age'] <= age_limit) &
                (brand_data['fuel_type'].isin(selected_fuel)) &
                (brand_data['transmission_type'].isin(selected_transmission))
            ]

            if len(filtered_data) == 0:
                st.warning("No cars found matching your criteria. Please adjust the filters.")
            else:
                st.subheader("Available Cars")
                
                # Display cars that match the criteria
                for idx, car in filtered_data.iterrows():
                    st.markdown(f"""
                    <div class='car-details'>
                        <h3>🚗 {car['brand']} {car['model']}</h3>
                        <p><strong>💰 Price:</strong> ₹{car['selling_price']:,}</p>
                        <p><strong>📊 Specifications:</strong></p>
                        <ul>
                            <li><strong>🕐 Age:</strong> {car['vehicle_age']} years</li>
                            <li><strong>⛽ Fuel:</strong> {car['fuel_type']}</li>
                            <li><strong>🔄 Transmission:</strong> {car['transmission_type']}</li>
                            <li><strong>⚡ Mileage:</strong> {car['mileage']} kmpl</li>
                            <li><strong>🚦 Engine:</strong> {car['engine']} cc</li>
                            <li><strong>💪 Power:</strong> {car['max_power']} bhp</li>
                            <li><strong>👥 Seats:</strong> {car['seats']}</li>
                        </ul>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Show similar cars button
                    if st.button(f"Show Similar Cars", key=f"btn_{idx}"):
                        st.write("#### Similar Cars You Might Like:")
                        
                        # Create a similarity score based on multiple features
                        similar_cars = data[
                            (data.index != idx) & 
                            (data['brand'] != selected_brand)  # Exclude same brand
                        ].copy()
                        
                        # Calculate similarity score
                        similar_cars['similarity_score'] = (
                            (similar_cars['selling_price'] - car['selling_price']).abs() / data['selling_price'].std() * 0.4 +
                            (similar_cars['mileage'] - car['mileage']).abs() / data['mileage'].std() * 0.2 +
                            (similar_cars['engine'] - car['engine']).abs() / data['engine'].std() * 0.2 +
                            (similar_cars['vehicle_age'] - car['vehicle_age']).abs() / data['vehicle_age'].std() * 0.2
                        )
                        
                        # Get top 5 similar cars from different brands
                        similar_cars = similar_cars.nsmallest(5, 'similarity_score')
                        
                        # Display similar cars in a nice format
                        for _, rec_car in similar_cars.iterrows():
                            st.markdown(f"""
                            <div class='car-details' style='margin-left: 2rem;'>
                                <h4>🚗 {rec_car['brand']} {rec_car['model']}</h4>
                                <p><strong>💰 Price:</strong> ₹{rec_car['selling_price']:,}</p>
                                <ul>
                                    <li><strong>🕐 Age:</strong> {rec_car['vehicle_age']} years</li>
                                    <li><strong>⚡ Mileage:</strong> {rec_car['mileage']} kmpl</li>
                                    <li><strong>🚦 Engine:</strong> {rec_car['engine']} cc</li>
                                    <li><strong>⛽ Fuel:</strong> {rec_car['fuel_type']}</li>
                                </ul>
                            </div>
                            """, unsafe_allow_html=True)

except Exception as e:
    st.error(f"An error occurred: {str(e)}")
    st.write("Please ensure the dataset exists and has the required columns.")
