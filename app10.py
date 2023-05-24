import streamlit as st
import plotly.express as px
import altair as alt
import pandas as pd

def main():
    st.title('웹 대시보드')

    df1 = pd.read_csv('data/lang_data.csv')
    st.dataframe(df1)

    # st.text(df1.shape)
    st.write(df1.shape)

    print(df1.columns[1:])

    lang_list = df1.columns[1:]

    choice_list = st.multiselect('언어를 선택하세요', lang_list)

    #유저가 아무것도 선택 안했을 때 처리

    print(choice_list)  # 터미널 실행 하면 []

    if len(choice_list) > 0:

        choice_df = df1[choice_list]

        st.dataframe(choice_df)

        # 스트림릿이 제공하는 라인차트
        st.line_chart(choice_df)

        # 스트림릿이 제공하는 영역차트
        st.area_chart(choice_df)

    df2= pd.read_csv('data/iris.csv')

    # 스트림릿이 제공하는 bar 차트
    df3 = df2[['sepal_length', 'sepal_width']]
    st.bar_chart(df3)

    # Altair
    chart = alt.Chart(df2).mark_circle().encode(
        x='petal_length', #꽃잎 길이
        y='petal_width', #꽃잎 넓이
        color ='species'
    )
    st.altair_chart(chart) #웹에 표시하는 altair 방법

    chart2 = alt.Chart(df2).mark_boxplot().encode(
        x='petal_length', #꽃잎 길이
        y='petal_width', #꽃잎 넓이
        color ='species'
    )
    st.altair_chart(chart2) #웹에 표시하는 altair 방법

    # 스트림릿의 map 차트
    df4 = pd.read_csv('data/location.csv', index_col=0)
    print(df4)

    # st.map(df4, 5)
    st.map(df4)

    df5 = pd.read_csv('data/prog_languages_data.csv', index_col=0)
    st.dataframe(df5)

    # plotly의 pie 차트(비율을 보고 싶을 때 사용)
    # fig1 = px.pie(df5, 'lang', 'Sum')
    fig1 = px.pie(df5, 'lang', 'Sum', title='각 언어의 비율')
    st.plotly_chart(fig1)

    # plotly의 bar 차트
    df6= df5.sort_values('Sum', ascending=False) #데이터 가공
    fig2 = px.bar(df6, x='lang', y='Sum')
    st.plotly_chart(fig2)

if __name__ =='__main__' :
    main()    