import plotly.graph_objs as go
import create_graph as cg
import view.custom_objects as view_objs

def create_layout(w=1000, h=1000, tit="Weather Forecast", xax=None, yax=None, annot=None, shps=None, axis={}):

	return go.Layout(
		title=tit,
		width=w,
		height=h,
		showlegend=False,
		scene=dict(
			xaxis=dict(axis),
			yaxis=dict(axis),
			zaxis=dict(axis),
		),
		margin=dict(
			t=100
		),
		hovermode='closest',
		annotations=annot
	)

def create_data(graph, data):
	count_nodes = len(data['nodes'])

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
	for e in graph.get_edgelist():
		Xe+=[layt[e[0]][0],layt[e[1]][0], None] # x-coordinates of edge ends
		Ye+=[layt[e[0]][1],layt[e[1]][1], None]  
		Ze+=[layt[e[0]][2],layt[e[1]][2], None]
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
		labels=labels
	)

def create_figure(data, layout):
	
	traces = view_objs.get_custom_traces(data)
	return dict(
			data=traces,
			layout=layout
		)

if __name__ == '__main__':
	print(create_figure([], []))