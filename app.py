from enum import unique
import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(page_title='Online Education Survey',layout="wide")

df= pd.read_csv('online_education_survey.csv')


#Sidebar

st.sidebar.header("Please select feeature here:")
Education_level= st.sidebar.multiselect(
    "select the education level of the student:",
    options=df['Level_of_Education'].unique(),
    default=df['Level_of_Education'].unique()
)

Gender= st.sidebar.multiselect(
    "Select the Gender:",
    options=df['Gender'].unique(),
    default= df['Gender'].unique()
)

Economic_status= st.sidebar.multiselect(
    "Select the Economic_status:",
    options=df['Economic_status'].unique(),
    default= df['Economic_status'].unique()
)

df_selection= df.query(
    "Gender==@Gender & Level_of_Education==@Education_level & Economic_status==@Economic_status"
)




#barchart

fig_hist=px.histogram(df_selection,x='Performance_in_online',category_orders=dict(Performance_in_online=["1", "2", "3", "4","5","6","7","8","9","10"]))

fig_hist.update_layout(yaxis_title="Number of Students",bargap=0.2)
st.plotly_chart(fig_hist)

st.dataframe(df_selection)
