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

prev_test = "Ok"

data = ld.read_data("../data/forecasts.json")
my_graph = alg_graph.GraphWeighted(data)
vis = drw.GraphVisual(my_graph)

graph = cg.create_graph(data)
figure_data = cf.create_data(graph, data)
fig = cf.create_figure(figure_data, cf.create_layout(axis=view_objs.custom_axis()), view_objs.get_bold_traces)

app.layout = html.Div(children=[
	view_graph.get_graph(fig),
	view_objs.create_slider(),
	view_objs.create_dropdown()
])


# ------------------------------ CALLBACKS -------------------------------------
@app.callback(
	dash.dependencies.Output('example-graph', 'figure'),
	[dash.dependencies.Input('algo_steps', 'value'),
	dash.dependencies.Input('drop-data', 'value')])
def update_graph(value, test):
	global fig
	global vis
	global prev_test
	new_fig = vis.get_snapshot(value)
	# if new_fig is not None:
	# 	frames = vis.get_frames()
	# 	new_fig['frames'] = [{'data' : }]
	if test == "fore" and test != prev_test:
		prev_test = "fore"
		data = ld.read_data("../data/forecasts.json")
		my_graph = alg_graph.GraphWeighted(data)
		vis = drw.GraphVisual(my_graph)

		graph = cg.create_graph(data)
		figure_data = cf.create_data(graph, data)
		fig = cf.create_figure(figure_data, cf.create_layout(axis=view_objs.custom_axis()), view_objs.get_bold_traces)
		return fig
	elif test == "test1" and test != prev_test:
		prev_test = "test1"
		data = ld.read_data("../data/test.json")
		my_graph = alg_graph.GraphWeighted(data)
		vis = drw.GraphVisual(my_graph)

		graph = cg.create_graph(data)
		figure_data = cf.create_data(graph, data)
		fig = cf.create_figure(figure_data, cf.create_layout(axis=view_objs.custom_axis()), view_objs.get_bold_traces)
		return fig
	elif test == "test2" and test != prev_test:
		prev_test = "test2"
		data = ld.read_data("../data/test1.json")
		my_graph = alg_graph.GraphWeighted(data)
		vis = drw.GraphVisual(my_graph)

		graph = cg.create_graph(data)
		figure_data = cf.create_data(graph, data)
		fig = cf.create_figure(figure_data, cf.create_layout(axis=view_objs.custom_axis()), view_objs.get_bold_traces)
		return fig
	if new_fig is None:
		return fig
	return new_fig

@app.callback(
	dash.dependencies.Output('slider-container', 'children'),
	[dash.dependencies.Input('prim-btn', 'n_clicks')],
	[dash.dependencies.State('drop-algos', 'value')])
def update_output(n_clicks, value):
	if value == 'prim':
		vis.apply_prim()
	elif value == 'stw':
		vis.apply_stoer_wagner()
	elif value == 'pfp':
		vis.apply_preflow()
	if n_clicks != None and n_clicks > 0:
		return dcc.Slider(
			id='algo_steps',
			min=0,
			max=vis.count_snapshots(),
			value=1,
			marks={str(i) : str(i) for i in range(vis.count_snapshots())}
		)
	#return view_objs.create_slider()

if __name__ == '__main__':
	app.run_server(debug=False)