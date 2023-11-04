import streamlit as st


def create_sidebar():
    with st.sidebar:
        st.session_state["n_players"] = st.number_input("Number of players", min_value=1, max_value=None, value="min", step=1)