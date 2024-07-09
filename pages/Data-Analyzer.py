import streamlit as st
import pandas as pd
import plotly.express as px
import agent
from utils import *
from openai import OpenAI

st.set_page_config(page_title="AI Data Analyzer", page_icon="📈")

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    if openai_api_key:
        st.session_state['openai_api_key'] = openai_api_key


if 'analyzer_assist' not in st.session_state:
        st.session_state['analyzer_assist'] = ''

if 'analyzer_thread' not in st.session_state:
        st.session_state['analyzer_thread'] = ''

if 'analyzer_text' not in st.session_state:
        st.session_state['analyzer_text'] = ''

if 'analyzer_img' not in st.session_state:
        st.session_state['analyzer_img'] = ''

if 'multiselect_items' not in st.session_state:
        st.session_state['multiselect_items'] = []

if 'selection_option' not in st.session_state:
        st.session_state['selection_option'] = ''

st.title('📈 AI Data Analyzer')
st.write('---')

datasets = st.multiselect(
    label = "Datasets you want to analyze",
    options = ["Total_Inflation", "Category_Inflation"],
    default = st.session_state['multiselect_items'],
    on_change = multiselect_callback,
    key = 'dataset_select') # need to handle deafult state

topline_Inflation, cumulative_inflation_by_category = get_data()

with open('instruction.txt', 'r') as file:
    instruction_prompt = file.read()


selection_option = ''
df_list = []

if len(datasets) == 1:
    if datasets[0] == 'Total_Inflation':
        selection_option = 'Total_Inflation'
        df_list.append(topline_Inflation)
    elif datasets[0] == 'Category_Inflation':
        selection_option = 'Category_Inflation'
        df_list.append(cumulative_inflation_by_category)
elif len(datasets) == 2:
    selection_option = 'Category_Total'
    df_list.append(topline_Inflation)
    df_list.append(cumulative_inflation_by_category)

query = st.text_area(
    "Analysis query:",
    )


if st.button(':green[Submit]'):
    if st.session_state['openai_api_key']:
        openai_api_key = st.session_state['openai_api_key']

        with st.spinner("Generating response..."):

            if not datasets:
                st.info('Please select dataset')

            if not query:
                st.info('Please submit a query')

            if query and datasets:
                try:
                    client = OpenAI(api_key = openai_api_key)
                    if st.session_state['selection_option'] != selection_option:
                            
                           assistant, thread = agent.create_assistant(client, instruction_prompt, df_list)
                           st.session_state['analyzer_assist'] = assistant.id
                           st.session_state['analyzer_thread'] = thread.id
                           st.session_state['selection_option'] = selection_option
                
                # get ai analysis
                    st.session_state['analyzer_text'], st.session_state['analyzer_img'] = agent.get_analysis(client, thread_id = st.session_state['analyzer_thread'], 
                                                    assist_id = st.session_state['analyzer_assist'],
                                                    query = query)
                except Exception as e:
                    # st.write(e)
                    st.error('Sorry something went wrong. Please try again later')
    else:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

if st.session_state['analyzer_img']:
        st.image(st.session_state['analyzer_img'])

if st.session_state['analyzer_text']: 
        st.markdown(st.session_state['analyzer_text'])
                