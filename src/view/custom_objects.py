import styles_elements
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
import random as rd

def custom_layout():
	return [dict(
				showarrow=False,
				#text="Data source: <a href='http://bost.ocks.org/mike/miserables/miserables.json'>[1] miserables.json</a>",
				xref='paper',
				yref='paper',
				x=0,
				y=0.1,
				xanchor='left',
				yanchor='bottom',
				font=dict(
					size=14
				)
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

def get_custom_traces(data):
	new_id = rd.randint(0, 17)
	print(new_id)
	# Creating edges
	trace1=go.Scatter3d(
		x=data['Ce']['Xe'],
		y=data['Ce']['Ye'],
		z=data['Ce']['Ze'],
		mode='lines',
		line=dict(color='rgb(200,200,200)', width=2),
		hoverinfo='none'
	)

	# Creating nodes 
	# ??????????????????????????????? WHAT ABOUT DIFFERENT SIZES????
	trace2=go.Scatter3d(
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
	print(trace1)
	print("----------------------------------------------------------")
	print(trace2)
	return [trace1, trace2]

def get_bold_traces(data):
	#new_id = rd.randint(0, 17)
	new_id = 14
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
			line=dict(color='rgb(255,10,10)' if edgesX[i]['bold'] else 'rgb(200,200,200)', width=10 if edgesX[i]['bold'] else 2),
			hoverinfo=['x', 'y', 'z', 'text', 'name']
		))
	

	# Creating nodes 
	# ??????????????????????????????? WHAT ABOUT DIFFERENT SIZES????
	trace2=go.Scatter3d(
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
	#print(trace1)
	#print("----------------------------------------------------------")
	#print(trace2)
	trace1.append(trace2)
	return trace1

def create_slider():
	return html.Div(dcc.Slider(
        id='algo_steps',
        min=1,
        max=10,
        value=1,
        step=1,
        marks={i : "Step {}".format(i) for i in range(11)},
        disabled=False
    ), style={'width': '60%'}, id='slider-container')

if __name__ == '__main__':
	main()