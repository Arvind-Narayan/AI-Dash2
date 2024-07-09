import streamlit as st
import pandas as pd
import plotly.express as px
import agent
from utils import *

st.set_page_config(page_title="AI Dashboard", page_icon="📈")

## read files:
topline_Inflation, cumulative_inflation_by_category = get_data()

## initialize state
initialize_state(topline_Inflation, cumulative_inflation_by_category)

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    if openai_api_key:
        st.session_state['openai_api_key'] = openai_api_key

st.title('Adobe Digital Price Index')
st.write('---')

# Graph 1
col_1, col_2 = st.columns([0.75,0.25], vertical_alignment="bottom")
col_1.subheader('Total Online Inflation')
with col_2:
    option = st.selectbox(label = 'Base Date', options = list(topline_Inflation.index), 
                        index = list(topline_Inflation.index).index(st.session_state['base_date1']),
                        placeholder = topline_Inflation.index[0],
                        key = 'base_select1',
                        on_change = base_callback_1
                        )

df1 = re_index(topline_Inflation,option)
df1 = df1.loc[st.session_state['start_date1'] : st.session_state['end_date1'],:]
fig1 = px.line(df1)
st.plotly_chart(fig1, use_container_width = True)

#Date slider
start_date1, end_date1 = st.select_slider(
    label = 'date range',
    options=list(topline_Inflation.index),
    value=(st.session_state['start_date1'], st.session_state['end_date1']),
    key = 'date_range1',
    label_visibility = 'collapsed',
    on_change = slider_callback_1
    )

col_a, col_b, col_c = st.columns([0.5,0.2,0.3], vertical_alignment="bottom") #st.columns([0.3,0.5,0.3])

if col_a.checkbox("show raw data", key = 'checkbox1'):
    st.write(df1)

if not st.session_state['gen_insights1']: 
    col_c.button("Generate insights", use_container_width=True, on_click=gen_insights1_callback, key = 'button_gen1')
else:
    col_c.button("Clear", use_container_width=True, on_click=gen_insights1_callback, key = 'button_clear1')

if st.session_state['gen_insights1']:
    with st.spinner("Generating insights..."): 
        if st.session_state['ai_insights1']:
                with st.expander("✨AI Insights"):
                    st.write(st.session_state['ai_insights1'])
        else:
            try:
                description = f'The data provided contains total online inflation over time, indexed to {st.session_state['base_date1']}.\
                    Please generate interesting insights' 
                st.session_state['ai_insights1'], result = agent.get_insights(df1, description)
                with st.expander("✨AI Insights"):
                    st.write(st.session_state['ai_insights1'])
            except Exception as e:
                st.write(e)
                st.write('⛔ Sorry there was a problem. Try again later')
else: 
    st.session_state['ai_insights1'] = ''

#--------------------------------------------------------------------------------------------------------------
st.write('---')
# Graph 2
col_3, col_4 = st.columns([0.75,0.25], vertical_alignment="bottom")
col_3.subheader('Inflation by Category')
with col_4:
    option2 = st.selectbox(label = 'Base Date', options = list(cumulative_inflation_by_category.index), 
                        index = list(cumulative_inflation_by_category.index).index(st.session_state['base_date2']),
                        placeholder = cumulative_inflation_by_category.index[0],
                        key = 'base_select2',
                        on_change = base_callback_2
                        )

df2 = re_index(cumulative_inflation_by_category,option2)
df2 = df2.loc[st.session_state['start_date2'] : st.session_state['end_date2'],:]
fig2 = px.line(df2)
st.plotly_chart(fig2, use_container_width = True)

#Date slider
start_date2, end_date2 = st.select_slider(
    label = 'date range',
    options=list(cumulative_inflation_by_category.index),
    value=(st.session_state['start_date2'], st.session_state['end_date2']),
    key = 'date_range2',
    label_visibility = 'collapsed',
    on_change = slider_callback_2
    )

col_x, col_y, col_z = st.columns([0.5,0.2,0.3], vertical_alignment="bottom") #st.columns([0.3,0.5,0.3])

if col_x.checkbox("show raw data", key = 'checkbox2'):
    st.write(df2)

if not st.session_state['gen_insights2']: 
    col_z.button("Generate insights", use_container_width=True, on_click=gen_insights2_callback, key = 'button_gen2')
else:
    col_z.button("Clear", use_container_width=True, on_click=gen_insights2_callback, key = 'button_clear2')

if st.session_state['gen_insights2']:
    with st.spinner("Generating insights..."):
        if st.session_state['ai_insights2']: 
                with st.expander("✨AI Insights"):
                    st.write(st.session_state['ai_insights2'])
        else:
            try:
                description = f'The data in the file contains online inflation by product category over time, indexed to {st.session_state['base_date2']}.\
                    Please generate interesting insights' 
                st.session_state['ai_insights2'], result = agent.get_insights(df2, description)
                with st.expander("✨AI Insights"):
                    st.write(st.session_state['ai_insights2'])
            except:
                st.write('⛔ Sorry there was a problem. Try again later')
else: 
    st.session_state['ai_insights2'] = ''