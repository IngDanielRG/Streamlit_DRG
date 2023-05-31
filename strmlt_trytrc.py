import streamlit as st
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import altair as alt


def sidebar():
    st.markdown("<h1 style='text-align: center; color: #7D3C98 ;'> Rearreanged</h1>", unsafe_allow_html=True)

    select = option_menu(
        menu_title = None, #required
        options = ["Operaciones", "Ventas", "Membresías"], #required
        icons = ["gear", "bar-chart", "person-badge"], #optional --- https://icons.getbootstrap.com/
        orientation = "horizontal", 
    )
    
   # if select == "Home":
    #    st.title(f"You have selected {select}")
   # elif select == "Projects":
    #    st.title(f"You have selected {select}")
   # elif select == "Contact":
    #    st.title(f"You have selected {select}")
    
def buttons():
  st.header("IMU")
  col1, col2, col3 = st.columns(3)
        
  with col1:
    col1.metric("Ingresos por Membresía", "100K", "20%")
        
  with col2:
    col2.metric("Ingresos por Vendedor", "20MDP", "30%")

  with col3:
    col3.metric("Costos de Operación", "100K", "-4.2")
    
      
def chart():
    col1, col2 = st.columns(2)
    
    with col1:
            csv_url = "https://raw.githubusercontent.com/IngDanielRG/Streamlit_DRG/main/try.csv"
            # Load the .csv file
            df = pd.read_csv(csv_url, encoding='utf-8')
            # Display the table using Streamlit
            st.line_chart(df)
            
    with col2:
            source = pd.DataFrame({
                "Dummy" : [2, 4, 6, 8 ,10, 12, 14, 16, 18, 20, 22, 26],
                "Memberships" :[ 15, 14, 9, 24, 11, 15, 15, 18, 14, 15, 13, 17],
                "Month" :["ENE", "FEB", "MAR", "ABR", "MAY", "JUN", "JUL", "AGO", "SEPT", "OCT", "NOV", "DIC"]
            })
                
            bar_chart = alt.Chart(source).mark_bar().encode(
                y = "Memberships", 
                x = "Month",
            )
            st.altair_chart(bar_chart, use_container_width=True)       
    
def pie():
    col1 = st.colums(1)
    
    with col1:
        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
        sizes = [15, 30, 45, 10]
        explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        st.pyplot(fig1)
        

    
            
                
sidebar()
buttons()
#line()
#bar()
