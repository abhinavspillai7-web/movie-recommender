import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
def prepare_data():
    df=pd.read_csv("movies.csv",sep=",")
    df["genres"]=df["genres"].str.replace("|", " ",regex=False)
    df=df[~(df["genres"] == "(no genres listed)")]
    df = df.reset_index(drop=True)
    tfidf=TfidfVectorizer()
    tfidf_matrix=tfidf.fit_transform(df["genres"])
    return df,tfidf_matrix
def get_recommendations(movie_a,movie_b,movie_c,df,tfidf_matrix):
    selected_movies=(movie_a,movie_b,movie_c)
    movie_indices=[]
    for i in selected_movies:
        movie_indices.append(df[df["title"]==i].index[0])
    score_a=cosine_similarity(tfidf_matrix[movie_indices[0]],tfidf_matrix)
    score_b=cosine_similarity(tfidf_matrix[movie_indices[1]],tfidf_matrix)
    score_c=cosine_similarity(tfidf_matrix[movie_indices[2]],tfidf_matrix)
    combined_score=(score_a+score_b+score_c)/3
    sorted_indices=np.argsort(combined_score[0])[::-1]
    sorted_indices = sorted_indices[~np.isin(sorted_indices, movie_indices)]
    return df.iloc[sorted_indices[:5]]
df, tfidf_matrix = prepare_data()
