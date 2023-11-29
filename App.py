import streamlit as st
import pickle 

movies = pickle.load(open('netflix_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_list = movies["title"].values

# Streamlit app code
st.header("Movie Recommendation System")
selectvalue=st.selectbox("Select the netflix from dropdown", movies_list)

def recommended(movie):
    index=movies[movies['title']==movies].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    recommended_movie=[]
    for i in distance[1:6]:
        recommended_movie.append(movies.iloc[i[0]].title)
    return recommended_movie


if st.button("Show Recommeded"):
    movie_name = recommended(selectvalue)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
      st.text(movie_name[0])
    with col2:
      st.text(movie_name[1])
    with col3:
      st.text(movie_name[2])
    with col4:
      st.text(movie_name[3])
    with col5:
      st.text(movie_name[4])