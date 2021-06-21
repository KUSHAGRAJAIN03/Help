# Import writer class from csv module
import csv
from tkinter import Text
import pandas as pd
from csv import DictReader
import numpy as np
import datetime
from datetime import date, timedelta
from datetime import datetime
import decimal
from dateutil.rrule import rrule, DAILY
from datetime import *
from tempfile import NamedTemporaryFile
import shutil
import csv

op=True

def float_range(start, stop, step):
  while start < stop:
    yield float(start)
    start += decimal.Decimal(step)
x = True
List=[]
s=0
y=0.0
z=0
df=''
while (x==True):
    t = str(input(">"))
    if (t == '0'):
        a = str(input("Date : "))
        b = float(input("Haudi Katai Paddy(40Kg,30Kg)Nob : "))
        c = float(input("Rate : "))
        d = float(input("Haudi Katai Rice(60Kg,50Kg)Nob : "))
        e = float(input("Rate : "))
        f = float(input("Paddy Loading(40Kg,30Kg)Nob : "))
        g = float(input("Rate : "))
        h = float(input("Rice Loading(60kg,50kg,40kg)Nob : "))
        i = float(input("Rate : "))
        j = float(input("Rice Loading(25kg)Nob : "))
        k = float(input("Rate : "))
        l = float(input("Polish Loading Nob : "))
        m = float(input("Rate : "))
        n = float(input("Rice Dhala Nob : "))
        o = float(input("Rate : "))
        p = float(input("Bundle Stack/Loading Nob : "))
        q = float(input("Rate : "))
        r = float(input("Advance (if any) : "))
        s = float(b*c+d*e+f*g+h*i+j*k+l*m+n*o+p*q-r)

        # List 
        List=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s]
        
        with open('Records.csv', 'a',newline='') as f_object:
            df = pd.read_csv('Records.csv')

            new_df = df.dropna()

            #print(new_df.to_string())

            writer_object =csv.writer(f_object)
        
            writer_object.writerow(List)

           # f_object.close




    else :
        bd = str(input("Start Date : "))
        ed = str(input("How many days : "))
        pp = 0
        EN = ''
        D = ''
        data = pd.read_csv("Records.csv")
        data.set_index("Date", inplace = True)
        df = data.loc[bd:ed,['Sum','Advance']]
        print(df)