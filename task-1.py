import pickle
import pandas as pd
import json
import matplotlib.pyplot as plt

def load_data():
    file = open("Task1Files/data.pkl", "rb")
    data_df = pickle.load(file)
    file.close()

    return data_df['task'].tolist()

def label_data(data_list):
    file = open('Task1Files/names.json', "r")
    name_json = json.loads(file.read())
    file.close()
    
    all_names = []
    
    counter = 0
    isOneStarted = False
    for i in range(len(data_list)):
        if data_list[i] == 1.0 and isOneStarted is False:
            start = i
            isOneStarted = True
        if data_list[i] == 0.0 and isOneStarted:
            end = i
            isOneStarted = False
            counter = counter + 1
            all_names.append([name_json[str(counter)]] * (end-start+1))
            data_list[start:end] = [name_json[str(counter)]] * (end-start+1)
        
    return data_list, all_names
    
def draw_data(name_list):
    _figure = plt.figure()
    _ax = _figure.add_axes([0.1,0.1,0.75,0.75])
    name_len_list = [len(name_list[i]) for i in range(len(name_list))]
    split = name_len_list[0]
    squad = name_len_list[0] + name_len_list[1]
    sl = name_len_list[1] + name_len_list[2] + name_len_list[3] + name_len_list[4] + name_len_list[5] + name_len_list[9]
    bw = name_len_list[2]
    decel = name_len_list[2]
    prone = name_len_list[3]
    curls = name_len_list[3]
    glute = name_len_list[4]
    bridge = name_len_list[4] + name_len_list[5]
    elevated = name_len_list[5]
    glue = name_len_list[5]
    _45deg = name_len_list[6]
    adductor = name_len_list[6] + name_len_list[7]
    squeeze = name_len_list[6] + name_len_list[7]
    _0deg = name_len_list[7]
    copenhagen = name_len_list[8]
    straight = name_len_list[9]
    knee = name_len_list[9]
    calf = name_len_list[9]
    _raise = name_len_list[9]
    counts = [split, squad, sl, bw, decel, prone, curls, glute, bridge, elevated, glue, _45deg, adductor, squeeze, _0deg, copenhagen, straight, knee, calf, _raise]
    words = ['split', 'squad', 'SL', 'BW', 'Decel', 'prone', 'curls', 'glute', 'bridge', 'elevated', 'glue', '45deg', 'adductor', 'squeeze', '0deg', 'copenhagen', 'straight', 'knee', 'calf', 'raise']
    _ax.bar(words, counts)
    _ax.set_title("Word Count")
    plt.setp(_ax.get_xticklabels(), rotation=30, horizontalalignment='right', fontsize='x-small')
    plt.savefig("task1-graph.png")

data_list = load_data()
data_list, name_list = label_data(data_list)
draw_data(name_list)
[print(item) for item in data_list]
