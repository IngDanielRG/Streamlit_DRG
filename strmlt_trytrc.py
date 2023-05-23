from __future__ import annotations
import streamlit as st
import pandas as pd
import numpy as np

game_data = pd.read_csv("Game.csv")

def sidebar():
    # st.title("O")
    st.markdown("<h1 style='text-align: center; color: #7D3C98 ;'> Rearreanged</h1>", unsafe_allow_html=True)
     with st.sidebar:
        st.header("Encabezado")
        st.subheader("Subencabezado")
        text = st.text_area("Filtrar ")

        button0 = st.button("Golf")
        if button0:
            st.write(text)
   
 
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

  with col4:
    button4 = st.button("TRC")
    if button4:
        st.write("No")
    elif not button4:
        st.write("Golf'nt")
      
def xls():
    game_data = pd.read_csv("Game.csv")
        
    
def barra():
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    st.bar_chart(chart_data)
        
sidebar()
header()
xls()
barra()
