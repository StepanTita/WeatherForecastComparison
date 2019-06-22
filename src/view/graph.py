import dash_core_components as dcc
import model

def get_graph(fig):
	return dcc.Graph(
		id='example-graph',
		figure=fig
	)

if __name__ == '__main__':
	print(get_graph())