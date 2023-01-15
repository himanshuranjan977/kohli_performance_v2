# kholi_performance_v2

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("dataset.csv")
print(df.head())

# Find all the matches where Virat scored a Century  
print("Totals runs :" ,df ["Runs"].sum())

# Find all the matches where Virat's strike rate was >100   
print("Strike Rate:", df["BF"].sum())

# Find all the matches where Virat played with Srilanka and scored a century
print("Avg strike rate",df["SR"].mean())

#  Number of mathes he has played at different  position kholi played
print(df["Pos"].head(10))

position=df["Pos"].unique
print(position)

df["Pos"]=df["Pos"].map({
    3.0:"Batting at 3",
    4.0:"Batting at 4",
    2.0:"Batting at 2",
    1.0:"Batting at 1",
    5.0:"Batting at 5",
    6.0:"Batting at 6",
})
print(df[["Runs","Pos"]])
pos_counts=df["Pos"].value_counts()
print(pos_counts)
#print("Listof the position he has played",df["Pos"].unique())

# Total run scored in different positions 
pos_counts_values=pos_counts.values
pos_counts_labels=pos_counts.index

fig=plt.figure(figsize=(10,7))
plt.pie(pos_counts_values,labels=pos_counts_labels)
plt.show()

# Total sixex scored in different grounds againsts different oppositions
def show_pie_plots(df,key):
    counts=df[key].value_counts()
    print(counts)
    counts_values=counts.values
    counts_labels=counts.index
    fig=plt.figure(figsize=(10,7))
    plt.pie(counts_values,labels=counts_labels)
    plt.show()

#  Number of mathes he has played at different Opposition
show_pie_plots(df,"Opposition")    

#numberof matches he has played at grounds
show_pie_plots(df,"Ground")
#total sixes scored in different positions
runs_at_pos=df.groupby("Pos")["6s"].sum()
print(runs_at_pos,type(runs_at_pos))
runs_at_pos_values=runs_at_pos.values
runs_at_pos_labels=runs_at_pos.index

fig=plt.figure(figsize=(10,7))
plt.bar(
    runs_at_pos_labels,
    runs_at_pos_values,
    color="green",
    width=0.3
)
plt.show()

# Total runs scored with different countries 
run_with_countries=df.groupby("Runs")["Opposition"].sum()
run_with_countries_values=run_with_countries.values
run_with_countries_labels=run_with_countries.index

plt.bar(
    run_with_countries_labels,
    run_with_countries_values,
    color="blue",
    width=0.3
)
