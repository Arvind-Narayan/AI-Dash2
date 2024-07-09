import streamlit as st

st.set_page_config(page_title="Glossary", page_icon="📈")

st.title('📚 Glossary')
st.write('---')

st.subheader('What is the Adobe Digital Price Index?')
st.write(''' The Adobe Digital Price Index (DPI) is a comprehensive measure of inflation in the digital economy, developed by Adobe in partnership with renowned economists. The key points about the Adobe Digital Price Index are:
- It is modeled after the Consumer Price Index (CPI) published by the U.S. Bureau of Labor Statistics, but focuses specifically on tracking online prices rather than offline prices.
- It analyzes over one trillion visits to retail sites and over 100 million product SKUs across 18 different product categories, including electronics, apparel, groceries, and more.
- The index uses the Fisher Price Index methodology to calculate price changes by category, weighting the analysis by the actual quantities of products purchased in adjacent months.
- The DPI is developed in partnership with renowned economists Austan Goolsbee and Pete Klenow, providing expert economic insights.
- It provides the most comprehensive view into how much consumers pay for goods online, complementing the government's CPI which captures offline prices.
         
In summary, the Adobe Digital Price Index is a leading indicator of digital economy inflation, leveraging Adobe's extensive e-commerce data to deliver a more comprehensive and timely measure of online price trends compared to traditional government indexes.
''')

st.subheader('How to interpret the trend lines?')
st.write("The Adobe Digital Price Index (DPI) provides a comprehensive measure of inflation in the digital economy. Here's how to interpret the key information from the DPI:")
st.write('''**Total Inflation**: 
- Measures the overall change in prices of goods sold online relative to the base date, which is Jan 2014 by default
- For instance, the DPI (digital price index) 0.76 in May 2024 implies that online prices in May 2024 was 76% of the prices in Jan 2014. In other words, we saw a defaltion of 24%.
         
**Category Inflation**: 
- Analyzes price changes across 18 different product categories, from electronics to groceries. relative to the base date, which is Jan 2014 by default
- For example, the DPI of 0.41 for electronics showed that prices fell by 59% in May 2024 relative to Jan 2014 ''')

st.subheader('Reference: ')
st.write('https://business.adobe.com/resources/digital-price-index.html')