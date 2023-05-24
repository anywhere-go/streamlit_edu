import streamlit as st
import pandas as pd


def main():
    st.title('웹 대시보드')

    df = pd.read_csv('data/iris.csv')

    # 버튼 만들기
    # st.button('버튼')
    if st.button('데이터 보기'):
        st.dataframe(df)

    name = 'Mike'
    #대문자 버튼을 누르면, 대문자로 표시
    #소문자 버튼을 누르면, 소문자로 표시
    if st.button('대문자'):
        st.text(name.lower())
    if st.button('소문자'):
        st.text(name.upper())

    st.dataframe(df)

    #petal_length 컬럼을 정렬하고 싶다
    #오름차순정렬, 내림차순정렬 두가지 옵션 선택

    status = st.radio('정렬을 선택하세요',['오름차순','내림차순'])
    print(status)
    if status =='오름차순':
       st.dataframe( df.sort_values('petal_length'))
    elif status =='내림차순':
       st.dataframe (df.sort_values('petal_length', ascending=False))

    #checkbox
    if st.checkbox('데이터프레임 보이기'):
        st.dataframe(df.head(3))
    else:
        st.write('데이터가 없습니다.')

    # 여러개 중에 1개를 선택
    language = ['Python', 'Java', 'C', 'Go', 'PHP']
    selected_lang = st.selectbox('선호하는 언어를 선택!', language)
    if selected_lang == 'Python':
        st.text('파이썬이 최고지')
    elif selected_lang == 'Java':
        st.text('클레스가 좀 어렵지')
    elif selected_lang == 'C':
        st.text('문법이 좀 어렵지')
    elif selected_lang == 'Go':
        st.text('구글에서 만들었지')
    else:
        st.text('PHP는 멋지지')

    # 멀티셀렉트 : 여러개 중에서, 여러개 선택하는 UI
    # st.multiselect('여러개 선택가능', language)
    
    column_list = st.multiselect('컬럼을 선택하세요', df.columns)

    # 멀티셀렉트를 이용해서, 특정 컬럼들만 가져오기.
    # 유저에게, iris df의 컬럼들을 다 보여주고,
    # 유저가 선택한 컬럼들만, 데이터프레임을 화면에 보여줄것!
    st.dataframe(df[column_list])

    # 슬라이더 :  숫자 조정하는데 주로 사용 
    #st.slider('나이', min_value=30, step =10, value= 50)
    age = st.slider('나이', min_value=30, max_value=110, value= 50)
    st.text('나이는' + str(age) + '입니다.')

    # 익스펜더 
    with st.expander('Hello') :
        st.text('안녕하세요')



if __name__ =='__main__' :
    main()