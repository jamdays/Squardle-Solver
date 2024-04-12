"""This file is Copyright (c) Oscar Heath, Max Djaya, Punpun Payapvattanavong, Aayush Karki"""

import time
import pandas as pd
import plotly.express as plt
from project import (Tree, Squaredle, make_squaredle, find_words, brute_force)

"""Project 2 Tests"""

with open("dictionary.txt") as dic:
    words = set()
    lines = dic.readlines()
    for line in lines:
        words.add(line.strip())


times = {}

# TEST 1: Normal Daily Squaredle
start = time.time()
word_tree = Tree('Start')

with open('dictionary.txt') as word_dict:
    for line in word_dict.readlines():
        line_stripped = line.strip()
        if len(line_stripped) >= 4:
            word_tree.add_string(line_stripped)
squaredle = make_squaredle('yesterday.txt')
graph = Squaredle(squaredle)
WORD_LIST = find_words(graph, word_tree)
end = time.time()
elapsed = (abs(end - start))
times["Time"] = [elapsed]
times["Name"] = ['Normal']

# TEST 2: Normal Daily Squaredle Brute Force
start = time.time()
squaredle = make_squaredle('yesterday.txt')
graph = Squaredle(squaredle)
brute_force(graph, words)
end = time.time()
elapsed = (abs(end - start))
times["Time"].append(elapsed)
times["Name"].append('Normal_brute_force')

# TEST 3: Extra Long Squardle
start = time.time()

word_tree = Tree('Start')

with open('dictionary.txt') as word_dict:
    for line in word_dict.readlines():
        line_stripped = line.strip()
        if len(line_stripped) >= 4:
            word_tree.add_string(line_stripped)

squaredle = make_squaredle('extra_long.txt')
graph = Squaredle(squaredle)
WORD_LIST = find_words(graph, word_tree)
end = time.time()

elapsed = (abs(end - start))
times["Time"].append(elapsed)
times["Name"].append("Extra Long")

df = pd.DataFrame(times)
print(df)
fig = plt.bar(df, x='Name', y="Time")
fig.show()
