from django.shortcuts import render, redirect
from django.http.response import HttpResponse
import json
import pandas as pd
import csv
from collections import Counter
from .models import *
"""
with open("./draw.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    for cell in csvreader:
       # print(cell[0], cell[1])
    
        data = DATA(date_of_drow= cell[0], 
                ball1=cell[1], ball2=cell[2],ball3=cell[3],
                ball4=cell[4],ball5=cell[5],lucky1=cell[6],lucky2=cell[7])
        data.save()
    
"""
jan = []
feb = []
mar = []
may = []
jun = []
jul = []
aug = []
sep = []
oct = []
nov = []
dec = []


month_data =[]
data1 = DATA.objects.all()


# Create your views here.
def index(request):
    data1 = DATA.objects.all()
    #print(data1)
    Month = []
    monts =[]

    for i in data1:
        
       
        for m in i.date_of_drow.split('-'):
            if m == 'Jan':
                Month.append(m)
            elif m == 'Feb':
                Month.append(m)
            elif m == 'Mar':
               Month.append(m)
            elif m == 'Apr':
                Month.append(m)
            elif m == 'May':
               Month.append(m)
            elif m == 'Jun':
               Month.append(m)
            elif m == 'Jul':
               Month.append(m)
            elif m == 'Aug':
               Month.append(m)
            elif m == 'Sep':
                Month.append(m)
            elif m == 'Oct':
                Month.append(m)
            elif m == 'Nov':
                Month.append(m)
            elif m == 'Dec':
                Month.append(m)
            #print (m)
        
    #for key, value in Month:

    #print(set(Month))    
    
    return render(request, 'data/index.html', {'data':data1,
                                               'month':m, 'dic':set(Month)})

def months(request, month):
    cont = 0
    br_cont = 0
    occurance = []
    data_month = []

    input_number = request.POST.get('InputNumber')
    for i in data1:
        br_cont += 1

        for m in i.date_of_drow.split('-'):
            if m == month:  
               data_month.append(i)
               occurance.append(i.ball1)
               for n in  occurance:
                   if n in occurance:
                       cont += 1
                   
                #print(i)
            
    values = Counter(occurance)
    num = values[input_number]
    #data_month.sort_values('date_of_drow', inplace=True)
    #data_month.drop_duplicates(subset='date_of_drow', keep=False, inplace=True)
    #data = list(dict.fromkeys(data_month))

    new_cont = 0
    new_data = []
    for new in data_month:
        new_cont += 1
        if new not in new_data:
          
            new_data.append(new)

    remove = new_cont - 2 

    print(new_data[:-remove])

    return render(request, 'data/month.html', { 'data': data_month, 'month':month, 'count':num} )
     #return redirect('index')
    #return HttpResponse(json.dumps(dish_data), content_type="application/json")


# need to work more on this 
def pyMonth(requet):
    #print(month_data)
    m = set()
    for key, value in month_data:
       print(key)
      # m.add(d)

    return render(requet, 'data/month.html', { 'data':m })
 

def month(request):
   
    for i in data1:
            for m in i.date_of_drow.split('-'):
                if m == 'Jan':
                    month_data.append({'month':m,'data1':i.ball1,
                                       'date2':i.ball2,'data3':i.ball3,'data4':i.ball5,'luckey1':i.lucky1,'luckey2':i.lucky2})
                elif m == 'Feb':
                    month_data.append({'month':m,'data1':i.ball1,
                                       'date2':i.ball2,'data3':i.ball3,'data4':i.ball5,'luckey1':i.lucky1,'luckey2':i.lucky2})
                elif m == 'Mar':
                    month_data.append({'month':m,'data1':i.ball1,
                                       'date2':i.ball2,'data3':i.ball3,'data4':i.ball5,'luckey1':i.lucky1,'luckey2':i.lucky2})
                elif m == 'Apr':
                    month_data.append({'month':m,'data1':i.ball1,
                                       'date2':i.ball2,'data3':i.ball3,'data4':i.ball5,'luckey1':i.lucky1,'luckey2':i.lucky2})
                elif m == 'May':
                    month_data.append({'month':m,'data1':i.ball1,
                                       'date2':i.ball2,'data3':i.ball3,'data4':i.ball5,'luckey1':i.lucky1,'luckey2':i.lucky2})
                elif m == 'Jun':
                    month_data.append({'month':m,'data1':i.ball1,
                                       'date2':i.ball2,'data3':i.ball3,'data4':i.ball5,'luckey1':i.lucky1,'luckey2':i.lucky2})
                elif m == 'Jul':
                    month_data.append({'month':m,'data1':i.ball1,
                                       'date2':i.ball2,'data3':i.ball3,'data4':i.ball5,'luckey1':i.lucky1,'luckey2':i.lucky2})
                elif m == 'Aug':
                    month_data.append({'month':m,'data1':i.ball1,
                                       'date2':i.ball2,'data3':i.ball3,'data4':i.ball5,'luckey1':i.lucky1,'luckey2':i.lucky2})
                elif m == 'Sep':
                    month_data.append({'month':m,'data1':i.ball1,
                                       'date2':i.ball2,'data3':i.ball3,'data4':i.ball5,'luckey1':i.lucky1,'luckey2':i.lucky2})
                elif m == 'Oct':
                    month_data.append({'month':m,'data1':i.ball1,
                                       'date2':i.ball2,'data3':i.ball3,'data4':i.ball5,'luckey1':i.lucky1,'luckey2':i.lucky2})
                elif m == 'Nov':
                    month_data.append({'month':m,'data1':i.ball1,
                                       'date2':i.ball2,'data3':i.ball3,'data4':i.ball5,'luckey1':i.lucky1,'luckey2':i.lucky2})
                elif m == 'Dec':
                    month_data.append({'month':m,'data1':i.ball1,
                                       'date2':i.ball2,'data3':i.ball3,'data4':i.ball5,'luckey1':i.lucky1,'luckey2':i.lucky2})
    #print(month_data)
    return HttpResponse(json.dumps(month_data), content_type="application/json")


