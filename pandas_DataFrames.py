'''Program to 
    1.import all components of pandas
    2.Read a csv file
    3.Print the csv file that is read.
    4.print head,tail,info and description of the file using methods of DataFrames in pandas'''

from pandas import *

df=read_csv('/home/ksns-sarwani/ubuntu/Documents/DBMS_data/Employee.csv')
print(df)
print("\n")
print("First five records")
print(df.head)
print("\n")
print("last five records")
print(df.tail())
print("\n")
print("Info")
print(df.info())
print("\n")
print("Description")
print(df.describe())

