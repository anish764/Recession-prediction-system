import streamlit as st # type: ignore
import pandas as pd
import numpy as np
import openpyxl
import time
import xlrd

st.set_page_config(layout="wide")
st.write('#')
st.markdown("""
<style>
.big-font {
    font-size:100px !important;
    font-align:center; !important;
    }
.small-font{
    font-size:20px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">Recession Prediction India   🇮🇳</p>', unsafe_allow_html=True)

left_column, right_column = st.columns([0.6,0.4])
with left_column:
    st.subheader("A recession is a significant decline in economic activity that lasts for an extended period. It's usually marked by a drop in Gross Domestic Product (GDP), which is the total value of goods and services produced in a country. During a recession, there's often a decrease in consumer spending, business investment, and employment. This can lead to businesses producing less, people losing their jobs, and overall economic hardship.")
with right_column:
    st.image('Recession-removebg.png',width=500)

st.header("")
st.header("")
st.header("")

st.markdown("<p class='small-font'>Lets analyse India's GDP and unemployment rate</p>", unsafe_allow_html=True)

# Add a slider to the sidebar:
add_slider = st.slider(
    'Select a range of values',
    1963, 2024, (1990, 2024),1
)

data_raw=pd.read_excel("dataset/gdp_unemp_raw.xlsx")

gdp_data = data_raw[["Year","GDP"]]
unemp_data=data_raw[["Year","Unemployment"]]

gdp_show=gdp_data[(gdp_data["Year"]>=add_slider[0])&(gdp_data["Year"]<=add_slider[1])]
unemp_show=unemp_data[(unemp_data["Year"]>=1989)&(unemp_data["Year"]>=add_slider[0])&(unemp_data["Year"]<=add_slider[1])]

left, right = st.columns(2)
with left:
    st.markdown('<p class="small-font">GDP per capita of India (US dollars)</p>', unsafe_allow_html=True)
    st.line_chart(data=gdp_show,x="Year",y="GDP")
with right:
    st.markdown('<p class="small-font">Unemployment Rate of India (Percentage of labor force)</p>', unsafe_allow_html=True)
    st.line_chart(data=unemp_show,x="Year",y="Unemployment")


st.markdown("<h1 style='text-align: center;'>But when does recession occur ?</h1>", unsafe_allow_html=True)
left2,right2=st.columns([0.6,0.4],gap="large")
with left2:
    df = pd.DataFrame(data={'GDP':[20,25,10,-35,-20,0,15,30],"Unemployment":[-30,-35,-15,37,3,-7,-20,-25]})
    st.line_chart(df)
with right2:
    st.subheader("A recessions takes place when there is a decline in the country's economy. This can be easily observed with a dip in the GDP and an increase in the country's unemployment rate.")

st.header("Now in order to predict future recessions we need to forecast GDP and unemployment data")
st.markdown("<p class='small-font'>For this purpose we use <a href='https://en.wikipedia.org/wiki/Convolutional_neural_network'>Convolutional Neural Networks.</a> Instead of actual gdp values we use % chage to easily see the variations</p>", unsafe_allow_html=True)

# Add a selectbox to the sidebar:
add_selectbox = st.selectbox(
    'Forecast -',
    ('GDP change in %', 'Unemployment change in %')
)

gdp_final=pd.read_excel("dataset/test.xlsx")
unemp_final=pd.read_excel("dataset/test2.xlsx")
both_final=pd.read_excel("dataset/both.xlsx")

res=st.button('Generate')
if res==True:
    with st.status("Predicting...", expanded=True) as status:
        st.write("Downloading data")
        time.sleep(2)
        st.write("Making models")
        time.sleep(1)
        st.write("Plotting data")
        time.sleep(1)
        status.update(label="Prediction complete!", state="complete", expanded=False)
    if add_selectbox=="GDP change in %":
        st.line_chart(data=gdp_final,x="Year",y=['Old','Predicted'],color=["#0068c9","#4be4ff"])
    else:
        st.line_chart(data=unemp_final,x="Year",y=['Old','Predicted'],color=["#ff2b2b","#ffd16a"])

flag=st.button("Plot both")
if flag==True:
    st.line_chart(data=both_final,x="Years",y=['GDP_Old','GDP_Predicted','Unemp_Old','Unemp_Predicted'],color=["#0068c9","#4be4ff","#ff2b2b","#ffd16a"])
    st.subheader("From the plot we can see that there is a chnace of recession between 2027 and 2032")

