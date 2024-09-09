import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
st.title('Belajar Analisis Data')

st.header('Pengembangan Dashboard')

st.write(
    """
    # My first app
    Hello, para calon praktisi data masa depan!
    """
)

df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})

st.metric(label="Temperature", value="28 °C", delta="1.2 °C")

st.dataframe(data=df, width=500, height=150)

code = """def hello():
    print("Hello, Streamlit!")"""
st.code(code, language='python')

st.latex(r"""
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
""")

x = np.random.normal(15, 5, 250)
 
fig, ax = plt.subplots()
ax.hist(x=x, bins=15)
st.pyplot(fig)

st.caption('Copyright (c) 2023')