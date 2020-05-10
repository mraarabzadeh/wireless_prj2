import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

connected_graph = {}
colors = ['red', 'blue', 'green', 'black' ,'cyan','magenta','yellow']
def hash_calc(node,size):
    return node[0]*size + node[1]

def find_tree(node,r,size):

    for i in range(len(node)):
        key = hash_calc(node[i], size)
        for j in range(i+1,len(node)):
            if (node[i][0] - node[j][0])**2 + (node[i][1] - node[j][1])**2 <= r **2:
                if key in connected_graph:
                    connected_graph[key].append(node[j])
                else:
                    connected_graph[key] = [node[i],node[j]]
    return

def prepare_to_plot(node_list):
    head = node_list[0]
    x = []
    y = []
    for i in range(1,len(node_list)):
        x.append(head[0])
        y.append(head[1])
        x.append(node_list[i][0])
        y.append(node_list[i][1])
        
    return x,y

def plot_graph(x,y):
    find_tree(node, 1,size)
    plt.plot(x,y, color='black', linewidth = 0, 
             marker='o', markerfacecolor='black', markersize=12) 
    i = 0
    for key , value in connected_graph.items():
        xx , yy= prepare_to_plot(value)
        plt.plot(xx,yy, color=colors[i%7], linewidth = 1, 
                marker='o', markerfacecolor='black', markersize=12) 
        i += 1
    plt.show()
n = int(input())
size = int(input())
x = np.random.uniform(0,size, n)
y = np.random.uniform(0,size, n)
node = np.stack([x,y],1)
plot_graph(x,y)
