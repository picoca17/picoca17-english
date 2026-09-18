import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="picoca17 - English Academy",
    page_icon="🇬🇧",
    layout="centered"
)

# Estilos visuales personalizados
st.markdown("""
    <style>
    .main-title { font-size: 3rem; color: #6c5ce7; text-align: center; font-weight: bold; }
    .sub-title { font-size: 1.2rem; text-align: center; color: #555; }
    .phrase-box { background-color: #ffeaa7; padding: 15px; border-radius: 10px; border-left: 6px solid #fdcb6e; margin-bottom: 20px; color: #2d3436; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">picoca17 🇬🇧 ✨</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Aprende inglés de forma dinámica, motivadora y aprueba tus exámenes de la EOI</div><br>', unsafe_allow_html=True)

# Menú interactivo de selección de nivel EOI
level = st.selectbox(
    "Elige tu nivel de inglés EOI:",
    ["Nivel A1", "Nivel A2", "Nivel B1", "Nivel B2", "Nivel C1", "Nivel C2"]
)

# Base de datos
data = {
    "Nivel A1": {
        "phrase": "Cheer up! Every step counts.",
        "spelling": ["ENGLISH", "TEACHER", "WELCOME"],
        "reading": "Read the short email from Sarah and identify her job.",
        "mediation": "Traduce o adapta este mensaje corto para tu compañero en español.",
        "video": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    },
    "Nivel A2": {
        "phrase": "You are doing great! Keep going.",
        "spelling": ["SCHOOL", "STUDENT", "LESSON"],
        "reading": "Read the notice board and answer the questions.",
        "mediation": "Resume la información del folleto de la escuela para tu amigo.",
        "video": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    },
    "Nivel B1": {
        "phrase": "You are very welcome! Practice makes progress.",
        "spelling": ["TRAVEL", "EXPERIENCE", "KNOWLEDGE"],
        "reading": "Read the travel blog and complete the gap fill.",
        "mediation": "Explica la normativa de la biblioteca a tu compañero de intercambio.",
        "video": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    },
    "Nivel B2": {
        "phrase": "Thank you very much indeed for your hard work!",
        "spelling": ["ACCOMMODATION", "ENVIRONMENT", "MEDIATION"],
        "reading": "Read the article about sustainable living and answer the multiple-choice questions.",
        "mediation": "Examine the chart below and summarize the key trends for your study partner.",
        "video": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    },
    "Nivel C1": {
        "phrase": "Brilliant work! Expressing complex ideas with confidence.",
        "spelling": ["SUBSTANTIAL", "CONSIDERABLE", "FLUCTUATE"],
        "reading": "Analyze the academic paper excerpt and identify nuances.",
        "mediation": "Synthesize the main arguments of two articles for a panel debate.",
        "video": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    },
    "Nivel C2": {
        "phrase": "Congratulations! You are operating at native-like mastery.",
        "spelling": ["UNPRECEDENTED", "CONSCIENTIOUS", "ONOMATOPOEIA"],
        "reading": "Analyze the opinion piece on artificial intelligence and identify implicit attitudes.",
        "mediation": "Synthesize two conflicting opinion pieces into a cohesive 150-word summary.",
        "video": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    }
}

current_data = data[level]

st.divider()

# Mensaje motivador de picoca17
st.markdown(f'<div class="phrase-box"><strong>Message from picoca17:</strong> "{current_data["phrase"]}"<br><br><em>You are very welcome to practice as much as you need!</em></div>', unsafe_allow_html=True)

# Sección Spelling Bee
st.subheader("🔤 Spelling Bee Challenge (Deletreando)")
st.write("Practica deletreando estas palabras clave para la EOI:")
for word in current_data["spelling"]:
    spelled = " - ".join(list(word))
    st.write(f"👉 **{word}**: `{spelled}`")

st.divider()

# Sección Reading & Comprehension
st.subheader("📖 Reading & Comprehension")
st.info(current_data["reading"])

# Sección Mediación (EOI)
st.subheader("🔄 Mediación (EOI Skill)")
st.warning(current_data["mediation"])

# Sección Video / Listening
st.subheader("🎧 Listening & Video Section")
st.video(current_data["video"])

# Pie de página
st.divider()
st.caption("picoca17 English Academy © 2026 | Thank you very much indeed for visiting!")
    
