import pandas as pd
df= pd.read_csv("dataset.csv")
print(df.head(50))
print(df.tail(20))

df.info()
print(df["Opposition"].describe())
print(df["BF"].describe())


run_frequency=df["Opposition"].value_counts()
print(run_frequency)

new_df=df[["Runs","SR","Opposition"]]
print(new_df)

vs_aussies=df[df["Opposition"]=="v Australia"]
print(vs_aussies)

# Find all the matches where Virat scored a Century  
tons=df[df["Runs"]>=100]
print(tons)
# Find all the matches where Virat's strike rate was >100   
tons_sr=df[df["SR"]>100]
print(tons_sr)
# Find all the matches where Virat played with Srilanka and scored a century
sril_cent=df[
    (df["Opposition"]=="v Sri Lanka") & (df["Runs"])
]
print(sril_cent)

def find_centuries(x):
    if x>=100:
        return"OG"
    else:
        return"NOOB"  

df["Centuries"]=df["Runs"].apply(find_centuries)
print(df.tail(10))

