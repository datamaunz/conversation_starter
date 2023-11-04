import streamlit as st
import pandas as pd
from st_clickable_images import clickable_images

from src.modules.sheets_api import load_google_sheets_data, append_google_sheets_row
from src.modules.initialize_session_state import initiatlize_session_dict
from src.modules.question_sampler import sample_random_question
from src.modules.sidebar import create_sidebar

initiatlize_session_dict()

@st.cache_data
def create_star_choice_options(n_players):
    return [" ".join(['⭐️']*i) for i in range(st.session_state["n_players"]+1)]

def main():
    st.set_page_config(layout="centered",
                       page_title="Conversation Starter",
                       page_icon = '💡')

    st.title("Conversation Starter")
    st.divider()
    create_sidebar()
    questions_df = st.session_state["questions_df"]
    
    col1, col2, col3,col4, col5 = st.columns(5)
    
    sample_button = col3.button("🎰 Select new question")
    
    
    #image_path = "https://i.insider.com/5c79a8cfeb3ce837863155f5?width=1000&format=jpeg&auto=webp"
    #clicked = clickable_images(
    #    [
    #        image_path
    #    ],
    #    titles=["generate new question"],
    #    div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
    #    img_style={"margin": "5px", "height": "200px"},
    #)
    #st.write(clicked)
    
    #st.help(clickable_images)
    
    if sample_button:
        sample_random_question(questions_df)

    
    st.divider()
    
    col1, col2, col3 = st.columns([0.2,0.6,0.2])
    col2.info(f"### {st.session_state['question']}")
    
    st.divider()
    #st.info(st.session_state['question'])
    
    options = create_star_choice_options(st.session_state["n_players"])
    rating = st.select_slider('Select number of upvotes', options)
    
    rating_sumbit_button = st.button("Submit your rating")
    if rating_sumbit_button:
        new_data = pd.DataFrame({
            "question":[st.session_state["question"]],
            "rating":[str(len(rating.split()))],
            "participants":[str(st.session_state["n_players"])]
        })
        append_google_sheets_row("ratings", new_data.iloc[0])
        st.success("Rating successfully submitted")

if __name__ == '__main__':
    main()
    
    