import streamlit as st
from datetime import datetime # 파일명 현재시간 조합
from PIL import Image
import pandas as pd
import os  # 파이썬 파일 폴드 작업

# 디렉토리(폴드) 이름정보와 파일을 알려주면, 해당 디렉토리에
# 파일을 저장하는 함수
def save_uploaded_file(directory, file) :
    # 1.디렉토리(폴드)가 있는지 확인하여, 없으면 디렉토리부터만든다.
    if not os.path.exists(directory) : # 이 디렉토리 없니
        os.makedirs(directory) # 없으면 만들어줘
    # 2. 디렉토리가 있으니, 파일을 저장.
    with open(os.path.join(directory, file.name), 'wb') as f :    #wb :write binary
        f.write(file.getbuffer())
    return st.success('파일 저장 완료')
    # return st.success("Saved file : {} in {}".format(file.name, directory)) #return true해도 됨
    


def main():
    st.title('웹 대시보드')

    # 사이드바 만들기 

    menu = ['Image업로드', 'CSV업로드', 'About']
    choice = st.sidebar.selectbox('메뉴', menu)
    if choice == menu[0]:
        # st.title('웹 대시보드')
        st.subheader('이미지 파일 업로드')
        img_file = st.file_uploader('이미지를 업로드 하세요',type=['png', 'jpg', 'jpeg'])
        if img_file is not None : #이미지 파일이 없는게 아니면= 있다면
            print(type(img_file))

            print(img_file.name)
            print(img_file.size)
            print(img_file.type)

            # 유저가 올린 파일을 , 서버에서 유니크하게 처리하기 위해서 
            # 파일명을 현재시간 조합으로 해서 만든다.
            current_time = datetime.now()
            print(current_time)
            print(current_time.isoformat().replace(':', '_') + '.jpg')

            filename = current_time.isoformat().replace(':', '_') + '.jpg'
            img_file.name = filename

            save_uploaded_file('image', img_file)

            st.image('image/'+ filename)

    elif choice == menu[1]:
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
            
    else:
        st.subheader('이 대시보드 설명')

if __name__ =='__main__' :
    main()