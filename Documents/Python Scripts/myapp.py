import streamlit as st
import pandas as pd
import dtale
from pandas_profiling import ProfileReport
import sweetviz as sv
from streamlit.components.v1 import components
from streamlit_pandas_profiling import st_profile_report

st.title("Automated EDA by profiling")

def display_sweetviz(report_html, width=1000, height=800):
    report_file = open(report_html, 'r')
    page = report_file.read()
    # components.html(page, width=width, height=height, scrolling=True)

def main():    
    menu = ['Pandas-Profiling', 'SweetViz', 'D-tale', 'About']
    option = st.sidebar.selectbox("Menu", menu)

    if option == 'Pandas-Profiling':
        st.header("Pandas-Profiling")
        data_file = st.file_uploader("Upload_csv", type=['csv'])
        if data_file is not None:
            load_csv = pd.read_csv(data_file)
            st.write(load_csv)
            if st.button('Generate Report'):
                report = ProfileReport(load_csv, title = "CSV Profiling Report", explorative=True)
                st.write('---')
                st.header('**Pandas Profiling Report**')
                st_profile_report(report)

    elif option == 'SweetViz':
        st.header("SweetViz")
        data_file = st.file_uploader("Upload_csv", type=['csv'])
        if data_file is not None:
            load_csv = pd.read_csv(data_file)
            st.write(load_csv)
            st.write('---')
            st.header('**SweetViz Profiling Report**')
            if st.button('Generate Report'):
                report = sv.analyze(load_csv)
                report.show_html()
                display_sweetviz("SWEETVIZ_REPORT.html")

    elif menu=='About':
        st.subheader("Simple tool for better and quick visualization and EDA!!")
        st.write()
        # components.iframe('https://www.youtube.com/watch?v=zWiliqjyPlQ')


if __name__ == '__main__':
    main()