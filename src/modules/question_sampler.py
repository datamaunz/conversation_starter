import pandas as pd
import streamlit as st

def sample_random_question(df):

    random_row = df.sample(n=1)
    st.session_state["question"] = random_row["questions"].iloc[0]
    
        