import streamlit as st
import requests
import json

# URL de votre fonction Azure
azure_function_url = "https://functionrecommend.azurewebsites.net/api/recommend"

# Titre de l'application
st.title('Recommandation d\'articles')

# Entrée pour l'ID utilisateur
user_id = st.number_input('Entrez votre ID utilisateur:', min_value=0)

# Bouton pour obtenir des recommandations
if st.button('Obtenir des recommandations'):
    # Appel de la fonction Azure
    params = {'user_id': user_id}
    response = requests.get(azure_function_url, params=params)
    
    # Traitement de la réponse
    if response.status_code == 200:
        data = response.json()
        st.write(f"ID utilisateur: {data['user_id']}")
        st.write("Recommandations:")
        for rec in data['recommendations']:
            st.write(f"- Article ID: {rec}")
    else:
        st.error(f"Erreur: {response.text}")
