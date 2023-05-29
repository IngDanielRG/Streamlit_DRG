import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np



def sidebar():
    st.markdown("<h1 style='text-align: center; color: #7D3C98 ;'> Rearreanged</h1>", unsafe_allow_html=True)

    select = option_menu(
        menu_title = None, #required
        options = ["Operaciones", "Ventas", "Membresías"], #required
        icons = ["gear", "bar-chart", "person-badge"], #optional --- https://icons.getbootstrap.com/
        orientation = "horizontal", 
    )
    
    if select == "Home":
        st.title(f"You have selected {select}")
    elif select == "Projects":
        st.title(f"You have selected {select}")
    elif select == "Contact":
        st.title(f"You have selected {select}")
    
def buttons():
  st.header("TRC")
  col1, col2, col3, col4 = st.columns(4)
  
  with col1:
    button1 = st.button("TRC?")
    if button1:
        st.write("Golf")
    elif not button1:
        st.write("Si")
        
  with col2:
    button2 = st.button("TRC")
    if button2:
        st.write("Golfn't")
    elif not button1:
        st.write("No")
        
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
      
def chart():
    col1, col2 = st.columns(2)
    
    with col1:
            csv_url = "https://raw.githubusercontent.com/IngDanielRG/Streamlit_DRG/main/try.csv"
            # Load the .csv file
            df = pd.read_csv(csv_url, encoding='utf-8')
            # Display the table using Streamlit
            st.bar_chart(df)
            
    with col2:
        chart_data = pd.DataFrame(
            np.random.randn(20, 1),
            columns=['a'])
        st.bar_chart(chart_data)
        
sidebar()
buttons()
chart()
#line()
#bar()
