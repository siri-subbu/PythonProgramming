'''Program to
    1.create a customized dictionary with keys as column names and values as data
    2.assign that dictionary to dataframe and display.
    3.Display the dataframe'''

from pandas import *

d={"Name":["Subbu","K.Bhanu Prasad","Madhu",],
    "Registered No":["24635-CM-022","24635-CM-024","24635-CM-020"],
    "Branch":["CME","CME","CME"],
    "College":["Govt Polytechnic college,Chodavaram","Govt Polytechnic college,Chodavaram","Govt Polytechnic college,Chodavaram"]}
    
df=DataFrame(d)
print(df)
