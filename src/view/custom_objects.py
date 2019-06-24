import styles_elements
import plotly.graph_objs as go
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
			size=rd.randint(9, 18),
			color=data['group'],
			colorscale=get_colorscale(new_id),
			line=dict(color='rgb(50,50,50)', width=0),
			opacity=0.8
		),
		text=data['labels'],
		hoverinfo='text'
	)
	return [trace1, trace2]

if __name__ == '__main__':
	main()