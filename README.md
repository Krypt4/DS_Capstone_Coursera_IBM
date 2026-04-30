# DS-Capstone-Coursera-IBM

# Resumen del Proyecto SpaceX

## 01 – Recolección de Datos
* **1_API_Collection.ipynb**: Obtención de datos mediante la API oficial de SpaceX. Se filtran lanzamientos del Falcon 9 y se exportan a `dataset_part_1.csv`.
* **2_Web_Scraping.ipynb**: Extracción de información adicional sobre Falcon 9 y Falcon Heavy desde Wikipedia. Los datos se consolidan en `wiki_launches.csv`.

## 02 – Limpieza de Datos
* **3_Data_Wrangling.ipynb**: Transformación de los datos de la API. Se introduce la variable objetivo `Class` (1 para aterrizaje exitoso, 0 para fallo) y se genera el archivo `dataset_part_2.csv`.

## 03 – Análisis Exploratorio (EDA)
* **4_EDA_SQL.ipynb**: Consultas en SQL para identificar patrones, calcular el total de éxitos y la masa promedio de la carga útil.
* **5_EDA_Visualization.ipynb**: Uso de la librería Seaborn para analizar visualmente la relación entre el número de vuelo, el sitio de lanzamiento y la tasa de éxito.

## 04 – Mapas Interactivos y Dashboard
* **6_Interactive_Maps_Folium.ipynb**: Creación de mapas con Folium. Incluye clusters de marcadores por colores (verde para éxito, rojo para fallo) y cálculos de distancia a la costa mediante la fórmula de Haversine.
* **7_Launch_Site_Dash_App.py**: Desarrollo de una aplicación con Dash que permite filtrar por sitio de lanzamiento y visualizar gráficos dinámicos de rendimiento.

## 05 – Machine Learning
* **8_Machine_Learning_Prediction.ipynb**: Entrenamiento y evaluación de modelos predictivos.
    * **Proceso**: Normalización con `StandardScaler`, división de datos (80/20) y optimización de hiperparámetros con `GridSearchCV`.
    * **Algoritmos evaluados**: Regresión Logística, SVM, Árboles de Decisión y KNN.
    * **Objetivo**: Comparar la precisión (accuracy) para seleccionar el mejor modelo de predicción de aterrizajes.