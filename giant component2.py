# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 18:05:20 2018

@author: roopal jain
"""


import math
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
n=150
g = nx.fast_gnp_random_graph(n,0.02)
nx.draw_random(g)
##
##giant = sorted(nx.connected_component_subgraphs(g),key = len,reverse = True)
giant = max(nx.connected_component_subgraphs(g),key = len)
nx.draw_random(giant)
#%%
g_node = nx.number_of_nodes(g)
giant_node = nx.number_of_nodes(giant)
isolate_node = nx.number_of_isolates(g)
print(g_node,"\n")
print(giant_node,"\n")
print(isolate_node,"\n")
prob_g = math.log(g_node)/g_node
print(prob_g)
#%%
#g = nx.fast_gnp_random_graph(100,prob_isolate-0.1)
#nx.draw_random(g)
prob_g = math.log(g_node)/g_node
p = []
for i in range(4):
    prob_g =prob_g- 0.03
    p.append(prob_g)
prob_g1 = math.log(g_node)/g_node
for i in range(4):
    prob_g1 =prob_g1+ 0.03
    p.append(prob_g1)


p.append(math.log(n)/n)
p.sort()
#%%
i = 1
while i < len(p):
    component=nx.fast_gnp_random_graph(n,p[i])
    print(plt.figure(i),nx.draw(component),)
    i = i+1
    