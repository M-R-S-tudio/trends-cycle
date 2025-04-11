
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Charger les données
@st.cache_data
def load_data():
    return pd.DataFrame({
        "Année": list(range(1920, 2030, 5)),
        "Hemline": [3, 4, 1, 0, 2, 3, 5, 4, 7, 9, 6, 4, 7, 8, 3, 4, 9, 8, 2, 5, 3, 6],
        "Fashioncut": [6, 5, 3, 2, 4, 4, 2, 3, 5, 6, 7, 8, 8, 7, 4, 6, 1, 2, 9, 6, 8, 6],
        "Matiere": [2, 2, 3, 3, 4, 4, 3, 3, 5, 6, 5, 6, 8, 7, 6, 5, 9, 9, 6, 5, 6, 5],
        "Couleur": [8, 7, 4, 3, 4, 4, 6, 5, 7, 9, 9, 8, 10, 9, 6, 5, 10, 9, 3, 6, 4, 7],
        "Accessoires": [7, 6, 3, 2, 4, 3, 5, 4, 6, 7, 6, 5, 9, 8, 6, 5, 8, 9, 6, 6, 7, 6],
        "Genre": [7, 8, 9, 10, 10, 9, 10, 10, 8, 6, 5, 6, 8, 7, 6, 5, 7, 7, 3, 4, 2, 3],
        "Originalite": [6, 5, 3, 2, 3, 3, 2, 2, 6, 8, 9, 7, 9, 8, 6, 6, 9, 8, 3, 5, 7, 8],
        "Contexte": [6, 8, 2, 1, 3, 5, 8, 7, 6, 7, 5, 3, 9, 7, 4, 5, 9, 8, 2, 6, 4, 7]
    })

# Chargement des données
df = load_data()

# Interface utilisateur
st.title("TRENDS CYCLE — Histoire stylistique (1920–2025)")
st.markdown("Explore les relations entre les tendances mode et le contexte socio-politique de chaque époque.")

# Sélection d'un ou plusieurs indices
indices = ["Hemline", "Fashioncut", "Matiere", "Couleur", "Accessoires", "Genre", "Originalite"]
selected = st.multiselect("Choisis les indices stylistiques à comparer avec le contexte :", options=indices, default=indices[:3])

# Affichage interactif du graphique
fig = go.Figure()

# Ajouter l'indice de contexte
fig.add_trace(go.Scatter(x=df["Année"], y=df["Contexte"], mode="lines+markers", name="Contexte", line=dict(color="black")))

# Ajouter les indices sélectionnés
colors = ["blue", "green", "orange", "red", "pink", "brown", "purple"]
for i, name in enumerate(selected):
    fig.add_trace(go.Scatter(x=df["Année"], y=df[name], mode="lines+markers", name=name, line=dict(color=colors[i % len(colors)])))

# Affichage du graphique
fig.update_layout(title="Comparaison des indices stylistiques et du contexte socio-économique", xaxis_title="Année", yaxis_title="Indice (0 à 10)", height=600)
st.plotly_chart(fig, use_container_width=True)

# Légende
st.markdown("""
**Légende des indices**  
- **Hemline** : Longueur des jupes (10 = mini, 0 = longue)  
- **Fashioncut** : Coupe des vêtements (10 = oversize, 0 = skinny)  
- **Matiere** : Présence de matières synthétiques (10 = synthétique, 0 = naturel)  
- **Couleur** : Saturation des couleurs (10 = très vive, 0 = neutre)  
- **Accessoires** : Degré d'accessoirisation (10 = maximal, 0 = minimal)  
- **Genre** : Binarité du genre dans la mode (10 = très genré, 0 = neutre)  
- **Originalite** : Liberté stylistique/créativité (10 = très créatif, 0 = uniforme)  
- **Contexte** : Contexte socio-économique (10 = prospère, 0 = crise)
""")
