import scipy.io
import snap
import networkx as nx
import numpy as np


#Problem5

#load data
data = scipy.io.loadmat("./Enron/Y.mat")['Y']
employees = scipy.io.loadmat("./Enron/employees.mat")['employees']


for i in range(44):
    if(np.amin(data[:, :, i])!=0):
        print(i)

# A) aggregate matrixs and map its element to {0, 1}
A = np.where(np.sum(data, axis = 2) > 0, 1, 0)
print(A.shape)
for i in range(184):
    if(A[i][i]!=0):
        print("false")

# G(V,E)
# number of vertex
V = len(A);
# a set of ordered pair of vertices, in other word, directed arcs
E = set();
for i in range(V):
    for j in range(V):
        if A[i][j] == 1:
            E.add((i, j))

# B) compute the number of directed edges
d_edges = len(E)
print(d_edges)

# C) D) compute the number of undirected edges and mutual arcs
# ud_edges = d_edges - mut_edges
mut_edges = 0
for i, j in E:
    if (j, i) in E:
        mut_edges += 1
mut_edges //= 2
ud_edges = d_edges - mut_edges
print(ud_edges)
print(mut_edges)

# E)
indegree_0_ids = [] 
for i in range(V):
    if np.sum(A[:, i])==0:
        indegree_0_ids.append(i)
print(len(indegree_0_ids))

indegree_0_names = []
for e in indegree_0_ids:
    indegree_0_names.append(employees[i])


# F)
outdegree_0_ids = []
for i in range(V):
    if np.sum(A[i, :])==0:
        outdegree_0_ids.append(i)
print(len(outdegree_0_ids))

outdegree_0_names = []
for e in outdegree_0_ids:
    outdegree_0_names.append(employees[i])

# G)
employee_contacted_larger_than_30 = 0
for v in range(V):
    if np.sum(A[:, v]) >= 30:
        employee_contacted_larger_than_30 += 1
print(employee_contacted_larger_than_30)

# H)
employee_contacting_larger_than_30 = 0
for v in range(V):
    if np.sum(A[v,:]) >= 30:
        employee_contacting_larger_than_30 += 1
print(employee_contacting_larger_than_30)

# I)
A3 = A.dot(A.dot(A))
triangle_count = np.trace(A3) / 3
print(triangle_count)
