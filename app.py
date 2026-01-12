import streamlit as st
import time
import random

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="BookGENESIS AI",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- ESTILOS CSS (TU IMAGEN DE FONDO) ---
background_url = "https://i.postimg.cc/nLz5g7V8/Book-GENESIS-01-ELEGIDA.png"

st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("{background_url}");
        background-attachment: fixed;
        background-size: contain; background-repeat: no-repeat; background-color: #000000;
        background-position: center;
    }}
    /* Limpieza de interfaz */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    
    /* Títulos con sombra para leerse sobre el espacio */
    h1, h2, h3, p, label, .stMarkdown {{
        color: #ffffff !important;
        text-shadow: 0px 0px 10px rgba(0,0,0,0.8);
    }}
    
    /* Inputs semitransparentes */
    .stTextInput > div > div > input {{
        background-color: rgba(0, 0, 0, 0.5);
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.3);
    }}
    
    /* Botón Mágico */
    .stButton > button {{
        background: linear-gradient(90deg, #4b6cb7 0%, #182848 100%);
        color: white;
        border: none;
        box-shadow: 0 0 15px rgba(75, 108, 183, 0.6);
        font-weight: bold;
        transition: all 0.3s;
    }}
    .stButton > button:hover {{
        transform: scale(1.05);
        box-shadow: 0 0 25px rgba(75, 108, 183, 0.9);
    }}
    
    /* Caja de Resultados (Glassmorphism) */
    .result-box {{
        background-color: rgba(0, 0, 0, 0.75);
        border-radius: 10px;
        padding: 25px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-top: 20px;
    }}
    </style>
""", unsafe_allow_html=True)

# --- INTERFAZ ---
st.markdown("<br>", unsafe_allow_html=True)

# Input del Usuario
topic = st.text_input("Enter your Book Idea or Topic:", placeholder="e.g., A time traveler who changes history...")

# Botón de Generación
if st.button("✨ GENERATE BOOK STRUCTURE", use_container_width=True):
    if topic:
        with st.spinner("Analyzing Concept & Structuring Chapters..."):
            time.sleep(2.5) # Simulación de pensamiento
            
            # Generación Simulada (Templates inteligentes)
            titles = [
                f"The Chronicles of {topic.split()[0] if topic else 'Time'}",
                f"Beyond the {topic.split()[-1] if topic else 'Horizon'}",
                "Echoes of Destiny"
            ]
            selected_title = random.choice(titles) if len(topic) > 5 else "The Untitled Masterpiece"
            
        # Mostrar Resultado
        st.markdown(f"""
        <div class="result-box">
            <h2 style="color: #4da6ff !important;">📖 Generated Blueprint</h2>
            <p><strong>Working Title:</strong> {selected_title}</p>
            <p><strong>Genre:</strong> Speculative Fiction / Drama</p>
            <hr style="border-color: rgba(255,255,255,0.2);">
            <h4>Chapter Outline:</h4>
            <ul>
                <li><strong>Chapter 1: The Spark</strong> - Establishing the world and the inciting incident regarding '{topic}'.</li>
                <li><strong>Chapter 2: The Crossing</strong> - The protagonist faces the first major obstacle.</li>
                <li><strong>Chapter 3: The Revelation</strong> - A secret is uncovered that changes everything.</li>
                <li><strong>Chapter 4: The Climax</strong> - The ultimate confrontation.</li>
                <li><strong>Chapter 5: Resolution</strong> - The new normal is established.</li>
            </ul>
            <br>
            <p style="font-style: italic; opacity: 0.8;">* Full manuscript generation available in Pro Version.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.success("Structure Created Successfully!")
        
    else:
        st.warning("Please enter a topic first.")

# Pie de página
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.caption("BookGENESIS AI - Functional Prototype Demo")
