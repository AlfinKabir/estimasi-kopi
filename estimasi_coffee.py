import pickle
import streamlit as st

model = pickle.load(open('estimasi_coffee.sav', 'rb'))

st.title('Estimasi Harga Kopi')

Open = st.number_input('Input Harga awal saat perdadangan dimulai')
High = st.number_input('Input Harga tertinggi kopi selama satu periode')
Low = st.number_input('Input Harga kopi selama satu periode')
Volume = st.number_input('Input Jumlah kopi yang diperdagangkan')

predict = ''

if st.button('Proses'):
    predict = model.predict(
        [[Open, High, Low, Volume]]
    )
    st.write ('Estimasi harga Kopi dalam USD : ', predict)
    st.write ('Estimasi harga Kopi dalam IDR (Juta) :', predict*15000)