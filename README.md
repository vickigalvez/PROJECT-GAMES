# PROYECTO INDIVIDUAL

# MACHINE LEARNING OPERATIONS (MLOps)
![image](https://github.com/vickigalvez/PROJECT-GAMES/assets/106280956/24999e71-5704-438e-9803-cc2230d76fb4)

# INTRODUCCION AL PROYECTO:
En este proyecto abordamos un procedimiento completo de MLOps Engineer que incluye tres etapas principales: Ingeniería de Datos, Análisis Exploratorio y Transformación de los Datos, y Modelado con Técnicas de Machine Learning.

En la primera etapa, implementaremos técnicas de Ingeniería de Datos para disponibilizar los datos para su posterior consumo y consulta. Crearemos consultas específicas para obtener información relevante.

En la segunda etapa, nos sumergiremos en la fase de Análisis Exploratorio de los Datos (EDA), donde limpiaremos y exploraremos los datos para prepararlos adecuadamente para la recomendación. Este análisis será un paso crucial para entender las relaciones entre las variables y detectar posibles patrones y anomalías.

En la tercera y última etapa, llegaremos al corazón de este proyecto: el Modelo de Recomendación. Aquí utilizaremos un modelo de machine learning para desarrollar un sistema de recomendación sobre los juegos en Steam utilizando técnicas de cálculo de similitud. Además, se desarrolló una API utilizando el framework FastAPI para disponibilizar los datos y se implementaron diferentes consultas para interactuar.

# TAREAS REALIZADAS
1. ETL
Realizamos un proceso de ETL (Extracción, Transformación y Carga) en el que extrajimos datos de diferentes fuentes, los transformamos según las necesidades del proyecto y los cargamos en un destino final para su análisis y uso posterior. Las herramientas utilizadas fueron: Python, Pandas Y Textblob

2. EDA
Se realizó un Análisis Exploratorio de Datos (EDA) para investigar las relaciones entre las variables del dataset y descubrir patrones. Se utilizaron técnicas de visualización y se generaron gráficas. Las herramientas utilizadas fueron: Numpy, Pandas, Matplotlib, Seaborn, Wordcloud, NLTK, scikit-learn.

3. Deployment de la API
Se desarrolló una API utilizando el framework FastAPI para disponibilizar los datos. Se implementaron las siguientes consultas:

   def PlayTimeGenre( genero : str ): devuelve el año con mas horas jugadas para dicho género.

   def UserForGenre( genero : str ): Devuelve el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.

   def UsersRecommend( año : int ): Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. 

   def UsersNotRecommend( año : int ): Devuelve el top 3 de juegos MENOS recomendados por usuarios para el año dado.

   def sentiment_analysis( año : int ): Según el año de lanzamiento, devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados     con un análisis de sentimiento.

   Las herramientas utilizadas fueron: Uvicorn, Render, FastAPI

5. Modelo de Machine Learning
Realizamos un modelo de Machine Learning para generar recomendaciones de juegos, utilizando algoritmos y técnicas que analizaron patrones en los datos de usuarios y juegos, con el fin de brindar recomendaciones personalizadas y precisas basadas en los gustos y preferencias de cada usuario. La herramienta utilizada fue: Scikit-Learn

# LINKS DE UTILIDAD 
➮ Deployment: [Link de Render](https://project-deploy-682s.onrender.com)https://project-deploy-682s.onrender.com
➮ Video: Link al Video





