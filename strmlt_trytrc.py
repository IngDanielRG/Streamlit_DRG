from __future__ import annotations
import streamlit as st
import pandas as pd
import numpy as np



def sidebar():
    st.markdown("<h1 style='text-align: center; color: #7D3C98 ;'> Rearreanged</h1>", unsafe_allow_html=True)
    
    with st.sidebar:
        selected = st.sidebar.selectbox(
            "Main Menu", #required
            ["Home", "Projects", "Contact"], #required
        )
    if selected == "Home":
        st.title(f"You have selected {selected}")
    elif selected == "Projects":
        st.title(f"You have selected {selected}")
    elif selected == "Contact":
        st.title(f"You have selected {selected}")
            
           
def header():
  st.header("TRC")
  col1, col2, col3, col4 = st.columns(4)
  
  with col1:
    button1 = st.button("TRC?")
    if button1:
        st.write("Si")
    elif not button1:
        st.write("Golf")
        
  with col2:
    button2 = st.button("TRC")
    if button2:
        st.write("No")
    elif not button1:
        st.write("Golf'nt")
        
  with col3:
    button3 = st.button("Doc")
    if button3:
        st.write("No")
    elif not button3:
        st.write("Ask")

  with col4:
    button4 = st.button("Han")
    if button4:
        st.write("No")
    elif not button4:
        st.write("Q")
      
def csv():
    csv_url = "https://raw.githubusercontent.com/IngDanielRG/Streamlit_DRG/main/try.csv"
    # Load the .csv file
    df = pd.read_csv(csv_url, encoding='utf-8')
    # Display the table using Streamlit
    st.line_chart(df)
        
    
def barra():
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    st.bar_chart(chart_data)
        
sidebar()
header()
csv()
barra()
