# -*- coding: utf-8 -*-
import sys
sys.path.append('./model')
sys.path.append('./view')

import dash
import dash_core_components as dcc
import dash_html_components as html
import view.custom_objects as view_objs
import view.graph as view_graph
import model.create_figure as cf
import model.create_graph as cg
import model.load_data as ld

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

data = ld.read_data("../data/forecasts.json")
graph = cg.create_graph(data)
figure_data = cf.create_data(graph, data)
fig = cf.create_figure(figure_data, cf.create_layout(annot=view_objs.custom_layout()))

app.layout = html.Div(children=[
	html.H1(children='Hello Dash'),

	html.Div(children='''
		Dash: A web application framework for Python.
	'''),

	view_graph.get_graph(fig)
])

if __name__ == '__main__':
	app.run_server(debug=True)