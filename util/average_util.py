import sys
sys.path.append('../')

import pandas as pd
import numpy as np
import model.load_data as m_ld
import math
import plotly
import plotly.plotly as py
from plotly import tools
import plotly.graph_objs as go
import statistics as st

def get_biases(pred, real):
	return [pr - rl for pr, rl in zip(pred, real)]

def read_data(path="../data/weatherHistory.csv"):
	df = pd.read_csv(path)
	temp_df = df.drop(axis=1, labels=['Summary', 'Humidity', 'Wind Speed (km/h)', 'Wind Bearing (degrees)', 'Visibility (km)', 'Loud Cover', 'Pressure (millibars)', 'Daily Summary', 'Precip Type'])
	temp_df = temp_df.rename(columns={"Temperature (C)": "real", "Apparent Temperature (C)": "predicted"})#'Formatted Date', 
	return temp_df

def draw_biases(data, biases):
	# Create a trace
	avg = st.mean(biases)
	trace1 = go.Scatter(
	    x = [i for i in range(len(biases))],
	    y = biases,
	    name="Bias"
	)
	trace2 = go.Scatter(
		x = [i for i in range(len(biases))],
		y = [avg for __ in range(len(biases))],
		name="Average bias"
	)
	# trace3 = go.Scatter(
	# 	x = [i for i in range(len(biases))],
	# 	y = [data['real'][i] for i in range(len(biases))],
	# 	name="Real Temperature",
	# 	mode="markers+text",
	# 	text="y"
	# )
	trace4 = go.Scatter(
		x = [i for i in range(len(biases))],
		y = [data['real'][i] for i in range(len(biases))],
		name="Real Temperature"
	)
	trace5 = go.Scatter(
		x = [i for i in range(len(biases))],
		y = [data['predicted'][i] for i in range(len(biases))],
		name="Predicted Temperature"
	)
	# trace6 = go.Scatter(
	# 	x = [i for i in range(len(biases))],
	# 	y = [data['predicted'][i] for i in range(len(biases))],
	# 	name="Real Temperature",
	# 	mode="markers+text",
	# 	text="y"
	# )

	#data = [trace1, trace2]
	# layout = dict(title = 'Bias and average bias Values',
 #              yaxis = dict(title = 'Bias'),
 #              xaxis=dict(
 #              		title = 'Date',
 #                  	rangeselector=dict(
 #                      	buttons=list([
 #                          	dict(count=1,
 #                               	label='1m',
 #                               	step='month',
 #                               	stepmode='backward'),
 #                          	dict(count=6,
 #                               	label='6m',
 #                               	step='month',
 #                               	stepmode='backward'),
 #                          	dict(count=1,
 #                              	label='YTD',
 #                             	step='year',
 #                              	stepmode='todate'),
 #                          	dict(count=1,
 #                              	label='1y',
 #                              	step='year',
 #                              	stepmode='backward'),
 #                          	dict(step='all')
 #                      	])
 #                  	),
 #                  	rangeslider=dict(
 #                      	visible = True
 #                  	),
 #                  	type='date'
 #              	)
 #            )
	#fig = go.Figure(data=data, layout=layout)

	fig = tools.make_subplots(rows=2, cols=1)
	fig.append_trace(trace1, 1, 1)
	fig.append_trace(trace2, 1, 1)
	fig.append_trace(trace4, 2, 1)
	fig.append_trace(trace5, 2, 1)

	#fig = dict(data=data, layout=layout)
	fig['layout'].update(title = 'Bias and average bias Values',
              yaxis = dict(title = 'Bias'),
              xaxis=dict(
              		title = 'Date',
                  	rangeselector=dict(
                      	buttons=list([
                          	dict(count=1,
                               	label='1m',
                               	step='month',
                               	stepmode='backward'),
                          	dict(count=6,
                               	label='6m',
                               	step='month',
                               	stepmode='backward'),
                          	dict(count=1,
                              	label='YTD',
                             	step='year',
                              	stepmode='todate'),
                          	dict(count=1,
                              	label='1y',
                              	step='year',
                              	stepmode='backward'),
                          	dict(step='all')
                      	])
                  	),
                  	rangeslider=dict(
                      	visible = True
                  	),
                  	type='date'
              	))
	
	plotly.offline.plot(fig, filename='../graphs/bias-graph')

def main():
	THRESH = 5
	data = read_data()
	biases = get_biases(data['predicted'], data['real'])
	draw_biases(data, biases[9000:10000])
	for thr in range(1, THRESH + 1):
		result = [0 if abs(bias) >= thr else 1 for bias in biases]
		print("Thresh value : " + str(thr))
		print("Accuracy:", sum(result) / len(result))
	

if __name__ == '__main__':
	main()