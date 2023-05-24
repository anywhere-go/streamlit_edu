import os
import streamlit as st


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