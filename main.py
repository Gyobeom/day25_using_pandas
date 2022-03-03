import pandas

cnt = 0

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrel = len(data[data["Primary Fur Color"] == "black"])
Cinnamon_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(gray_squirrel)

data_dict = {
    "Fur Color" :["Gray","Cinnamon","Black"],
    "Count": [gray_squirrel,Cinnamon_squirrel,black_squirrel]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")