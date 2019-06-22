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