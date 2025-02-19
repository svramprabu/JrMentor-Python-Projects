import streamlit as st
from scipy import constants as c


def main():

    st.title('Force Finder')
    st.subheader('Between two objects')

    m = st.number_input('Mass of object 1 (kg): ',step=1.0,min_value=0.0)
    M = st.number_input('Mass of object 2 (kg): ',step=1.0,min_value=0.0)
    d = st.number_input('Distance between objects (m): ',step=1.0,min_value=0.0)
    g = st.text_input('Gravitational Constant',
                      value=c.gravitational_constant,
                      disabled=True)
    g = float(g)
    st.button('Calculate Force',on_click=force,args=(m,M,d,g))

def force(m,M,d,g):
    f = ( g * m * M ) / (d ** 2)
    st.text(f"{f}N")

main()





def main():
    pass
if __name__ == '__main__':
    main()




















