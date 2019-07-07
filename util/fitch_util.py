import sys
sys.path.append('../')

import pandas as pd
import numpy as np
import model.load_data as m_ld
import math

def fitch_tree(data):
	tree = [[] for __ in range(2 * int(math.log2(len(data['sources'])) + 1))]
	tree[0] += [src for src in data['sources']]

	prev = 0
	for step in range(1, len(tree)):
		if len(tree[prev]) % 2 != 0:
			tree[prev].append({
					"name" : ["pseudo"],
					"acc_t" : {"src" : "pseudo", "val" : 0}, 
					"acc_h" : {"src" : "pseudo", "val" : 0}, 
					"acc_w" : {"src" : "pseudo", "val" : 0}
				})
		
		for i in range(0, len(tree[prev]), 2):
			last = len(tree[step])
			tree[step].append({
				"name" : [],
				"acc_t" : {"src" : "pseudo", "val" : 0}, 
				"acc_h" : {"src" : "pseudo", "val" : 0}, 
				"acc_w" : {"src" : "pseudo", "val" : 0}
			})
			# -----1-----
			if tree[prev][i]["acc_t"]["val"] > tree[prev][i + 1]["acc_t"]["val"]:
				new_name = tree[prev][i]["acc_t"]["src"]
				new_val = tree[prev][i]["acc_t"]["val"]
				if new_name not in tree[step][last]["name"]:
					tree[step][last]["name"].append(new_name)
				tree[step][last]["acc_t"]["src"] = new_name
				tree[step][last]["acc_t"]["val"] = new_val
			else:
				new_name = tree[prev][i + 1]["acc_t"]["src"]
				new_val = tree[prev][i + 1]["acc_t"]["val"]
				if new_name not in tree[step][last]["name"]:
					tree[step][last]["name"].append(new_name)
				tree[step][last]["acc_t"]["src"] =  new_name
				tree[step][last]["acc_t"]["val"] = new_val
			# -----2-----
			if tree[prev][i]["acc_h"]["val"] > tree[prev][i + 1]["acc_h"]["val"]:
				new_name = tree[prev][i]["acc_h"]["src"]
				new_val = tree[prev][i]["acc_h"]["val"]
				if new_name not in tree[step][last]["name"]:
					tree[step][last]["name"].append(new_name)
				tree[step][last]["acc_h"]["src"] =  new_name
				tree[step][last]["acc_h"]["val"] = new_val
			else:
				new_name = tree[prev][i + 1]["acc_h"]["src"]
				new_val = tree[prev][i + 1]["acc_h"]["val"]
				if new_name not in tree[step][last]["name"]:
					tree[step][last]["name"].append(new_name)
				tree[step][last]["acc_h"]["src"] =  new_name
				tree[step][last]["acc_h"]["val"] = new_val
			# ------3------
			if tree[prev][i]["acc_w"]["val"] > tree[prev][i + 1]["acc_w"]["val"]:
				new_name = tree[prev][i]["acc_w"]["src"]
				new_val = tree[prev][i]["acc_w"]["val"]
				if new_name not in tree[step][last]["name"]:
					tree[step][last]["name"].append(new_name)
				tree[step][last]["acc_w"]["src"] =  new_name
				tree[step][last]["acc_w"]["val"] = new_val
			else:
				new_name = tree[prev][i + 1]["acc_w"]["src"]
				new_val = tree[prev][i + 1]["acc_w"]["val"]
				if new_name not in tree[step][last]["name"]:
					tree[step][last]["name"].append(new_name)
				tree[step][last]["acc_w"]["src"] =  new_name
				tree[step][last]["acc_w"]["val"] = new_val
			
		if len(tree[step]) == 1:
			break
		prev = step
	return tree

def my_print(tree):
	flag = False
	for i in range(len(tree)):
		for j in range(len(tree[i])):
			print(tree[i][j]["name"], end=" ")
			if (len(tree[i]) == 1):
				flag = True
				print("\nResult: ")
				print(">> Temperature accuracy(" + tree[i][j]["acc_t"]["src"] + "): " + str(tree[i][j]["acc_t"]["val"]))
				print(">> Humidity accuracy(" + tree[i][j]["acc_h"]["src"] + "): " + str(tree[i][j]["acc_h"]["val"]))
				print(">> Wind speed accuracy(" + tree[i][j]["acc_w"]["src"] + "): " + str(tree[i][j]["acc_w"]["val"]), end="")
		print("\n------------------------")
		if flag:
			break
		


def test_fitch():
	data = m_ld.read_data("../data/sources.json")
	tree = fitch_tree(data)
	#print_tree(tree)
	my_print(tree)

if __name__ == '__main__':
	#main()
	test_fitch()