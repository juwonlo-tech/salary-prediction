import streamlit as st
import pickle
import numpy as np

def load_model():
	with open('procedures.pkl','rb') as file:
		data= pickle.load(file)
		return data

data= load_model()

loaded_model= data['model']
country_encoder= data['country_encoder']
edu_encoder= data['edu_encoder']
age_encoder= data['age_encoder']

def show_predict_page():
	st.title("Software Developer Salary Prediction")

	st.write("""### We need some information to predict the salary""")

	countries= (
		'United States of America', 'United Kingdom', 'Spain', 'Netherlands', 'Germany', 'Canada', 'Belgium', 
		'Italy', 'Brazil', 'France', 'Poland', 'Indonesia', 'Greece', 'Czech Republic', 'India', 'Ukraine', 
		'Switzerland', 'Hungary', 'Romania', 'Portugal', 'Mexico', 'Israel', 'Nigeria', 
		'Finland', 'Sweden', 'Austria', 'Turkey', 'Others', 'Ireland', 'Estonia', 
		'Philippines', 'Australia', 'Sri Lanka', 'Taiwan', 'Croatia', 'Egypt', 'Argentina', 
		'Iran', 'Norway', 'Pakistan', 'Lithuania', 'Nepal', 'Denmark', 'Bangladesh', 'Russian Federation', 
		'South Africa', 'Chile', 'Colombia', 'Serbia', 'New Zealand', 'Singapore', 'Bulgaria', 'Slovenia', 
		'China', 'Japan', 'Malaysia', 'Viet Nam', 'South Korea', 'Slovakia'
	)

	education= (
		'Bachelor’s degree', 'Master’s degree',
		"Less than a Bachelor's degree", 'Post grad'
	)

	age= ('less than 18', '18-39', '40-65', 'older than 65')

	country =st.selectbox("Country", countries)
	education =st.selectbox("Education Level", education)
	age= st.selectbox("Age Range", age)

	experience= st.slider("Years of Experience", 0, 50, 3)

	ok= st.button("Calculate Salary")
	if ok: 
		X = np.array([[country, education, age, experience ]])
		X[:, 0] = country_encoder.transform(X[:,0])
		X[:, 1] = edu_encoder.transform(X[:,1])
		X[:, 2] = age_encoder.transform(X[:,2])
		X = X.astype(float)

		salary = loaded_model.predict(X)

		st.subheader(f"The estimated salary is ${salary[0]:.2f}")
