import streamlit as st

st.set_page_config(page_title="Analyse Repas Santé", layout="centered")
st.title("Analyse de ton repas")
st.markdown("Cette application t'aide à évaluer ton repas selon ton régime personnalisé (LUV, protéinurie, acide urique, sarcoïdose).")

st.header("1. Téléverse une photo (optionnel)")
uploaded_file = st.file_uploader("Téléverse une image de ton repas", type=["jpg", "jpeg", "png"])

st.header("2. Sélectionne les aliments présents dans ton repas")
aliments = [
    "Tofu", "Œuf", "Saumon", "Poulet", "Pois chiches", "Lentilles", "Riz basmati", "Quinoa",
    "Pain de seigle", "Pain complet", "Avocat", "Amandes", "Graines de courge", "Brocolis", "Courgettes",
    "Épinards", "Fenouil", "Carottes", "Betteraves", "Tomates", "Concombres", "Cerises", "Myrtilles",
    "Poire", "Pomme", "Dattes", "Fromage blanc", "Yaourt nature", "Gyoza végétarien", "Aubergines"
]
aliments_selectionnes = st.multiselect("Quels aliments sont présents ?", aliments)

st.header("3. Résultat de l'analyse")

def analyse_repas(aliments_selectionnes):
    score = 0
    remarques = []

    proteines_veg = {"Tofu", "Pois chiches", "Lentilles"}
    if any(a in proteines_veg for a in aliments_selectionnes):
        score += 1
        remarques.append("Bon apport en protéines végétales.")

    proteines_animales = {"Œuf", "Saumon", "Poulet"}
    if any(a in proteines_animales for a in aliments_selectionnes):
        score += 0.5
        remarques.append("Protéines animales présentes (à modérer en cas de protéinurie).")

    purines = {"Lentilles", "Pois chiches", "Saumon", "Dattes"}
    if any(a in purines for a in aliments_selectionnes):
        score -= 0.5
        remarques.append("Présence d'aliments modérément riches en purines.")

    bons_lipides = {"Avocat", "Amandes", "Graines de courge"}
    if any(a in bons_lipides for a in aliments_selectionnes):
        score += 1
        remarques.append("Présence de bons lipides anti-inflammatoires.")

    alcalinisants = {"Épinards", "Fenouil", "Concombres", "Betteraves", "Courgettes", "Salade verte"}
    if any(a in alcalinisants for a in aliments_selectionnes):
        score += 1
        remarques.append("Présence de légumes alcalinisants, bon pour les reins.")

    fruits_rouges = {"Cerises", "Myrtilles", "Poire", "Pomme"}
    if any(a in fruits_rouges for a in aliments_selectionnes):
        score += 1
        remarques.append("Fruits riches en antioxydants présents.")

    if score >= 3.5:
        conclusion = "Ton repas est bien équilibré et adapté à ton régime."
    elif 2 <= score < 3.5:
        conclusion = "Repas globalement bon, mais quelques ajustements possibles."
    else:
        conclusion = "Ce repas est à modérer en fonction de ton état de santé."

    return conclusion, remarques

if aliments_selectionnes:
    conclusion, remarques = analyse_repas(aliments_selectionnes)
    st.subheader("Conclusion :")
    st.success(conclusion)

    st.subheader("Détails de l'analyse :")
    for remarque in remarques:
        st.markdown(f"- {remarque}")
else:
    st.info("Sélectionne des aliments pour lancer l'analyse.")
