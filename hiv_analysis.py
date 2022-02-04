
from this import s
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics as st

df = pd.read_csv("/Users/jjimm/Documents/Analysis_projects/HIV_AIDS_Diagnoses_by_Neighborhood__Sex__and_Race_Ethnicity.csv")
#print(df.head())

df1 = pd.DataFrame(df)
#print(df1)


def my_function():
    df2 = pd.DataFrame(df1.where(df1['YEAR'] == 2010))
    df3 = df2.dropna(axis=0)
    q = np.array(df3['TOTAL NUMBER OF AIDS DIAGNOSES'])
    r = df3['RACE/ETHNICITY']
    s = df3['TOTAL NUMBER OF HIV DIAGNOSES']
    u = df3['AIDS DIAGNOSES PER 100,000 POPULATION']
    v = df3['HIV DIAGNOSES PER 100,000 POPULATION']
    def graphing1(variable1, variable2): 
        plt.bar(variable1, variable2)
        plt.show()
    print(graphing1(r, s))
    def graphing2(variable1, variable2):
        plt.scatter(variable1, variable2)
        plt.show()
    print(graphing2(q, s))
    def average(numbers):
        a = st.mean(numbers)
        b = st.median(numbers)
    print(average(q))

#print(my_function())


def my_function2():
    df2 = pd.DataFrame(df1.where(df1['YEAR'] == 2011))
    df3 = df2.dropna(axis=0)
    q = df3['TOTAL NUMBER OF AIDS DIAGNOSES']
    r = df3['RACE/ETHNICITY']
    s = df3['TOTAL NUMBER OF HIV DIAGNOSES']
    u = df3['AIDS DIAGNOSES PER 100,000 POPULATION']
    v = df3['HIV DIAGNOSES PER 100,000 POPULATION']
    def graphing(variable1, variable2): 
        plt.bar(variable1, variable2)
        plt.show()
    print(graphing(r, s))
    def graphing2(variable1, variable2):
        plt.scatter(variable1, variable2)
        plt.show()
    print(graphing2(q, s))
    def average(numbers):
        a = st.mean(numbers)
        b = st.median(numbers)
    print(average(q))

#print(my_function2())

def my_function3():
    df2 = pd.DataFrame(df1.where(df1['YEAR'] == 2012))
    df3 = df2.dropna(axis=0)
    q = df3['TOTAL NUMBER OF AIDS DIAGNOSES']
    r = df3['RACE/ETHNICITY']
    s = df3['TOTAL NUMBER OF HIV DIAGNOSES']
    u = df3['AIDS DIAGNOSES PER 100,000 POPULATION']
    v = df3['HIV DIAGNOSES PER 100,000 POPULATION']
    def graphing(variable1, variable2): 
        plt.bar(variable1, variable2)
        plt.show()
    print(graphing(r, s))
    def graphing2(variable1, variable2):
        plt.scatter(variable1, variable2)
        plt.show()
    print(graphing2(q, s))
    def average(numbers):
        a = st.mean(numbers)
        b = st.median(numbers)
    print(average(q))

#print(my_function3())

def my_function4():
    df2 = pd.DataFrame(df1.where(df1['YEAR'] == 2013))
    df3 = df2.dropna(axis=0)
    q = df3['TOTAL NUMBER OF AIDS DIAGNOSES']
    r = df3['RACE/ETHNICITY']
    s = df3['TOTAL NUMBER OF HIV DIAGNOSES']
    u = df3['AIDS DIAGNOSES PER 100,000 POPULATION']
    v = df3['HIV DIAGNOSES PER 100,000 POPULATION']
    def graphing(variable1, variable2): 
        plt.bar(variable1, variable2)
        plt.show()
    print(graphing(r, s))
    def graphing2(variable1, variable2):
        plt.scatter(variable1, variable2)
        plt.show()
    print(graphing2(q, s))
    def average(numbers):
        a = st.mean(numbers)
        b = st.median(numbers)
    print(average(q))

#print(my_function4())









    

























































        








        







