import streamlit as st 
import pandas as pd
import numpy as np
#untuk judul
st.title('SIMPLE VECTOR MATRIX APPS') 


#untuk sidebar
with st.sidebar:
    tipe =  st.radio('pilih tipe', ['single vector', 'double matrix'])

#untuk expander
with st.expander('pilih ukuran'):
    with st.form('pilih ukuran'):
        if tipe == 'single vector':
            size = st.number_input('pilih ukuran dari vektor',min_value=2)
        elif tipe == 'double matrix':
            col1 = st.number_input('pilih baris dari matrix pertama', min_value=2)
            row1 = st.number_input('pilih kolom dari matrix pertama', min_value=2)
            col2 = st.number_input('pilih baris dari matrix kedua', min_value=2)
            row2 = st.number_input('pilih kolom dari matrix kedua', min_value=2)
        st.form_submit_button('kirim ukuran')

#untuk memasukkan angka data
if tipe == 'single vector':
    st.write('data untuk vector')
    #index untuk menentukan banyak baris
    #columns untuk menentukan banyak kolom
    #dtype supaya inputnya berupa angka
    df = pd.DataFrame(columns=range(1, size+1), index=range(1,2), dtype=float) #membuat tabel kosong
    df_input = st.experimental_data_editor(df, use_container_width=True) #untuk masukkan data

elif tipe == 'double matrix':
    st.write('data untuk matrix pertama')
    df1 = pd.DataFrame(columns=range(1, col1+1), index=range(1, row1+1), dtype=float)
    df1_input = st.experimental_data_editor(df1, use_container_width=True, key=1)

    st.write('data untuk matrix kedua')
    df2 = pd.DataFrame(columns=range(1, col2+1), index=range(1, row2+1), dtype=float)
    df2_input = st.experimental_data_editor(df2, use_container_width=True, key=2)

    #untuk menghitung operasi
    operasi = st.radio('pilih operasi', ['A*B', 'A+B'])

    #untuk merubah tabel menjadi matrix
    matrix_1 = df1_input.fillna(0).to_numpy()
    matrix_2 = df2_input.fillna(0).to_numpy()

    if operasi == 'A*B':
        hasil = np.matmul(matrix_1, matrix_2) #untuk perkalian matrix
        st.write(hasil) #untuk menampilkan hasil
    elif operasi == 'A+B':
        hasil = matrix_1 + matrix_2
        st.write(hasil)
