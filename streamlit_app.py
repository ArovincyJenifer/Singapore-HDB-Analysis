import joblib
import streamlit as st
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder


# Load the compressed model
model = joblib.load('modellinear.pkl')


# Design the Streamlit app
st.title('Resale Price Prediction')

# #towns = ['ANG MO KIO', 'BEDOK', 'BISHAN', 'BUKIT BATOK', 'BUKIT MERAH',
#        'BUKIT PANJANG', 'BUKIT TIMAH', 'CENTRAL AREA', 'CHOA CHU KANG',
#        'CLEMENTI', 'GEYLANG', 'HOUGANG', 'JURONG EAST', 'JURONG WEST',
#        'KALLANG/WHAMPOA', 'MARINE PARADE', 'PASIR RIS', 'QUEENSTOWN',
#        'SENGKANG', 'SERANGOON', 'TAMPINES', 'TOA PAYOH', 'WOODLANDS',
#        'YISHUN', 'SEMBAWANG', 'PUNGGOL', 'LIM CHU KANG']



# Sidebar for user input
st.sidebar.title('Input Features')

month_input = st.sidebar.text_input('Enter the month (YYYY-MM):', '2024-06')


# town = st.sidebar.selectbox('Select Town',towns)
# # Initialize LabelEncoder
# label_encoder = LabelEncoder()

# label_encoder.fit(towns)
# encoded_town = label_encoder.transform([town])[0]

# Convert month to ordinal value
try:
    month = pd.to_datetime(month_input, format='%Y-%m').toordinal()
except ValueError:
    st.sidebar.error("Invalid date format. Please enter the date in YYYY-MM format.")
    st.stop()

# Text input for number of rooms
No_of_rooms = st.sidebar.number_input('Enter the number of rooms:', min_value=1, max_value=7, value=3)

# Text input for storey
storey = st.sidebar.number_input('Enter the storey:', min_value=1, max_value=51, value=9)

floor_area_sqm = st.sidebar.number_input('Enter the floor area in square meters:', min_value=28.0, max_value=307.0, value=69.0)

# Text input for lease commencement date
lease_commence_date = st.sidebar.number_input('Enter the lease commencement year:', min_value=2017, max_value=2024)


if st.button('Predict'):

    input_data = pd.DataFrame(
        {
            'month' :[month],
             'No_of_Rooms' : [No_of_rooms],
            'storey':[storey],
            'floor_area_sqm':[floor_area_sqm],
            'lease_commence_date' :[lease_commence_date]
            #'town_encoded':[encoded_town]

        }
    )

    prediction = model.predict(input_data)
    st.write('### Predicted Resale Prices in SGD:')
    st.write(prediction[0])

    


