import math
import plotly
import plotly.plotly as py
from plotly import tools
import plotly.graph_objs as go
import statistics as st

def main():
	labels = ['AccuWeather','Yandex','BBC','Gismeteo', 'World Weather', 'Intellicast']
	values = [27, 30, 25, 9, 6, 3]

	trace = go.Pie(labels=labels, values=values)
	layout=dict(
		paper_bgcolor='#1e202b',
    	plot_bgcolor='#1e202b',
    	title='Forecast share',
    	font=dict(
            family='sans-serif',
            size=15,
            color='#FFF'
        ),
    )

	
	fig = go.Figure(data=[trace], layout=layout)
	plotly.offline.plot(fig, filename='../graphs/pie_chart')

if __name__ == '__main__':
	main()