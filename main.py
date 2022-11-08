import streamlit as st
import pandas as pd
import numpy as np
import datetime
dt_now = datetime.datetime.now()
st.set_page_config(layout="wide")

st.title("Sirius to Windows Converter (ver 1.0)")
st.subheader("SalonAppで取得したSirius CSVをアップロードしてください")
tmp = st.file_uploader("", type='csv')

st.write(tmp)



if(tmp != None):
	df = pd.read_csv(tmp,encoding = 'UTF8')
	st.write(df)

	df_out = pd.DataFrame({
		'Time' : df['timeStamp'],
		'RawData' : df['brainWave'],
		'RawData_uV' : df['brainWave'],
		'RawDataEdit' : df['brainWave'],
		'RawDataEdit_uV' : df['brainWave'],
		'SQ' : np.zeros(len(df['timeStamp']),dtype=int)
		})
	st.write(df_out)
	name = "mind_raw_" + str(dt_now.year)+str(dt_now.month)+str(dt_now.day) + "_" + str(dt_now.hour) + str(dt_now.minute) + '.csv'
	st.write(name)

	df_out = df_out.to_csv(index = False).encode('utf-8')

	st.download_button(
		label='ダウンロード',
		data=df_out,
		file_name=name,
		mime='text/csv',)