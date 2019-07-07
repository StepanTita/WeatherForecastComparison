import igraph as ig

import json
import urllib.request

def load_data(path="https://raw.githubusercontent.com/plotly/datasets/master/miserables.json"):
	data = []
	file = urllib.request.urlopen(path)
	data = json.loads(file.read())
	return data
def read_data(path):
	data = []
	with open(path) as file:
		data = json.loads(file.read())
	return data

if __name__ == "__main__":
	print(load_data())
