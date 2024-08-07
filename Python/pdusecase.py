import pandas as pd

df = pd.read_csv("cars.csv")
# df = pd.read_csv("https://raw.githubusercontent.com/mpandurangan/datasets/blob/main/cars.csv")
print(df)

#remove null rows
df.dropna(axis=0,inplace=True,)

# df.set_index('car_id', inplace=True)

print(df.loc[df["model_year"].isin(2023,2022)])
# print(df[["car_id","color"]])

# df.insert(3, 'status', ['latest' if model_year > 2022 else 'old' for model_year in df['model_year']])

# print(df.index)

#git clone 

# #To fix that date
# df = df.replace('"', '', regex=True)

# df['production_date'] = pd.to_datetime(df['production_date'])
# #strftime("%d/%M/%Y")

# # To remove duplicates

# df.drop_duplicates(subset=df.columns.difference(['car_id']),inplace=True)


# #Remove inappropriate engine type
# df = df.query("engine_type in ['Gas','Hybrid','Diesel']")

# #df[df["engine_type"].loc(~['Gas','Hybrid','Diesel'])]

# #To remove empty cells rew
# df = df.replace(' ','',regex=True)

# df = df[df.color != '']

# print("-----cleaned data\n",df)

# #Mean, Median , STD

# print("production_date------mean",df["production_week"].mean())

# print("production_date------median",df["production_week"].median())

# print("production_date------SD",df["production_week"].std())

# print("model_year------mean",df["model_year"].mean())

# print("model_year------median",df["model_year"].median())

# print("model_year------SD",df["model_year"].std())
#.mode()

# #categorical columns count
# print("distribution of categorical columns using values count",df['engine_type'].value_counts(),df['color'].value_counts(),df['model_name'].value_counts(),end="\n")

# #Count cars by year
# # print(df.count(axis=0))

# print("Total number of cars produced by year",df.groupby(['model_year']).size())


#select model_year,color,count(color) as cnt from cars group by model_year,color order by cnt desc





