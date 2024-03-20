import pandas as pd
import time
import random
import matplotlib.pyplot as plt
from collections import defaultdict

from people import People
import BST
import RBT
import HT

def df_to_mas(file_name):
    f = open(file_name, 'r')
    tmp = []
    for i in f.readlines():
        line = i.split(',')
        tmp.append(People(line[0], line[1], line[2], line[3], line[4], i))
    f.close()
    return tmp

df_1 = df_to_mas('data_1.csv') #200
df_2 = df_to_mas('data_2.csv') #500
df_3 = df_to_mas('data_3.csv') #1000
df_4 = df_to_mas('data_4.csv') #5000
df_5 = df_to_mas('data_5.csv') #10000
df_6 = df_to_mas('data_6.csv') #50000
df_7 = df_to_mas('data_7.csv') #100000
df_8 = df_to_mas('data_8.csv') #150000

# Бинарное дерево
BST_time_creating = []
BST_time_searching = []

start = time.time()
root_tmp = BST.create_tree(df_1.copy())
BST_time_creating.append(time.time() - start)

elem = df_1[random.randint(0, len(df_1)-1)].name
print(elem)
start = time.time()
print(BST.search_BST(root_tmp, elem))
BST_time_searching.append(time.time() - start)

# Красночёрное дерево
RBT_time_creating = []
RBT_time_searching = []

start = time.time()
rbt = RBT.RedBlackTree()
rbt.build_from_list(df_1.copy())
RBT_time_creating.append(time.time() - start)

elem = df_1[random.randint(0, len(df_1)-1)].name
print(elem)
start = time.time()
print(rbt.find_element(rbt.root, elem))
RBT_time_searching.append(time.time() - start)

# Хеш таблица
HT_time_creating = []
HT_time_searching = []

start = time.time()
ht_1 = []
for i in df_1:
    HT.add(i, ht_1)
HT_time_creating.append(time.time() - start)

elem = df_1[random.randint(0, len(df_1)-1)].name
print(elem)
start = time.time()
print(HT.search_HT(elem, ht_1))
HT_time_searching.append(time.time() - start)


def df_to_multimap(df):
	tmp = defaultdict(list)
	for i in df:
		tmp[i.name].append(i)
	return tmp

mm_1 = df_to_multimap(df_1)
mm_2 = df_to_multimap(df_2)
mm_3 = df_to_multimap(df_3)
mm_4 = df_to_multimap(df_4)
mm_5 = df_to_multimap(df_5)
mm_6 = df_to_multimap(df_6)
mm_7 = df_to_multimap(df_7)
mm_8 = df_to_multimap(df_8)

mm_time_searching = []
elem = df_1[random.randint(0, len(df_1)-1)].name
print(elem)
start = time.time()
print(mm_1[elem])
mm_time_searching.append(time.time() - start)