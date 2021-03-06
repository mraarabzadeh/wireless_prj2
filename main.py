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
        connected_graph[key] = [node[i]]
        for j in range(i+1,len(node)):
            if (node[i][0] - node[j][0])**2 + (node[i][1] - node[j][1])**2 <= r **2:
                connected_graph[key].append(node[j])
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

def plot_graph(size, n):
    x = np.random.uniform(0,size, n)
    y = np.random.uniform(0,size, n)
    node = np.stack([x,y],1)
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

def calc_set(*args):
    size = args[0]
    dicc = {}
    listt = []
    for i in range(1,len(args)):
        for item in args[i]:
            if hash_calc(item, size) not in dicc:
                listt.append(item)
                dicc[hash_calc(item, size)] = 1
    dicc.clear()
    return listt

def make_touple(x,y):
    output = []
    for i in range(len(x)):
        output.append([x[i], y[i]])
    return output


def BDfs(key,size, setdic):
    if key in setdic:
        return setdic[key]
    this_set = calc_set(size,connected_graph[key])
    if len(connected_graph[key]) == 1:
        return this_set
    for i in range(1,len(connected_graph[key])):
        this_set = calc_set(size,BDfs(hash_calc(connected_graph[key][i], size),size, setdic) ,this_set )
    setdic[key] = this_set
    return this_set

def find_alone_node(listt):
    x = 0
    for i in listt:
        if i == 1:
            x+= 1
    return x

def stroglyConnectedComponent(size,n):
    x = np.random.uniform(0,size, n)
    y = np.random.uniform(0,size, n)
    # node = np.stack([x,y],1)
    node = make_touple(x,y)
    find_tree(node,1,size)
    BDfs_dic = {}
    size_list = []
    setdic = {}
    for key,item in connected_graph.items():
        if key in BDfs_dic:
            continue
        r = BDfs(key,size,setdic)
        for items in r:
            BDfs_dic[hash_calc(items,size)] = 1
        size_list.append(len(r))
        size_list.sort()
    return size_list if len(size_list) > 0 else 0

def detail_of_SCC(size):
    listt = []
    for n in range(100):
        max_size = 0
        second_max_size = 0
        min_size = 0
        for i in range(10):
            size_list = stroglyConnectedComponent(size, n)
            if size_list == 0:
                continue
            elif len(size_list) == 1:
                max_size += size_list[0]
                min_size += size_list[0]
                second_max_size += size_list[0]
            else:
                max_size += size_list[-1]
                min_size += find_alone_node(size_list)
                second_max_size += size_list[-2]
            connected_graph.clear()
        listt.append([ max_size/10, min_size/10, second_max_size/10])
    listt = [[listt[j][i] for j in range(len(listt))] for i in range(len(listt[0]))]
    plt.plot(range(100), listt[0], label='max size')
    plt.plot(range(100), listt[1], label='num of alone node')
    plt.plot(range(100), listt[2], label='second max size')
    plt.xlabel('graph size')
    plt.ylabel('num of nodes')
    plt.legend() 
    plt.show()
    return listt


def float_range(st,stop,step):
    return [x*step for x,i in enumerate(range(st,int(stop/step)))]
def A_N_connected(a, size, n):
    prob = []
    for r in float_range(0,4.5, .1):
        num = 0
        for i in range(100):
            size_list = stroglyConnectedComponent(size, n)
            if len(size_list) == 0:
                continue
            elif size_list[-1] >= a * n:
                num += 1
            connected_graph.clear()
        prob.append(num)
        # print(r,'   ', num)
    plt.plot(float_range(0,4.5,.1), prob)
    plt.xlabel('distance')
    plt.ylabel('probability')
    plt.legend() 
    plt.show()
# plot_graph(x,y)
if __name__ == "__main__":
    print(float_range(0,10,.5))
    situation = input('for printing graph enter1\nfor printing mid for size of connectedcomponent enter 2\nfor an connected analysis enter 3\n')
    if situation=='1':
        n = int(input('enter num of nodes:'))
        size = int(input('enter width of space:'))
        plot_graph(size, n)
    if situation=='2':
        size = int(input('enter width of space:'))
        detail_of_SCC(size)
    if situation == '3':
        n = int(input('enter num of nodes:'))
        size = float(input('enter width of space:'))
        a = float(input('enter multiplication:'))
        A_N_connected(a, size,n)