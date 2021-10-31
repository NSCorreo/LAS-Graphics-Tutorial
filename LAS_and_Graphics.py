import streamlit as st
from PIL import Image
import cv2 
import numpy as np



def main():

    selected_box = st.sidebar.selectbox(
    'Seleccione Una Opción',
    ('Bienvenido','Simple Graph GR')
    )
    
    if selected_box == 'Bienvenido':
        welcome() 
    if selected_box == 'Simple Graph GR':
        Simple_Graph_GR()
    #if selected_box == 'Video':
    #    video()
    #if selected_box == 'Face Detection':
    #    face_detection()
    #if selected_box == 'Feature Detection':
    #    feature_detection()
    #if selected_box == 'Object Detection':
    #    object_detection() 
 

def welcome():
    
    st.title('Image Processing using Streamlit')
    
    st.subheader('Esta es una simple aplicación que muestra como utilizar la librería WELLY en Phyton,  par efectuar la lectura'
             + ' de archivos LAS y generar las gráficas  correspondientes. ')
    st.subheader('El programa utiliza Jypiter Notebook como plataforma para ejecutar el código Python.')
    st.subheader('**  Seleccione una opción en el menu de la izquierda. **')

    st.subheader('*****  Aqui va el LOGO de le Empresa. *****')
#    st.image('01_Lectura_de_datos_crear_simple_gráfico_GR.jpg',use_column_width=True)


def Simple_Graph_GR():
    
    st.title('01 Lectura de datos y crear simple gráfico GR')
    
    st.subheader('Demostración de como se puede hacer la lectura de datos de un archivo LAS y crear'
             + ' el gráfico correspondiente, utilizando la interface Jupyter Notebook ' + 
             'y la libreria Welly.')
    
    st.image('01_Lectura_de_datos_crear_simple_gráfico_GR.jpg',use_column_width=True)


if __name__ == "__main__":
    main()