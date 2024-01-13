import streamlit as st
import numpy as np
import pandas as pd
import pickle
from PIL import Image
import sklearn




model = pickle.load(open('singapore.pkl', 'rb'))

st.title('Singapore resale flat price Prediction')




def user_report():
    region = st.text_input('region')
    number_of_rooms = st.text_input('number_of_rooms')
    storey = st.text_input('storey')
    floor_area_sqm = st.text_input('floor_area_sqm')
    remaining_lease = st.text_input('remaining_lease')
    
    
    


    user_report_data = {
        'region':region,
        'number_of_rooms':number_of_rooms,	
        'storey':storey,	
        'floor_area_sqm':floor_area_sqm,	
        'remaining_lease':remaining_lease,	
        
       	
      }   
    report_data = pd.DataFrame(user_report_data, index=[0])
    return report_data


user_data = user_report() 

if st.button("predict"):
     model.predict(user_data)
     st.write(model.predict(user_data))