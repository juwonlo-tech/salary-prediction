import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

def clean_employment(x):
    if 'Employed full-time' in x or 'Employed, full-time' in x:
        return 'Employed full-time'
    return "Not employed full-time"

def clean_experience(x):
    if x == 'More than 50 years':
        return 50
    if x == 'Less than 1 year':
        return 0.5
    return float(x)

# Function to clean the values in age
def clean_age(x):
    if x == '25-34 years old':
        return 34
    if x == '35-44 years old':
        return 44
    if x == '45-54 years old':
        return 54
    if x == '18-24 years old':
        return 24
    if x == '55-64 years old':
        return 64
    if x == '65 years or older':
        return 65
    if x == 'Under 18 years old':
        return 17
    if x == 'Prefer not to say':
        return np.nan
    return int(x)

# Create a function to combine categories based on requirements
def shorten_category(category, mark):
    categorical_map= {}
    for i in range(len(category)):
        if category.values[i] >= mark:
            categorical_map[category.index[i]]= category.index[i]
        else:
            categorical_map[category.index[i]]= 'Others'
    return categorical_map

def clean_country(x):
    if x == 'United States':
        return 'United States of America'
    if x == 'United Kingdom of Great Britain and Northern Ireland':
        return 'United Kingdom'
    if x == 'Iran, Islamic Republic of...':
        return 'Iran'
    return x

def clean_education(x):
    if "Bachelor’s degree" in x:
        return 'Bachelor’s degree'
    if "Master’s degree" in x:
        return 'Master’s degree'
    if "Professional degree" in x or "Other doctoral" in x:
        return 'Post grad'
    return "Less than a Bachelor's degree"

@st.cache_data 
def load_data():
    df_2020= pd.read_csv('survey_results_public_2020.csv')
    df_2021= pd.read_csv('survey_results_public_2021.csv')
    df_2022= pd.read_csv('survey_results_public_2022.csv')

    # Select most relevant columns for analysis
    df_2020= df_2020[['Country','Age','EdLevel','YearsCodePro','Employment','ConvertedComp']]
    df_2021= df_2021[['Country','Age','EdLevel','YearsCodePro','Employment','ConvertedCompYearly']]
    df_2022= df_2022[['Country','Age','EdLevel','YearsCodePro','Employment','ConvertedCompYearly']]

    # Rename the ConvertedComp for easy comprehension
    df_2020= df_2020.rename(columns={'ConvertedComp':'Salary'})
    df_2021= df_2021.rename(columns={'ConvertedCompYearly':'Salary'})
    df_2022= df_2022.rename(columns={'ConvertedCompYearly':'Salary'})

    # Merge the dataframes
    df= pd.concat([df_2020, df_2021,df_2022], ignore_index=True, sort=False)

    df= df.dropna()

    df['Employment']= df['Employment'].apply(clean_employment)
    df= df[df['Employment']=='Employed full-time']
    df= df.drop('Employment', axis=1)

    df['Age'] = df['Age'].apply(clean_age)
    df= df.dropna()
    # Categorize the ages into groups
    conditions = [
        (df['Age'] <= 18),
        (df['Age'] > 18) & (df['Age'] <= 39),
        (df['Age'] > 39) & (df['Age'] <= 65),
        (df['Age'] > 65)
        ]

    # create a list of the values we want to assign for each condition
    values = ['less than 18', '18-39', '40-65', 'older than 65']

    # create a new column and use np.select to assign values to it using our lists as arguments
    df['Age'] = np.select(conditions, values)

    mark= 200
    country_map= shorten_category(df.Country.value_counts(),mark)
    df['Country']= df['Country'].map(country_map)
    df['Country'] = df['Country'].apply(clean_country)

    df= df[df['Salary'] <=250000] 
    df= df[df['Salary'] >=10000] 
    df= df[df['Country'] !='Others']

    df['YearsCodePro'] = df['YearsCodePro'].apply(clean_experience)
    df['EdLevel']= df['EdLevel'].apply(clean_education)

    df = df.sample(frac = 1)
    
    return df
df= load_data()

def show_explore_page():
    st.title("Explore Software Engineer Salaries")

    st.write(
        """
        ### Stackoverflow Developer Survey 2020
        """
    )

    data = df["Country"].value_counts()

    fig1, ax1 =plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal") # Equal aspect ratio ensures that the pie is drawn as a circle

    st.write(""" ### Number of Data from Different Countries """)
    
    st.pyplot(fig1)

    st.write(""" ### Mean Salary Based on Country """)
    data = df.groupby(["Country"])["Salary"].mean().sort_values(ascending= True)
    st.bar_chart(data)

    st.write(""" ### Mean Salary based on Experience """)
    data = df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending= True)
    st.line_chart(data)



