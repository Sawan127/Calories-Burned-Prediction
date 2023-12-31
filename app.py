import streamlit as st
import pickle
import pandas as pd
import numpy as np

model = pickle.load(open('model.pkl','rb'))

st.write("Calories Burned Calculator App")

gender = st.selectbox("Select Gender", ("Male", "Female"))

if (gender == "Male"):
	g = 0
else:
	g = 1

age = st.number_input(" Enter age: ")

height = st.number_input("Enter Height (in cm): ")

weight = st.number_input("Enter Weight (in Kg): ")

duration = st.number_input("Enter the workout duration (in Minutes): ")

heartrate = st.number_input(" Enter the Heart rate(50-120): ")

bodytemp = st.number_input(" Enter the Body Temperature(in celcius): ")

prediction = model.predict(pd.DataFrame(columns = ['Gender', 'Age', 'Height','Weight','Duration','Heart_Rate', 'Body_Temp'], 
					data = np.array([g, age, height, weight, duration, heartrate, bodytemp]).reshape(1,7)))

if st.button('Predict'):
	st.write("Calories burned")
	st.success(prediction) 
	 
	 						   
						   

