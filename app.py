import streamlit as st
import train
st.set_page_config(
    page_title="Film Concierge",
    page_icon="🎬",
    layout="wide"
)
st.markdown("""<label class="eyebrow">MOVIE DISCOVERY</label>
<h1 class="hero-title">YOUR PERSONAL MOVIE Concierge</h1> 
<p class="hero-subtitle">Your taste. Your next favourite movie</p>""",unsafe_allow_html=True)
st.markdown("""
<style>
    .stApp {
        background-color: #141414;
    }
    .eyebrow {
    color: #e50914;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 3px;
}

.hero-title {
    color: #ffffff;
    font-size: 48px;
    font-weight: 800;
}

.hero-subtitle {
    color: #b3b3b3;
    font-size: 18px;
}
.stButton > button {
    background-color: #e50914;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 12px 28px;
    font-weight: 700;
}
.stButton > button:hover {
    background-color: #ff1f2b;
    color: white;
    border: none;
    transform: scale(1.03);
    transition: 0.2s ease;
}
.movie-card{
background-color: #242424;
color: white;
padding: 18px;
border-radius: 10px;
margin-bottom: 12px;
border-left: 4px solid #e50914;
}
.movie-card:hover{
background-color: #e50914;
border-left-color: white;
transform: scale(1.02);
transition: 0.2s ease;
}
.stSelectbox > div > div:hover {
    border-color: #e50914;
}

.stSelectbox > div > div:focus-within {
    border-color: #e50914;
    box-shadow: 0 0 0 1px #e50914;
}
.stSelectbox> div:hover {
    background-color: #e50914;
    color: white;
}
</style>
""", unsafe_allow_html=True)
col1,col2,col3=st.columns(3)
with col1:
    movie_a=st.selectbox("select your first movie",train.df["title"])
with col2:
    movie_b=st.selectbox("select your second movie",train.df["title"])
with col3:
    movie_c=st.selectbox("select your third movie",train.df["title"])
if st.button("Get Recommendation"):
    if len(set([movie_a, movie_b, movie_c])) == 3:
        recommendations=train.get_recommendations(movie_a,movie_b,movie_c,train.df,train.tfidf_matrix)
        for index, row in recommendations.iterrows():
            st.markdown(f'<div class="movie-card">{row["title"]}</div>',unsafe_allow_html=True)
    else:
        st.warning("Please select three different movies.")