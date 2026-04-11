import streamlit as st
import pandas as pd

# 1. Configuración de la página
st.set_page_config(page_title="Mi Buscador de Código", layout="wide")
st.title("📂 Dashboard de Proyectos")

# 2. Tus datos (Esto podrías cargarlo de un CSV externo)
data = [
    {"Nombre": "Limpieza de Datos", "Tag": "Data Science", "Link": "https://github.com/..."},
    {"Nombre": "Script de Scraping", "Tag": "Python", "Link": "https://github.com/..."},
    {"Nombre": "Dashboard Ventas", "Tag": "Visualización", "Link": "https://github.com/..."},
]
df = pd.DataFrame(data)

# 3. Buscador y Filtros
busqueda = st.text_input("🔍 Buscar código por nombre...")
tag_seleccionado = st.selectbox("Filtrar por categoría:", ["Todos"] + list(df['Tag'].unique()))

# 4. Lógica de filtrado
df_filtrado = df[df['Nombre'].str.contains(busqueda, case=False)]
if tag_seleccionado != "Todos":
    df_filtrado = df_filtrado[df_filtrado['Tag'] == tag_seleccionado]

# 5. Mostrar resultados
st.table(df_filtrado)
