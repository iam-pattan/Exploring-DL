import streamlit as st
import pandas as pd
import dtale
from pandas_profiling import ProfileReport
import sweetviz as sv
import streamlit.components.v1 as components
from PIL import Image
from streamlit_pandas_profiling import st_profile_report
import matplotlib.pyplot as plt

st.title("""
Automated EDA in Python 
Using Pandas-Profiling, SweetViz, Dtale""")
img2 = Image.open("./dtale.jpg")
img = Image.open("./pprof.png")
img1 = Image.open("./sweetviz.jpeg", mode="r")
col1, col2, col3 = st.beta_columns(3)
col1.image(img, width=100)
col2.image(img1, width=100)
col3.image(img2, width=100)

def display_sweetviz(report_html, width=1500, height=800):
    report_file = open(report_html, 'r')
    page = report_file.read()
    components.html(page, width=width, height=height, scrolling=True)

def main():    
    menu = ['Pandas-Profiling', 'SweetViz', 'D-tale', 'About']
    option = st.selectbox("Select Tool for Viz", menu)

    if option == 'Pandas-Profiling':
        st.header("Pandas-Profiling")
        data_file = st.file_uploader("Upload_csv", type=['csv'])
        if data_file is not None:
            load_csv = pd.read_csv(data_file)
            st.write(load_csv.head())
            st.success("Successfully uploaded!")
            if st.button('Generate Report'):
                report = ProfileReport(load_csv, title = "CSV Profiling Report", explorative=True)
                st.write('---')
                st.header('**Pandas Profiling Report**')
                st_profile_report(report)

    elif option == 'SweetViz':
        st.header("SweetViz")
        data_file = st.file_uploader("Upload_csv", type=['csv'])
        st.success("Successfully uploaded!")
        if data_file is not None:
            load_csv = pd.read_csv(data_file)
            st.write(load_csv)
            st.write('---')
            st.header('**SweetViz Profiling Report**')
            if st.button('Generate Report'):
                report = sv.analyze(load_csv)
                report.show_html()
                display_sweetviz("SWEETVIZ_REPORT.html")
        
    elif option == 'D-tale':
        st.header('D-tale')
        data_file = st.file_uploader("Upload_csv", type=['csv'])
        st.success("Successfully uploaded!")
        if data_file is not None:
            load_csv = pd.read_csv(data_file)
            st.write(load_csv)
            st.write('---')
            st.header('**D-Tale Profiling Report**')
            if st.button('Generate Report'):
                dtale.show(load_csv)
                components.iframe('http://dell-virlgti:40000/dtale/main/1', 
                                    width=1500, height=800, scrolling=True)
                # st.markdown(html, unsafe_allow_html=True)    

    elif menu=='About':
        st.subheader("Simple tool for better and quick visualization and EDA!!")
        st.write()
        st.write("check out this [link](https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py)")


if __name__ == '__main__':
    main()