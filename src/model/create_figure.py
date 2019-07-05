import plotly.graph_objs as go
import create_graph as cg
import view.custom_objects as view_objs

def create_layout(w=1000, h=700, tit="Weather Forecast", xax=None, yax=None, annot=None, shps=None, axis={}):

	return go.Layout(
		title=tit,
		#width=w,
		height=h,
		showlegend=True,
		scene=dict(
			xaxis=dict(axis),
			yaxis=dict(axis),
			zaxis=dict(axis),
		),
		margin=dict(
			t=100
		),
		hovermode='closest',
		annotations=annot,
		plot_bgcolor='black',
		paper_bgcolor='black',
		font=dict(
			size=13,
			family='sans-serif',
            color='#FFF'
		)
	)

def create_data(graph, data):
	count_nodes = len(data['nodes'])
	bold = None
	scale  = None
	weights = [data['links'][i]['value'] for i in range(len(data['links']))]

	if 'bold' in data:
		bold = data['bold']
	if 'scale' in data:
		scale = data['scale']
	labels=[]
	group=[]
	for node in data['nodes']:
		labels.append(node['name'])
		group.append(node['group'])
	layt=graph.layout('kk', dim=3) # Kamada-Kawai

	Xn=[layt[k][0] for k in range(count_nodes)] # x-coordinates of nodes
	Yn=[layt[k][1] for k in range(count_nodes)] # y-coordinates
	Zn=[layt[k][2] for k in range(count_nodes)] # z-coordinates
	Xe=[]
	Ye=[]
	Ze=[]

	third = None
	for idx, e in enumerate(graph.get_edgelist()):
		Xe.append({
			'coord' : [layt[e[0]][0], layt[e[1]][0], third],
			'bold' : bold[e[0]][e[1]] if bold != None else False,
			'scale' : int(scale[e[0]][e[1]]) if scale != None else 0
		}) # x-coordinates of edge ends
		Ye.append({
			'coord' : [layt[e[0]][1],layt[e[1]][1], third],
			'bold' : bold[e[0]][e[1]] if bold != None else False
		})
		Ze.append({
			'coord' : [layt[e[0]][2],layt[e[1]][2], third],
			'bold' : bold[e[0]][e[1]] if bold != None else False
		})
	return dict(
		Cn={
			'Xn': Xn, 
			'Yn': Yn, 
			'Zn': Zn
		},
		Ce={
			'Xe': Xe, 
			'Ye': Ye, 
			'Ze': Ze
		},
		group=group,
		labels=labels,
		weights=weights
	)

def create_figure(data, layout, fun):
	
	traces = fun(data)
	return dict(
			data=traces,
			layout=layout
		)

if __name__ == '__main__':
	print(create_figure([], []))