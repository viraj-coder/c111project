import plotly.figure_factory as ff
import statistics
import random
import pandas as pd
import csv

df=pd.read_csv("data.csv")
data=df["temp"].tolist()
population_mean=statistics.mean(data)
std_deviation=statistics.stdev(data)


def show_fig(mean_list):
    df=mean_list
    fig=ff.create_distplot([data],["temp"],show_hist=False)
    fig.add_trace(go.scatter(x=[mean,mean],y=[0,1],mode="lines",name="MEAN"))
    fig.show()

def random_set_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    std_deviation=statistics.stdev(dataset)

    print("population mean",population_mean)
    print("standard deviation",std_deviation)
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df], ["temp"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="MEAN"))
    fig.show()


# Pass the number of time you want the mean of the data points as a parameter in range function in for loop
def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means= random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    
    mean = statistics.mean(mean_list)
    print("Mean of sampling distribution :-",mean )

setup()


#Code to find the mean of the raw data ("population data")
population_mean = statistics.mean(data)
print("population mean:- ", population_mean)


# code to find the standard deviation of the sample data
def standard_deviation():
    mean_list = []
    for i in range(0,1000):
        set_of_means= random_set_of_mean(100)
        mean_list.append(set_of_means)

    std_deviation = statistics.stdev(mean_list)
    print("Standard deviation of sampling distribution:- ", std_deviation)

standard_deviation()