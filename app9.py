import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



def main():
    st.title('웹 대시보드')

    df = pd.read_csv('data/iris.csv')
    st.dataframe(df)

    #sepal_length, sepal_width (꽃받침의 길이 넓이의 관계를 차트로 알고 싶다)
    fig = plt.figure()
    plt.scatter(data=df, x='sepal_length', y='sepal_width')
    plt.title('sepal length vs width')
    plt.xlabel('sepal length')
    plt.ylabel('sepal width')
    st.pyplot(fig)

    fig2 = plt.figure()
    sns.regplot(data=df, x='sepal_length', y = 'sepal_width')
    st.pyplot(fig2)

    correlation = df[['sepal_length', 'sepal_width']].corr()
    st.dataframe(correlation)

    #sepal_length로 히스트그램 그리자
    #bin 의 갯수 20

    fig3 = plt.figure(figsize=(10,4))
    plt.subplot(1, 2, 1)
    plt.hist(data=df, x='sepal_length', bins=10,
                rwidth=0.8)

    plt.subplot(1, 2, 2)
    plt.hist(data=df, x='sepal_length', bins=20,
                rwidth=0.8)
    st.pyplot(fig3)


    #species 컬럼에는 종에 대한 정보가 들어있는데,
    #각 종별로 몇개씩의 데이터가 있는지 차트로 표시

    st.dataframe(df['species'].value_counts())

    fig4 = plt.figure()
    sns.countplot(data=df, x ='species')
    st.pyplot(fig4)

    #데이터프레임의 차트 그리는 
    fig5 = plt.figure()
    df['species'].value_counts().plot(kind='bar') #barh 수평
    st.pyplot(fig5)

    #데이터프레임 자체 plot 함수는 스트림릿에서는 실행 안 된다
    # fig6 = plt.figure()
    # df.plot()
    # st.pyplot(fig6)

    fig7 = plt.figure()
    df['sepal_length'].hist()
    st.pyplot(fig7)



if __name__ =='__main__' :
    main()