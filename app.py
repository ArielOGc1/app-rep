import pandas as pd
import plotly.express as px
import streamlit as st

df_car= pd.read_csv('vehicles_us.csv')

st.header('Vision de datos')
df_car.dropna(subset= ['is_4wd', 'paint_color'], inplace=True)
st.write(df_car)

st.header('Vehiculos por su fabricante')
df_manufacturer= df_car.groupby(by= ['type', 'model']).count().reset_index()
bar_charts= px.bar(df_manufacturer,x= 'model', color='type')
st.plotly_chart(bar_charts, use_container_width=True)

st.header('Histogramas')
hist_checkbox= st.checkbox('Construir un histograma')
if hist_checkbox: # al hacer clic en el botón
         # escribir un mensaje
         st.write('Creación de un histograma acerca del kilometraje de los vehiculos')
         
         # crear un histograma
         fig = px.histogram(df_car, x="odometer")
     
         # mostrar un gráfico Plotly interactivo
         st.plotly_chart(fig, use_container_width=True)

st.header('Dispersion')
scatter_checkbox= st.checkbox('Construir un grafico de dispersion')
if scatter_checkbox:
        # escribe un mensaje
        st.write('Creacion de un grafico de dispersion entre el kilometraje y el precio de los vehiculos')

        # crea el grafico de dispersion
        fig_scatter= px.scatter(df_car, x= 'odometer', y= 'price')

        # muestra un grafico interactivo
        st.plotly_chart(fig_scatter, use_container_width=True)
