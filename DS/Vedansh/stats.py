import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.dataframe(pd.read_csv(st.file_uploader('Upload csv here')))