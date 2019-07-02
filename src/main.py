# -*- coding: utf-8 -*-
import sys
sys.path.append('./model')
sys.path.append('./view')
sys.path.append('./algos')

import dash
import dash_core_components as dcc
import dash_html_components as html
import view.custom_objects as view_objs
import view.graph as view_graph
import model.create_figure as cf
import model.create_graph as cg
import model.load_data as ld
import model.draw_graph as drw
import algos.graph as alg_graph

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

data = ld.read_data("../data/forecasts.json")
my_graph = alg_graph.GraphWeighted(data)
vis = drw.GraphVisual(my_graph)

graph = cg.create_graph(data)
figure_data = cf.create_data(graph, data)
fig = cf.create_figure(figure_data, cf.create_layout(annot=view_objs.custom_layout()))

app.layout = html.Div(children=[
	html.H1(children='Hello Dash'),

	html.Div(children='''
		Dash: A web application framework for Python.
	'''),

	view_graph.get_graph(fig),
	view_objs.create_slider(),
	html.Button('Run Prim', id='prim-btn')
])


# ------------------------------ CALLBACKS -------------------------------------
@app.callback(
	dash.dependencies.Output('example-graph', 'figure'),
	[dash.dependencies.Input('algo_steps', 'value')])
def update_graph(value):
	global fig
	new_fig = vis.get_snapshot(value)
	if new_fig is None:
		return fig
	return new_fig

@app.callback(
	dash.dependencies.Output('slider-container', 'children'),
	[dash.dependencies.Input('prim-btn', 'n_clicks')])
def update_output(n_clicks):
	vis.apply_prim()
	if n_clicks != None and n_clicks > 0:
		return dcc.Slider(
			id='algo_steps',
			min=1,
			max=vis.count_snapshots(),
			value=1,
			marks={str(i + 1) : str(i + 1) for i in range(vis.count_snapshots())}
			)

if __name__ == '__main__':
	app.run_server(debug=True)