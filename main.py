import streamlit as st

# Interface utilisateur
st.title("Générateur de Flowchart Dynamique")
st.write("Collez le code Python de votre flowchart dans la zone de texte ci-dessous, puis cliquez sur le bouton pour générer et afficher le flowchart.")

# Zone de texte pour coller le code Python
code = st.text_area(
    "Collez ici le code Python de création du flowchart (utilisant Graphviz)",
    height=300,
    placeholder="Exemple : \nfrom graphviz import Digraph\n\n..."
)

# Bouton pour exécuter le code
if st.button("Générer le Flowchart"):
    try:
        # Afficher le flowchart
        st.graphviz_chart(code)
    except Exception as e:
        st.error(f"Une erreur s'est produite lors de l'exécuton du code : {str(e)}")