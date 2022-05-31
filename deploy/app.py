

import streamlit as st
import pandas as pd
import numpy as np


st.title("Restaurant Recommendation System 🍽")
st.caption('Developed By - Rishabh, Surabhi, Kriti, Bhumika')
st.text("Let us help you with finding restaurant in Dehradun 🍴 ")
video_file = open('video1.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)


selectbox = st.sidebar.slider(
    "How satisfied are you after using this recommendation system?", 0, 5)


st.subheader("Whats your preference?")
vegn = st.radio("Vegetables or none!",["veg","non-veg"],index = 1)

st.subheader("What Cuisine do you prefer?")
cuisine = st.selectbox("Choose your favourite!",['Healthy Food', 'Snack', 'Dessert', 'Japanese', 'Indian'])


st.subheader("whats ur age ?")
age = st.slider("age!",1,100,1,10)

st.subheader("Enter the max budget!")
budget = st.slider("From low to high",0,5000,500,500)    # min, max, startfrom, step




res = pd.read_csv("C:/Users/risha/Desktop/final-touch/Food-Recommendation-System-master/input/food.csv")


ans = res.loc[(res.C_Type==cuisine) & (res.Veg_Non == vegn) &(res.min_age<=age) & (age<res.max_age) & (res.price<=budget) ,['Name','C_Type','Veg_Non','url']]  # true, col values




names = ans['Name'].tolist()
url = ans['url'].tolist()

x = np.array(names)
y=np.array(url)

final_names = np.unique(x)
final_url =np.unique(y)

final_len=len(ans)


bruh = st.checkbox("Recommended Restaurent")
if bruh == True:
    i=0
    while i<final_len:
        st.write(final_names[i]+"\t"+final_url[i])
        i+=1




