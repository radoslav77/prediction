from django.shortcuts import render
from django.http.response import HttpResponse
import json
import csv
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

data1 = DATA.objects.all()
# Create your views here.
def index(request):
    data1 = DATA.objects.all()
    #print(data1)
    
    monts =[]

    for i in data1:
        
       
        for m in i.date_of_drow.split('-'):
            if m == 'Jan':
                jan.append(i)
            elif m == 'Feb':
                feb.append(i)
            elif m == 'Mar':
                mar.append(i)    
            #print (m)
        
            #print(m)    
    return render(request, 'data/index.html', {'data':data1,
                                               'month':m})

def months(request, month):
    monthData = []
    for i in data1:
        
        for m in i.date_of_drow.split('-'):
            if m == month:
                monthData.append(i)
    #print(monthData)
    
    #return HttpResponse(json.dumps(dish_data), content_type="application/json")

    pass

def month(request):
    month_data =[]
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
    print(month_data)
    return HttpResponse(json.dumps(month_data), content_type="application/json")


