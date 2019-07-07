import dash_core_components as dcc
import model

def get_graph(fig):
	return dcc.Graph(
		id='example-graph',
		figure=fig,
		animate=True,
        animation_options=dict(
            transition={'duration' : 500},
            redraw=False
        )
	)

if __name__ == '__main__':
	print(get_graph())