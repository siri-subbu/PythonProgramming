'''Program to
      1.define a dictionary with data
      2.Convert the dictionary to DataFrame
      3.Then DataFrame to csv file.'''

from os import *
from pandas import *

data={'Sid':[1,2,3,4,5],
      'name':['Hyma','Raghu','Subbu','Siri','Lasya'],
      'Age':[35,40,12,15,15]}

df=DataFrame(data)

df.to_csv('Data.csv',index=False)

