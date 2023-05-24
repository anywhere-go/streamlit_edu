import streamlit as st

# 이미지 처리를 위한 라이브러리
from PIL import Image

def main():
    st.title('웹 대시보드')
    img = Image.open('data/image_03.jpg')

    print(img)
    #사진과 영상
    st.image(img)

    st.image(img, use_column_width=True) #옆으로 꽉차게 보여주세요
    
    # 2. 인터넷상에 있는 이미지를 화면에 표시하기.
    #URL이 있는 이미지를 말한다.

    st.image('https://cdn.epnc.co.kr/news/photo/201907/91021_81259_3048.jpg')

    video_file = open('data/video1.mp4', 'rb') #'rb': 바이너리 파일을 읽어주세요
    st.video(video_file)

if __name__ == '__main__' :
    main()
