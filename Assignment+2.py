
# coding: utf-8

# ---
# 
# _You are currently looking at **version 1.2** of this notebook. To download notebooks and datafiles, as well as get help on Jupyter notebooks in the Coursera platform, visit the [Jupyter Notebook FAQ](https://www.coursera.org/learn/python-social-network-analysis/resources/yPcBs) course resource._
# 
# ---

# # Assignment 2 - Network Connectivity
# 
# In this assignment you will go through the process of importing and analyzing an internal email communication network between employees of a mid-sized manufacturing company. 
# Each node represents an employee and each directed edge between two nodes represents an individual email. The left node represents the sender and the right node represents the recipient.

# In[ ]:


import networkx as nx

# This line must be commented out when submitting to the autograder
#!head email_network.txt


# ### Question 1
# 
# Using networkx, load up the directed multigraph from `email_network.txt`. Make sure the node names are strings.
# 
# *This function should return a directed multigraph networkx graph.*

# In[ ]:


def answer_one():
    
    # Your Code Here
    import pandas as pd
    data = pd.read_csv('email_network.txt', sep='\t')
    data.drop(['time'], axis=1, inplace=True)
    data.columns = ['sender', 'recipient']
    data = data.astype(str)
    G = nx.from_pandas_dataframe(data,  'sender', 'recipient', create_using=nx.MultiDiGraph())
    return G# Your Answer Here


# ### Question 2
# 
# How many employees and emails are represented in the graph from Question 1?
# 
# *This function should return a tuple (#employees, #emails).*

# In[ ]:


def answer_two():
        
    # Your Code Here
    G = answer_one()
    n_employees = len(G.nodes())
    n_mails = len(G.edges())
    return (n_employees, n_mails) # Your Answer Here


# ### Question 3
# 
# * Part 1. Assume that information in this company can only be exchanged through email.
# 
#     When an employee sends an email to another employee, a communication channel has been created, allowing the sender to provide information to the receiver, but not vice versa. 
# 
#     Based on the emails sent in the data, is it possible for information to go from every employee to every other employee?
# 
# 
# * Part 2. Now assume that a communication channel established by an email allows information to be exchanged both ways. 
# 
#     Based on the emails sent in the data, is it possible for information to go from every employee to every other employee?
# 
# 
# *This function should return a tuple of bools (part1, part2).*

# In[ ]:


def answer_three():
        
    # Your Code Here
    G = answer_one()
    is_strongly_connected = nx.is_strongly_connected(G)
    is_weakly_connected = nx.is_weakly_connected(G)
    return (is_strongly_connected, is_weakly_connected) # Your Answer Here


# ### Question 4
# 
# How many nodes are in the largest (in terms of nodes) weakly connected component?
# 
# *This function should return an int.*

# In[ ]:


def answer_four():
        
    # Your Code Here
    G = answer_one()
    largest_cc = max(nx.weakly_connected_components(G), key=len)
    n_nodes = len(largest_cc)
    return n_nodes # Your Answer Here


# ### Question 5
# 
# How many nodes are in the largest (in terms of nodes) strongly connected component?
# 
# *This function should return an int*

# In[ ]:


def answer_five():
        
    # Your Code Here
    G = answer_one()
    largest_scc = max(nx.strongly_connected_components(G), key=len)
    n_nodes = len(largest_scc)
    return n_nodes # Your Answer Her


# ### Question 6
# 
# Using the NetworkX function strongly_connected_component_subgraphs, find the subgraph of nodes in a largest strongly connected component. 
# Call this graph G_sc.
# 
# *This function should return a networkx MultiDiGraph named G_sc.*

# In[ ]:


def answer_six():
        
    # Your Code Here
    G = answer_one()
    G_sc = max(nx.strongly_connected_component_subgraphs(G), key=len)
    return G_sc # Your Answer Here


# ### Question 7
# 
# What is the average distance between nodes in G_sc?
# 
# *This function should return a float.*

# In[ ]:


def answer_seven():
        
    # Your Code Here
    G_sc = answer_six()
    avrg_distance = nx.average_shortest_path_length(G_sc)
    
    return avrg_distance # Your Answer Here



# ### Question 8
# 
# What is the largest possible distance between two employees in G_sc?
# 
# *This function should return an int.*

# In[ ]:


def answer_eight():
        
    # Your Code Here
    G_sc = answer_six()
    diameter = nx.diameter(G_sc)
    return diameter # Your Answer Here


# ### Question 9
# 
# What is the set of nodes in G_sc with eccentricity equal to the diameter?
# 
# *This function should return a set of the node(s).*

# In[ ]:


def answer_nine():
       
    # Your Code Here
    G_sc = answer_six()
    periphery = nx.periphery(G_sc)
    return set(periphery) # Your Answer Here


# ### Question 10
# 
# What is the set of node(s) in G_sc with eccentricity equal to the radius?
# 
# *This function should return a set of the node(s).*

# In[ ]:


def answer_ten():
        
    # Your Code Here
    G_sc = answer_six()
    
    center = nx.center(G_sc)
    return set(center) # Your Answer Here


# ### Question 11
# 
# Which node in G_sc is connected to the most other nodes by a shortest path of length equal to the diameter of G_sc?
# 
# How many nodes are connected to this node?
# 
# 
# *This function should return a tuple (name of node, number of satisfied connected nodes).*

# In[ ]:


def answer_eleven():
        
    # Your Code Here
    
    return # Your Answer Here


# ### Question 12
# 
# Suppose you want to prevent communication from flowing to the node that you found in the previous question from any node in the center of G_sc, what is the smallest number of nodes you would need to remove from the graph (you're not allowed to remove the node from the previous question or the center nodes)? 
# 
# *This function should return an integer.*

# In[ ]:


def answer_twelve():
        
    # Your Code Here
    
    return # Your Answer Here


# ### Question 13
# 
# Construct an undirected graph G_un using G_sc (you can ignore the attributes).
# 
# *This function should return a networkx Graph.*

# In[ ]:


def answer_thirteen():
        
    # Your Code Here
    G_sc = answer_six()
    G_un = nx.Graph(G_sc.to_undirected())
    return G_un # Your Answer Here


# ### Question 14
# 
# What is the transitivity and average clustering coefficient of graph G_un?
# 
# *This function should return a tuple (transitivity, avg clustering).*

# In[ ]:


def answer_fourteen():
        
    # Your Code Here
    G_un = nx.Graph(answer_thirteen())
    transitivity = nx.transitivity(G_un)
    cc = nx.average_clustering(G_un)
    return (transitivity, cc)# Your Answer Here


# In[ ]:




