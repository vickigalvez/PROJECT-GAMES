from fastapi import FastAPI
import pandas as pd
import uvicorn
import numpy as np 

from sklearn.utils.extmath           import randomized_svd
from sklearn.metrics.pairwise        import cosine_similarity
from sklearn.metrics.pairwise        import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv('data_final.csv')
app = FastAPI()

#Prueba
@app.get('/')
def start():
    return 'Maria_Victoria_Galvez'

#Funcion creada con el objetivo de obtener el año con mas horas jugadas para un determinado género
@app.get('/genero/{genre}')
def PlayTimeGenre(genre: str):
    genre_df = df[df[genre] == 1]
    year_playtime_df = genre_df.groupby('release_year')['playtime_forever'].sum().reset_index()
    max_playtime_year = year_playtime_df.loc[year_playtime_df['playtime_forever'].idxmax(), 'release_year']
    return {f"Año de lanzamiento con más horas jugadas para genero {genre}": int(max_playtime_year)}


#Función creada para obtener el usuario con mas horas jugadas para un determinado género
@app.get('/usuario_por_genero/{genero}')
def UserForGenre(genero: str) -> dict:
    genero_df = df[df[genero] == 1]
    max_playtime_user = genero_df.loc[genero_df['playtime_forever'].idxmax(), 'user_id']
    year_playtime_df = genero_df.groupby('release_year')['playtime_forever'].sum().reset_index()
    playtime_list = year_playtime_df.to_dict(orient='records')

    result = {
        "Usuario con más horas jugadas para Género " + genero: max_playtime_user,
        "Horas jugadas": playtime_list
    }
    return result


#Función creada para obtener el top 3 de juegos MAS recomendados por usuarios por año
@app.get('/top3_mas_recomendados/{anio}')
def UsersRecommend(anio: int):
    df_filtrado = df[(df['posted_year'] == anio) & (df['recommend'] == True) & (df['sentiment_analysis'] >= 1)]
    
    if df_filtrado.empty:
        return 'Valor no encontrado'
    
    df_ordenado = df_filtrado.sort_values(by='sentiment_analysis', ascending=False)
    top_3_reseñas = df_ordenado.head(3)
    resultado = [
        {"Puesto 1": top_3_reseñas.iloc[0]['app_name']},
        {"Puesto 2": top_3_reseñas.iloc[1]['app_name']},
        {"Puesto 3": top_3_reseñas.iloc[2]['app_name']}
    ]
    return resultado


#Función creada para obtener el top 3 de juegos MENOS recomendados por usuarios por año 
@app.get('/top3_menos_recomendados/{anio}')
def UsersNotRecommend(anio:int):
    df_filtrado = df[(df['posted_year'] == anio) & (df['recommend'] == False) & (df['sentiment_analysis'] == 0)]
    
    if df_filtrado.empty:
        return 'Valor no encontrado'
    
    df_ordenado = df_filtrado.sort_values(by='sentiment_analysis', ascending=True)
    top_3_reseñas = df_ordenado.head(3)
    resultado = [
        {"Puesto 1": top_3_reseñas.iloc[0]['app_name']},
        {"Puesto 2": top_3_reseñas.iloc[1]['app_name']},
        {"Puesto 3": top_3_reseñas.iloc[2]['app_name']}
    ]
    return resultado


#Función creada para obtener la cantidad de registros de reseñas de usuarios
@app.get('/cantidad_reseñas/{anio}')
def sentiment_analysis(anio:int):
    df_filtrado = df[df['release_year'] == anio]
    
    if df_filtrado.empty:
        return 'Valor no encontrado'
    
    cantidad_negativos = df_filtrado[df_filtrado['sentiment_analysis'] == 0].shape[0]
    cantidad_neutrales = df_filtrado[df_filtrado['sentiment_analysis'] == 1].shape[0]
    cantidad_positivos = df_filtrado[df_filtrado['sentiment_analysis'] == 2].shape[0]
    resultado = {
        'Negative': cantidad_negativos,
        'Neutral': cantidad_neutrales,
        'Positive': cantidad_positivos
    }
    return resultado


#Creamos una muestra para el modelo
muestra = df.head(4000) 

#Creamos el modelo de machine learning con Scikit-Learn
tfidf = TfidfVectorizer(stop_words='english')
muestra=muestra.fillna("")

tdfid_matrix = tfidf.fit_transform(muestra['review'])
cosine_similarity = linear_kernel( tdfid_matrix, tdfid_matrix)


#Función creada para recomendar  5 juegos similares al ingresado.
@app.get('/recomendacion_juego/{id_producto}')
def recomendacion(id_producto: int):
    if id_producto not in muestra['steam_id'].values:
        return {'mensaje': 'No existe el id del juego.'}

    idx = muestra[muestra['steam_id'] == id_producto].index[0]
    sim_cosine = list(enumerate(cosine_similarity[idx]))
    sim_scores = sorted(sim_cosine, key=lambda x: x[1], reverse=True)
    sim_ind = [i for i, _ in sim_scores[1:6]]
    sim_juegos = muestra['app_name'].iloc[sim_ind].values.tolist()

    return {'juegos recomendados': list(sim_juegos)}


# Se crea la funcion de recomendación de 5 juegos recomendados para el usuario ingresado.
@app.get('/recomendacion_usuario/{id_usuario}')
def recomendacion_usuario(id: int):
    if id not in muestra['id'].values:
        return {'mensaje': 'No existe el id del juego.'}
    
    titulo = muestra.loc[muestra['id'] == id, 'app_name'].iloc[0]
    idx = muestra[muestra['app_name'] == titulo].index[0]
    sim_cosine = list(enumerate(cosine_similarity[idx]))
    sim_scores = sorted(sim_cosine, key=lambda x: x[1], reverse=True)
    sim_ind = [i for i, _ in sim_scores[1:6]]
    sim_juegos = muestra['app_name'].iloc[sim_ind].values.tolist()
    return {'juegos recomendados': list(sim_juegos)}

