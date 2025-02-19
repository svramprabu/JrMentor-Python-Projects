import streamlit as st
import numpy as np

st.title("Numpy using streamlit")
# data = st.text_input('Enter data: ').split()
# data = list(map(int,data))
# for i,each in enumerate(data):
#     data[i] = int(each)
# np_data = np.array(data)
# st.write(np_data)
# st.write(np_data.dtype)
#
# st.button()
st.selectbox('Choose an option',('horizontal','vertical'))