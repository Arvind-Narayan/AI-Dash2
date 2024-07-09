import streamlit as st
import pandas as pd

def re_index(df, index_date):
    df = df/df.loc[index_date,:]
    return df.sort_values(by='date')

def slider_callback_1():
    start_date1, end_date1 = st.session_state['date_range1']
    st.session_state['start_date1'] = start_date1
    st.session_state['end_date1'] = end_date1

def base_callback_1():
    option = st.session_state['base_select1']
    #update base date
    st.session_state['base_date1'] = option
    st.session_state['start_date1'] = option

def gen_insights1_callback():
    st.session_state['gen_insights1'] = not(st.session_state['gen_insights1'])

#---
def slider_callback_2():
    start_date2, end_date2 = st.session_state['date_range2']
    st.session_state['start_date2'] = start_date2
    st.session_state['end_date2'] = end_date2

def base_callback_2():
    option = st.session_state['base_select2']
    #update base date
    st.session_state['base_date2'] = option
    st.session_state['start_date2'] = option

def gen_insights2_callback():
    st.session_state['gen_insights2'] = not(st.session_state['gen_insights2'])

def multiselect_callback():
    datasets = st.session_state['dataset_select']
    st.session_state['multiselect_items'] = datasets

def initialize_state(topline_Inflation, cumulative_inflation_by_category):
    if 'base_date1' not in st.session_state:
        st.session_state['base_date1'] = topline_Inflation.index[0]

    if 'start_date1' not in st.session_state:
        st.session_state['start_date1'] = topline_Inflation.index[0]

    if 'end_date1' not in st.session_state:
        st.session_state['end_date1'] = topline_Inflation.index[-1]

    if 'gen_insights1' not in st.session_state:
        st.session_state['gen_insights1'] = False

    if 'ai_insights1' not in st.session_state:
        st.session_state['ai_insights1'] = ''
    #---
    if 'base_date2' not in st.session_state:
        st.session_state['base_date2'] = cumulative_inflation_by_category.index[0]

    if 'start_date2' not in st.session_state:
        st.session_state['start_date2'] = cumulative_inflation_by_category.index[0]

    if 'end_date2' not in st.session_state:
        st.session_state['end_date2'] = cumulative_inflation_by_category.index[-1]

    if 'gen_insights2' not in st.session_state:
        st.session_state['gen_insights2'] = False

    if 'ai_insights2' not in st.session_state:
        st.session_state['ai_insights2'] = ''
    
    if 'openai_api_key' not in st.session_state:
        st.session_state['openai_api_key'] = ''
        
def get_data():
    ## read files:
    cumulative_inflation_by_category = pd.read_csv('./data_packet/cumulative_inflation_by_category.csv')
    topline_Inflation = pd.read_csv('./data_packet/topline_Inflation.csv')

    #prep data
    cumulative_inflation_by_category = cumulative_inflation_by_category.rename(columns = {'Unnamed: 0' : 'date'})
    cumulative_inflation_by_category = cumulative_inflation_by_category.set_index('date')

    topline_Inflation = topline_Inflation.reset_index()
    topline_Inflation = topline_Inflation.rename(columns = {'month' : 'date'})
    topline_Inflation = topline_Inflation.set_index('date')
    topline_Inflation = topline_Inflation.drop(columns=['index'])
    topline_Inflation = topline_Inflation + 1

    return topline_Inflation, cumulative_inflation_by_category