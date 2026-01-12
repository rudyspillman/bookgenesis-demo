import streamlit as st
import time
import random

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="BookGENESIS AI",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- CSS STYLES (BACKGROUND IMAGE) ---
background_url = "https://i.postimg.cc/nLz5g7V8/Book-GENESIS-01-ELEGIDA.png"

st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("{background_url}");
        background-attachment: fixed;
        background-size: contain; 
        background-repeat: no-repeat; 
        background-color: #000000;
        background-position: center top;
    }}
    /* Clean Interface */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    
    /* Text Styles */
    h1, h2, h3, p, label, .stMarkdown {{
        color: #ffffff !important;
        text-shadow: 0px 0px 10px rgba(0,0,0,0.8);
    }}
    
    /* Input Field Styles (Semi-transparent) */
    .stTextInput > div > div > input {{
        background-color: rgba(0, 0, 0, 0.6);
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.4);
        border-radius: 8px;
    }}
    
    /* Magic Button Style */
    .stButton > button {{
        background: linear-gradient(90deg, #4b6cb7 0%, #182848 100%);
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 8px;
        font-weight: bold;
        transition: all 0.3s;
        width: 100%;
    }}
    .stButton > button:hover {{
        transform: scale(1.02);
        box-shadow: 0 0 20px rgba(75, 108, 183, 0.8);
        border-color: white;
    }}
    
    /* Result Box (Glassmorphism) */
    .result-box {{
        background-color: rgba(0, 0, 0, 0.85);
        border-radius: 12px;
        padding: 25px;
        border: 1px solid rgba(255, 255, 255, 0.15);
        margin-top: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }}
    </style>
""", unsafe_allow_html=True)

# --- USER INTERFACE ---

# 1. Spacer to push controls down (Revealing the Brain Artwork)
st.markdown("<br><br><br><br><br><br><br><br><br><br><br><br><br>", unsafe_allow_html=True)

# 2. Controls Section (Centered and Narrower)
c1, c2, c3 = st.columns([1, 2, 1]) # Column 2 is the center (50% width)

with c2:
    # User Input
    topic = st.text_input("Enter your Book Idea or Topic:", placeholder="e.g., A detective who can read memories...")
    
    st.markdown("<br>", unsafe_allow_html=True)

    # Generation Button
    generate = st.button("✨ GENERATE STRUCTURE")

# 3. Logic & Results
if generate:
    if topic:
        # Progress Bar Simulation (Centered)
        with c2:
            with st.spinner("Analyzing Concept & Structuring Chapters..."):
                time.sleep(2.5) # Simulate processing time
                
                # Dynamic Title Generation Logic
                titles = [
                    f"The Chronicles of {topic.split()[0] if topic else 'Time'}",
                    f"Beyond the {topic.split()[-1] if topic else 'Horizon'}",
                    "Echoes of Destiny",
                    f"The {topic.split()[0]} Paradox"
                ]
                selected_title = random.choice(titles) if len(topic) > 3 else "The Untitled Masterpiece"
            
            st.success("Structure Created Successfully!")

        # Display Result (Full Width for readability)
        st.markdown(f"""
        <div class="result-box">
            <h2 style="color: #4da6ff !important; text-align: center;">📖 Generated Blueprint</h2>
            <p style="text-align: center; font-size: 1.2em;"><strong>Working Title:</strong> {selected_title}</p>
            <p style="text-align: center;"><strong>Genre:</strong> Speculative Fiction / Drama</p>
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
            <p style="font-style: italic; opacity: 0.8; text-align: center; font-size: 0.8em;">* Full manuscript generation available in Pro Version.</p>
        </div>
        """, unsafe_allow_html=True)
        
    else:
        with c2:
            st.warning("Please enter a topic first.")

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; opacity: 0.5; font-size: 0.8rem;'>BookGENESIS AI - Functional Prototype Demo</p>", unsafe_allow_html=True)
