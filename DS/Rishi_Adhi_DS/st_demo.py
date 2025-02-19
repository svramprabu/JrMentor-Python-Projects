import streamlit as st
import numpy as np

def main():
    operation = st.selectbox('Choose an option',['Addition','Multiplication'])
    if operation == "Addition":
        Addition()

def option(operation):
    st.write("You chose", operation,"operation")
def Addition():
    a = st.text_input('Enter a Values').split()
    b = st.text_input('Enter b values').split()
    a = np.array(a,dtype=int)
    b = np.array(b,dtype=int)
    ans = np.add(a,b)
    st.write(ans)

if __name__ == "__main__":
    main()
