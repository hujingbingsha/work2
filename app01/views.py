import re
import json
import django.views.generic
from django.http import HttpResponse
from django.shortcuts import render
import csv
# 创建类视图
from django.views import View
from app01.models import Users


def read():
    file = open(r"C:\Users\25815\PycharmProjects\djangoProject1\app01\templates\学院教师信息.csv", "r")
    data = csv.reader(file)
    for i in data:
        Users.objects.create(name=i[1],Department=i[0],title=i[2],ways=i[3])

def login(request):
    # read()
    if request.method == "GET":
        return render(request, 'index.html')
    else:
        user_input = request.POST.get('q')
        datalist = Users.objects.all()
        for obj in datalist:
            if user_input == obj.name:
                return render(request, "index_2.html",locals())


        value_list = request.POST.getlist('my_value',[])
        list_2 =[]
        for dep in value_list:
            list = Users.objects.filter(Department=dep)
            for i in list:
                list_2.append(i)



        context = {'list':list_2}
        return render(request,"index_3.html",context)





        # value_list = request.POST.getlist("my_value", [])
        #
        # list= []
        # list_in=[]
        # list_ways=[]
        # for dep in value_list: #dep:循环为：数字媒体、传播
        #     for obj_2 in datalist: #onj_2是表单里某个老师的所有信息
        #         if obj_2.Department == dep:
        #             list_ways.append(obj_2.ways)
        #             list_in.append(obj_2.Department)
        #             list_in.append(obj_2.name)
        #             list_in.append(obj_2.title)
        #
        #             list.append(list_in)
        #             list_in=[]
        #
        #
        # return render(request, "index_3.html",locals())
# def teacher_1(request):




