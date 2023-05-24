import pandas as pd
import streamlit as st
from datetime import datetime
from app_utils import save_uploaded_file


def run_app_csv():
    st.subheader('CSV 파일 업로드')

    csv_file = st.file_uploader('CSV 파일 업로드', type= ['csv'])
    if csv_file is not None :

        # 파일명을 유니크하게 만들어서 저장해야 한다.
        # 현재시간을 활용해서, 파일명을 만든다. 
        current_time = datetime.now()
        print(current_time.isoformat().replace(':', '_'))

        filename = current_time.isoformat().replace(':', '_') + '.csv'
        csv_file.name = filename
        save_uploaded_file('csv', csv_file)

        df = pd.read_csv('csv/' +filename)
        st.dataframe(df)