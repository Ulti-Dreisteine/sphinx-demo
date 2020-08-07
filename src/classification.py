# -*- coding: utf-8 -*-
from sklearn.ensemble import GradientBoostingClassifier
import pandas as pd
import sys, os

sys.path.append('../')

from src import proj_dir


def load_test_data():
	"""
	载入测试数据并处理
	
	Returns
	-------
	data: pd.DataFrame, 本地测试数据
	"""
	data = pd.read_csv(os.path.join(proj_dir, 'data/local_test/patient_data.csv'))
	return data
	

def process_data(data):
	"""
	数据处理, 去掉多余字段并按照数值型和类别型字段进行值处理
	
	Parameters
	----------
	data: pd.DataFrame, 待处理数据表
	
	Returns
	-------
	data: pd.DataFrame, 处理好的数据表
	numeric_cols: list, 数值型字段
	categoric_cols: list, 类别型字段
	"""
	# 去掉多余字段.
	data.drop('INPATIENT_ID', axis = 1, inplace = True)
	
	# 按照数值型字段和类别性字段进行处理.
	numeric_cols = [
		'AGE', 'ISS', 'CAPRINI_SCORE', 'T', 'P', 'R', 'MBP', 'SHOCK_INDEX', 'HEIGHT', 'WEIGHT',
		'BMI', 'RBC', 'HGB', 'PLT', 'WBC', 'ALB', 'CRE', 'UA', 'AST', 'ALT', 'GLU', 'TG', 'CHO',
		'CA', 'MG', 'LDL', 'NA', 'K', 'CL', 'GFR', 'PT', 'FIB', 'DD', 'CK', 'INR'
	]
	
	categoric_cols = [p for p in list(data.columns) if p not in ['VTE'] + numeric_cols]
	
	for col in data.columns:
		if col == 'VTE':
			data[col] = data[col].apply(lambda x: 'pos' if x == 1 else 'neg')
		elif col in categoric_cols:
			data[col] = data[col].astype(int)
		elif col in numeric_cols:
			data[col] = data[col].astype(float)
		else:
			pass
	
	return data, numeric_cols, categoric_cols