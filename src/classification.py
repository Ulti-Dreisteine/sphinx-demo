# -*- coding: utf-8 -*-

import pandas as pd
import sys, os

sys.path.append('../')

from src import proj_dir


def load_test_data():
	"""
	Load local test data.
	
	:returns: data: pd.DataFrame, local test data
	"""
	data = pd.read_csv(os.path.join(proj_dir, 'data/local_test/patient_data.csv'))
	return data
	

def process_data(data):
	"""
	Process data, remove redundant fields and seperate them into numerical and
	categorical types.
	
	:param data: pd.DataFrame, data table to be processed
	:returns:
		data: pd.DataFrame, processed table;
		numeric_cols: list, numerical fields;
		categoric_cols: list, categorical fields;
	"""
	# Remove redundant fields.
	data.drop('INPATIENT_ID', axis = 1, inplace = True)
	
	# Process data according to numerical or categorical value types.
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