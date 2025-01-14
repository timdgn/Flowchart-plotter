import streamlit as st

# Interface utilisateur
st.title("Générateur de Flowchart Dynamique")

st.markdown("#####")

# Popover pour aider l'utilisateur
with st.expander("Rappel du prompt pour ChatGPT (Copie tout le texte présent dans la zone en dessous)"):
    st.markdown(
        r"""
        Utilise ce document joint et le processus qui y est décrit pour créer un flowchart avec python et la librairie GraphViz. Si nécessaire, inclus au sein des nodes des critères s’ils sont indiqués dans le document. Ta réponse ne doit inclure que le code python nécessaire pour créer le flowchart. Tu dois absolument donner le code en language Dot de GraphViz, pas autrement.

        Voici un exemple de formatage de code dont tu dois t’inspirer:

        “””
        digraph Validation_Process {
            rankdir="TB";
            size="10";

            // Noeuds principaux du processus
            Start [label="Début du processus", shape="ellipse"];
            Inventory [label="Mise à jour de l'inventaire des SI", shape="box"];
            NewSystem [label="Nouveaux systèmes ?", shape="diamond"];
            SystemChange [label="Modifications des systèmes ?", shape="diamond"];
            Validation [label="Validation / Revalidation ?", shape="diamond"];
            Abandoned [label="Systèmes abandonnés ?", shape="diamond"];
            ImpactGMP [label="Détermination de l'impact GMP\n\nCritères:\n1. Partie intégrante d'un équipement.\n2. Surveillance qualité.\n3. Traçabilité produit.\n4. Soumissions réglementaires.\n5. Etiquetage/traçabilité.\n6. Données critiques.\n7. Conformité réglementaire.", shape="box"];
            Categorization [label="Catégorisation des risques et criticités\n\nCatégories:\n- Cat. 1: Logiciels d'infrastructure.\n- Cat. 3: Produits standards.\n- Cat. 4: Produits configurés.\n- Cat. 5: Applications personnalisées.", shape="box"];
            RiskAssessment [label="Évaluation des risques\n\nMatrice:\nNon complexe / Complexe\n- Critique: Modéré / Élevé\n- Majeure: Modéré / Modéré\n- Mineure: Faible / Modéré.", shape="box"];
            ValidationPlan [label="Création du Plan de Validation", shape="box"];
            Qualification [label="Qualification (QI, QO, QP)", shape="box"];
            Testing [label="Tests\n\n- Vérification des calculs.\n- Vérification des protections.\n- Tests aux limites.\n- Sécurité des accès.", shape="box"];
            Report [label="Rédaction du rapport de validation", shape="box"];
            Archive [label="Archivage et maintien de l'état validé", shape="ellipse"];
            End [label="Fin du processus", shape="ellipse"];

            // Liaisons entre les étapes
            Start -> Inventory;
            Inventory -> NewSystem;
            NewSystem -> ImpactGMP [label="Oui"];
            NewSystem -> SystemChange [label="Non"];
            SystemChange -> ImpactGMP [label="Oui"];
            SystemChange -> Validation [label="Non"];
            Validation -> ImpactGMP [label="Oui"];
            Validation -> Abandoned [label="Non"];
            Abandoned -> Categorization [label="Non"];
            Abandoned -> End [label="Oui"];
            ImpactGMP -> Categorization;
            Categorization -> RiskAssessment;
            RiskAssessment -> ValidationPlan;
            ValidationPlan -> Qualification;
            Qualification -> Testing;
            Testing -> Report;
            Report -> Archive;
            Archive -> End;
        }
        “””

        A toi :
        """
    )

st.markdown("#####")

# Zone de texte pour coller le code Python
code = st.text_area(
    "Colle ici le code Python de création du flowchart qui a été généré par ChatGPT",
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