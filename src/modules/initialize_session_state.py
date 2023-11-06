import streamlit as st
from src.modules.sheets_api import load_google_sheets_data

def initiatlize_session_dict():
    if "n_players" not in st.session_state:
        st.session_state["n_players"] = 1
    if "questions_df" not in st.session_state:
        st.session_state["questions_df"] = load_google_sheets_data("questions")
    if "question" not in st.session_state:
        st.session_state["question"] = None
    if "question_sampling" not in st.session_state:
        st.session_state["question_sampling"] = 1
    if "random_player" not in st.session_state:
        st.session_state["random_player"] = None
        