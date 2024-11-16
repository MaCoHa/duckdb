
from collections import defaultdict
from dataclasses import dataclass
import json
from typing import Any

from matplotlib import pyplot as plt
import pandas as pd



# timings are 5 measurement for each querry

# log_sf* are 5 measurement for each querry



markers = ['o', 's', '^', 'D', 'v']
line_styles = ['-', '--', '-.', ':', '-']

def plot_lines(x, ys, title="Line Plot", xlabel="X-axis", ylabel="Y-axis", filename="line_plot.png"):
    #plt.figure(figsize=(8, 6))
    for index, key in enumerate(ys):
        data = ys[key]
        marker = markers[index]
        line_style = line_styles[index]
        plt.plot(x, data, marker=marker, linestyle=line_style, label=key)


    plt.legend()
    plt.title(title, fontsize=20)
    plt.xlabel(xlabel, fontsize=16)
    plt.ylabel(ylabel, fontsize=16)
    plt.grid(True)
    plt.savefig(f"plots/{filename}", format='png')
    plt.close()  # Close the figure after saving 
    
def reader_json(file: str,dict,vaiable:str):
    profilings = []
    with open(file) as f:
        buffer = []

        for line in f:
            buffer.append(line)

            if line.rstrip() == "}":
                profile = json.loads(''.join(buffer))
                profilings.append(profile)
                buffer.clear()
    i = 0
    counter = 1
    query = ["Q1","Q7","Q12"]
    cumulative_rows_scanned = 0
    cumulative_cardinality = 0
    for profile in profilings:
       
       
        cumulative_rows_scanned += profile["cumulative_rows_scanned"]
        cumulative_cardinality += profile["cumulative_cardinality"]
        if counter % 5 == 0:
            counter = 1
            dict[vaiable][query[i]]["cumulative_rows_scanned"] = cumulative_rows_scanned / 5
            dict[vaiable][query[i]]["cumulative_cardinality"] = cumulative_cardinality / 5   
             
            cumulative_rows_scanned = 0
            cumulative_cardinality = 0
            i += 1
        else:   
            counter += 1

def reader_timings(file:str,dict,vaiable):
    i = 0
    counter = 1
    query = ["Q1","Q7","Q12"]
    time = 0
    with open(file, 'r') as file:
        for line in file:
            time += float(line.strip())
            if counter % 5 == 0:
                counter = 1
                dict[vaiable][query[i]]["time"] = time / 5 
                i += 1
                time = 0             
            else:   
                counter += 1
            
            
thread_dict = defaultdict(lambda: defaultdict(lambda: defaultdict(float)))       
scale_factore_dict = defaultdict(lambda: defaultdict(lambda: defaultdict(float)))       
              
        
reader_json("log_sf1_t1.json",thread_dict,"t1")
reader_json("log_sf1_t4.json",thread_dict,"t4")
reader_json("log_sf1_t8.json",thread_dict,"t8")
reader_timings("timings_sf1_t1.csv",thread_dict,"t1")
reader_timings("timings_sf1_t4.csv",thread_dict,"t4")
reader_timings("timings_sf1_t8.csv",thread_dict,"t8")

reader_json("log_sf1_t4.json",scale_factore_dict,"sf1")
reader_json("log_sf10_t4.json",scale_factore_dict,"sf10")
reader_json("log_sf100_t4.json",scale_factore_dict,"sf100")
reader_timings("timings_sf1_t4.csv",scale_factore_dict,"sf1")
reader_timings("timings_sf10_t4.csv",scale_factore_dict,"sf10")
reader_timings("timings_sf100_t4.csv",scale_factore_dict,"sf100")


dict = defaultdict(lambda: defaultdict(list))
dict["time"]["Q1"] = [thread_dict["t1"]["Q1"]["time"],thread_dict["t4"]["Q1"]["time"],thread_dict["t8"]["Q1"]["time"]]
dict["time"]["Q7"] = [thread_dict["t1"]["Q7"]["time"],thread_dict["t4"]["Q7"]["time"],thread_dict["t8"]["Q7"]["time"]]
dict["time"]["Q12"] = [thread_dict["t1"]["Q12"]["time"],thread_dict["t4"]["Q12"]["time"],thread_dict["t8"]["Q12"]["time"]]

dict["cumulative_rows_scanned"]["Q1"] = [thread_dict["t1"]["Q1"]["cumulative_rows_scanned"]/1_000_000,thread_dict["t4"]["Q1"]["cumulative_rows_scanned"]/1_000_000,thread_dict["t8"]["Q1"]["cumulative_rows_scanned"]/1_000_000]
dict["cumulative_rows_scanned"]["Q7"] = [thread_dict["t1"]["Q7"]["cumulative_rows_scanned"]/1_000_000,thread_dict["t4"]["Q7"]["cumulative_rows_scanned"]/1_000_000,thread_dict["t8"]["Q7"]["cumulative_rows_scanned"]/1_000_000]
dict["cumulative_rows_scanned"]["Q12"] = [thread_dict["t1"]["Q12"]["cumulative_rows_scanned"]/1_000_000,thread_dict["t4"]["Q12"]["cumulative_rows_scanned"]/1_000_000,thread_dict["t8"]["Q12"]["cumulative_rows_scanned"]/1_000_000]

dict["cumulative_cardinality"]["Q1"] = [thread_dict["t1"]["Q1"]["cumulative_cardinality"]/1_000_000,thread_dict["t4"]["Q1"]["cumulative_cardinality"]/1_000_000,thread_dict["t8"]["Q1"]["cumulative_cardinality"]/1_000_000]
dict["cumulative_cardinality"]["Q7"] = [thread_dict["t1"]["Q7"]["cumulative_cardinality"]/1_000_000,thread_dict["t4"]["Q7"]["cumulative_cardinality"]/1_000_000,thread_dict["t8"]["Q7"]["cumulative_cardinality"]/1_000_000]
dict["cumulative_cardinality"]["Q12"] = [thread_dict["t1"]["Q12"]["cumulative_cardinality"]/1_000_000,thread_dict["t4"]["Q12"]["cumulative_cardinality"]/1_000_000,thread_dict["t8"]["Q12"]["cumulative_cardinality"]/1_000_000]

plot_lines(["t1","t4","t8"], 
        dict["time"], 
        title=f"Elasped time for querys with\n diffrent threads", 
        xlabel="Amount of threads", 
        ylabel="Elapsed Time (ms)", 
        filename=f"threads_elapsed_time.png")
plot_lines(["t1","t4","t8"], 
        dict["cumulative_rows_scanned"], 
        title=f"Cumulative rows scanned with\n diffrent threads", 
        xlabel="Amount of threads", 
        ylabel="million rows scanned", 
        filename=f"threads_cumulative_rows_scanned.png")

plot_lines(["t1","t4","t8"], 
        dict["cumulative_cardinality"], 
        title=f"Cumulative cardinality with\n diffrent threads", 
        xlabel="Amount of threads", 
        ylabel="million cardinalitys", 
        filename=f"threads_cumulative_cardinality.png")



dict = defaultdict(lambda: defaultdict(list))
dict["time"]["Q1"] = [scale_factore_dict["sf1"]["Q1"]["time"],scale_factore_dict["sf10"]["Q1"]["time"],scale_factore_dict["sf100"]["Q1"]["time"]]
dict["time"]["Q7"] = [scale_factore_dict["sf1"]["Q7"]["time"],scale_factore_dict["sf10"]["Q7"]["time"],scale_factore_dict["sf100"]["Q7"]["time"]]
dict["time"]["Q12"] = [scale_factore_dict["sf1"]["Q12"]["time"],scale_factore_dict["sf10"]["Q12"]["time"],scale_factore_dict["sf100"]["Q12"]["time"]]

dict["cumulative_rows_scanned"]["Q1"] = [scale_factore_dict["sf1"]["Q1"]["cumulative_rows_scanned"]/1_000_000,scale_factore_dict["sf10"]["Q1"]["cumulative_rows_scanned"]/1_000_000,scale_factore_dict["sf100"]["Q1"]["cumulative_rows_scanned"]/1_000_000]
dict["cumulative_rows_scanned"]["Q7"] = [scale_factore_dict["sf1"]["Q7"]["cumulative_rows_scanned"]/1_000_000,scale_factore_dict["sf10"]["Q7"]["cumulative_rows_scanned"]/1_000_000,scale_factore_dict["sf100"]["Q7"]["cumulative_rows_scanned"]/1_000_000]
dict["cumulative_rows_scanned"]["Q12"] = [scale_factore_dict["sf1"]["Q12"]["cumulative_rows_scanned"]/1_000_000,scale_factore_dict["sf10"]["Q12"]["cumulative_rows_scanned"]/1_000_000,scale_factore_dict["sf100"]["Q12"]["cumulative_rows_scanned"]/1_000_000]

dict["cumulative_cardinality"]["Q1"] = [scale_factore_dict["sf1"]["Q1"]["cumulative_cardinality"]/1_000_000,scale_factore_dict["sf10"]["Q1"]["cumulative_cardinality"]/1_000_000,scale_factore_dict["sf100"]["Q1"]["cumulative_cardinality"]/1_000_000]
dict["cumulative_cardinality"]["Q7"] = [scale_factore_dict["sf1"]["Q7"]["cumulative_cardinality"]/1_000_000,scale_factore_dict["sf10"]["Q7"]["cumulative_cardinality"]/1_000_000,scale_factore_dict["sf100"]["Q7"]["cumulative_cardinality"]/1_000_000]
dict["cumulative_cardinality"]["Q12"] = [scale_factore_dict["sf1"]["Q12"]["cumulative_cardinality"]/1_000_000,scale_factore_dict["sf10"]["Q12"]["cumulative_cardinality"]/1_000_000,scale_factore_dict["sf100"]["Q12"]["cumulative_cardinality"]/1_000_000]

plot_lines(["sf1","sf10","sf100"], 
        dict["time"], 
        title=f"Elasped time for querys with\n diffrent scale factore", 
        xlabel="Scale factore", 
        ylabel="Elapsed Time (ms)", 
        filename=f"SF_elapsed_time.png")
plot_lines(["sf1","sf10","sf100"], 
        dict["cumulative_rows_scanned"], 
        title=f"Cumulative rows scanned with\n diffrent scale factore", 
        xlabel="Scale factore", 
        ylabel="million rows scanned", 
        filename=f"SF_cumulative_rows_scanned.png")

plot_lines(["sf1","sf10","sf100"], 
        dict["cumulative_cardinality"], 
        title=f"Cumulative cardinality with\n diffrent scale factore", 
        xlabel="Scale factore", 
        ylabel="million cardinalitys", 
        filename=f"SF_cumulative_cardinality.png")