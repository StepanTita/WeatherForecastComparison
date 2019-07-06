import styles_elements
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
import random as rd
import math

def custom_layout():
	return [dict(
				showarrow=False,
				#text="Data source: <a href='http://bost.ocks.org/mike/miserables/miserables.json'>[1] miserables.json</a>",
				#xref='paper',
				#yref='paper',
				x=0,
				y=0.1,
				xanchor='left',
				yanchor='bottom',
				font=dict(
					size=16,
					family='sans-serif',
            		color='#FFF'
				),
				bgcolor='black'
			)]
def custom_axis():
	return dict(
		showbackground=False,
        showline=False,
        zeroline=False,
        showgrid=False,
        showticklabels=False,
        title=''
    )

def get_colorscale(new_id=14):
	colorscales = [
		'Blackbody',
		'Bluered',
		'Blues',
		'Earth',
		'Electric',
		'Greens',
		'Greys',
		'Hot',
		'Jet',
		'Picnic',
		'Portland',
		'Rainbow',
		'RdBu',
		'Reds',
		'Viridis',
		'YlGnBu',
		'YlOrRd',
		styles_elements.my_colorscale1()
	]
	return colorscales[new_id]

def get_bold_traces(data):
	#new_id = rd.randint(0, 17)
	new_id = 11
	#print(new_id)
	# Creating edges
	trace1 = []
	edges = data['Ce']
	edgesX = edges['Xe']
	edgesY = edges['Ye']
	edgesZ = edges['Ze']
	for i in range(len(edgesX)):
		trace1.append(go.Scatter3d(
			x=edgesX[i]['coord'],
			y=edgesY[i]['coord'],
			z=edgesZ[i]['coord'],
			mode='lines',
			line=dict(
				color='rgb(255,10,10)' if edgesX[i]['bold'] else 'rgb(250,250,250)', 
				width=10 if edgesX[i]['bold'] else 3
			),
			text=data['weights'][i],
			name="Edge " + str(i),
			#hoverinfo='x+y+z', 'text', 'name']
		))

	# Creating nodes 
	# ??????????????????????????????? WHAT ABOUT DIFFERENT SIZES????
	trace2 = go.Scatter3d(
		x=data['Cn']['Xn'],
		y=data['Cn']['Yn'],
		z=data['Cn']['Zn'],
		mode='markers',
		name='forecasts',
		marker=dict(
			symbol='circle',
			size=rd.randint(16, 26),
			color=data['group'],
			colorscale=get_colorscale(new_id),
			line=dict(color='rgb(50,50,50)', width=0),
			opacity=0.8,

			# sizemode="area",
			# sizeref=200000,
			# size=[rd.randint(12, 22) for __ in range(len(data['Cn']['Xn']))]
		),
		text=data['labels'],
		hoverinfo='text'
	)
	# print(trace1)
	# print("----------------------------------------------------------")
	# print(trace2)
	trace1.append(trace2)
	return trace1

def get_scale_traces(data):
	#new_id = rd.randint(0, 17)
	new_id = 11
	#print(new_id)
	# Creating edges
	trace1 = []
	edges = data['Ce']
	edgesX = edges['Xe']
	edgesY = edges['Ye']
	edgesZ = edges['Ze']

	colors = []
	Xs = []
	Ys = []
	Zs = []

	for i in range(len(edgesX)):
		Xs+=edgesX[i]['coord']
		Ys+=edgesY[i]['coord']
		Zs+=edgesZ[i]['coord']
		colors += [edgesX[i]['scale'], edgesX[i]['scale'], edgesX[i]['scale']]
	trace1 = go.Scatter3d(
		x=Xs,
		y=Ys,
		z=Zs,
		mode='lines',
		line=dict(
			color=colors, 
			width=12,#widths,
			colorscale=get_colorscale(11),
			cmin=0,
			cmax=len(colors),
			autocolorscale=True
        ),
        marker=dict(
        	colorbar=dict(
                title='Colorbar'
            )
        ),
        opacity=0.8,
		text=data['weights'],
		name="Flows"
		#hoverinfo='text'#['x', 'y', 'z', 'text', 'name']
	)

	# Creating nodes 
	# ??????????????????????????????? WHAT ABOUT DIFFERENT SIZES????
	trace2 = go.Scatter3d(
		x=data['Cn']['Xn'],
		y=data['Cn']['Yn'],
		z=data['Cn']['Zn'],
		mode='markers',
		name='forecasts',
		marker=dict(
			#symbol='circle',
			size=rd.randint(16, 26),
			color=data['group'],
			colorscale=get_colorscale(new_id),
			line=dict(color='rgb(50,50,50)', width=0),
			opacity=0.8
		),
		text=data['labels'],
		hoverinfo='text'
	)


	# print(trace1)
	# print("----------------------------------------------------------")
	# print(trace2)
	return [trace1, trace2]

def create_slider():
	return html.Div(dcc.Slider(
        id='algo_steps',
        min=0,
        max=10,
        value=0,
        step=1,
        marks={i : "Step {}".format(i) for i in range(11)},
        disabled=False
    ), style={'width': '100%', 'margin-bottom' : '30px', 'font-size' : '18pt'}, id='slider-container')

def create_dropdown():
	return html.Div(children=[dcc.Dropdown(
        id='drop-algos',
        options=[
            {'label': 'Prim', 'value': 'prim'},
            {'label': 'Stoer-Wagner', 'value': 'stw'},
            {'label': 'Preflow push', 'value': 'pfp'}
        ],
        value='prim',
        style={'width': '45%', 'float' : 'left'}
    ),
    html.Button('Run', id='prim-btn', style={'width' : '150px', 'font-size' : '24pt'}),
    dcc.Dropdown(
        id='drop-data',
        options=[
            {'label': 'Forecasts', 'value': 'fore'},
            {'label': 'Test 1', 'value': 'test1'},
            {'label': 'Test2', 'value': 'test2'}
        ],
        value='Forecasts',
        style={'width': '45%', 'float' : 'left'}
    )], style={'width': '100%'})

if __name__ == '__main__':
	main()