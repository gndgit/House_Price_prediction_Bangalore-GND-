import pandas as pd
import pickle as pk
import streamlit as st

model = pk.load(open(r'C:\Users\user\Desktop\My Repo\gndgit clone demo\HOUSE PRICE PREDICTION BANGALORE\RidgeModel.pkl','rb'))
st.header("Welcome to GND World")
st.header("Banglore House Price Prediction")

data = pd.read_csv(r'C:\Users\user\Desktop\My Repo\gndgit clone demo\HOUSE PRICE PREDICTION BANGALORE\Cleaned_bangalore_data.csv')

loc = st.selectbox('Choose The Location:', data['location'].unique())
sqft = st.number_input("Enter Total Sq Ft:")
beds = st.number_input("Enter number of bedrooms:")
bath = st.number_input("Enter number of Bathrooms:")


input = pd.DataFrame([[loc,sqft,bath,beds]],columns=['location','total_sqft','bath','size_BHK'])

if st.button('Predict Price'):
    output = model.predict(input)
    out_str = 'Price of the House is '+ str(output[0]*100000)
    st.write(out_str)
    