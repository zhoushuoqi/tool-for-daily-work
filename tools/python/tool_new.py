# -*- coding: utf-8 -*-
import csv
import os
import pandas as pd
import pandas
import time
from collections import Counter
from tabulate import tabulate

def covert(fpath):
    xls = pd.read_excel(fpath, sheet_name='Total')
    xls2 = pd.read_excel(fpath, sheet_name='NODE Pre-code')
    xls3 = pd.read_excel(fpath, sheet_name='pre')
    xls.to_csv('./tools/python/csv/precondition.csv', index=False)
    xls2.to_csv('./tools/python/csv/node.csv', index=False)
    xls3.to_csv('./tools/python/csv/all_pre.csv', index=False)



def pre_progress():


    with open('./csv/precondition.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        column = [row[1] for row in reader]
    with open('./csv/node.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        column2 = [row[1] for row in reader]
    with open('./csv/all_pre.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        column3 = [row[0] for row in reader]
    return column,column2,column3

def addnodevalue():
    column,column2,column3 = pre_progress()
    a =[]
    mydict = {}
    for pre in column2:
        with open('./csv/node.csv', 'rb') as csvfile:
            reader2 = csv.DictReader(csvfile)
            for row in reader2:
                if row['NODE Name'] == pre:
                    b = [row['Pre-code']]
                    k = pre
                    for element in b:
                        parts = element.split(',')
                        a.append(parts)
                    v = parts
                    mydict[k] = v
    return a,mydict,column,column2,column3
def check():
    node,mydict,column,column2,column3 = addnodevalue()
    list_of_lists = []
    with open('./csv/precondition.csv', 'rb') as csvfile:
        reader2 = csv.DictReader(csvfile)
        for i in column:
            check = []
            nodeNo = []
            error1= []
            for row in reader2:
                if row['Case_ID'] == i:
                    a = [row['Precondition']]
                    package = [row['Package']]
                    for element in a:
                        parts = element.split(',')
                    for x in node:
                            if set(parts).issubset(set(x)) is True:
                                check.append(x)
                    break
                    
            if len(check) == 0:
                list2 = 'no match'
                a = ",".join(a)
                package = ",".join(package)
                list_of_lists.append([i, a, package, 'not match'])
            else:
                nodelist = []
                for nodecheck in check:
                    for name, value in mydict.iteritems():
                        if value == nodecheck:
                            nodelist.append(name)
                a = ",".join(a)
                package = ",".join(package)
                nodelist = ",".join(nodelist)
                list_of_lists.append([i, a, package, nodelist])

    df = pd.DataFrame(list_of_lists, columns=['case_id', 'pre', 'package', 'node'])
    df.to_csv('./result/result.csv', index=False)
def checkpre():
    node,mydict,column,column2,column3 = addnodevalue()
    list_of_lists=[]
    with open('./csv/precondition.csv', 'rb') as csvfile:
        reader2 = csv.DictReader(csvfile)
        for i in column:
            for row in reader2:
                if row['Case_ID'] == i:
                    a = [row['Precondition']]
                    for element in a:
                        parts = element.split(',')
                    flag = True
                    for element3 in parts:
                        if element3 not in column3:
                            flag = False
                            error = element3
                            break
                        else:
                            flag = True
                    if flag:
                        pass
                        break
                    else:
                        list_of_lists.append([i, error])
                        break
    df = pd.DataFrame(list_of_lists, columns=['case_id', 'error'])
    df.to_csv('./result/check_error.csv', index=False)
    return list_of_lists
def count():
    with open('./result/result.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        column = [row[3] for row in reader]

    with open('./csv/node.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        column2 = [row[1] for row in reader]

    All = []
    All2 = []
    for element in column:
        parts = element.split(',')
        for element2 in parts:
            All.append(element2)

    dict1 = Counter(All)

    for element in column:
        if len(element) == 6 or len(element) == 7:
            All2.append(element)
    dict2 = Counter(All2)

    df = pd.DataFrame(dict1.items(), columns=['No.', 'can on this node'])
    df['only can on this node'] = df['No.'].map(dict2)
    df.to_csv('./result/count.csv',index = False)


    print df
def count2():
    column,column2,column3 = pre_progress()
    with open('./csv/precondition.csv', 'rb') as csvfile:
        reader2 = csv.DictReader(csvfile)
        count2_dict = dict()
        count2_dict2 = dict()
        for row in reader2:
            for i in column3:
                if i in row['Precondition']:
                    a = row['Case_ID']
                    count2_dict.setdefault(i,set()).add(a) 

    data = [['pre','No.','casename']]
    countlist = []
    for value in count2_dict:
        value_list = count2_dict[value]
        count = len(value_list)
        name = ",".join(value_list)
        countlist.append([value,count,name])
    df = pd.DataFrame(countlist, columns=['pre_name', 'count', 'casename'])
    df.to_csv('./result/count2.csv', index=False)
            
def count3():
	column,column2,column3 = pre_progress()
	a =[]
	for pre in column2:
            with open('./csv/node.csv', 'rb') as csvfile:
			reader2 = csv.DictReader(csvfile)
			for row in reader2:
				if row['NODE Name'] == pre:
					b = [row['Pre-code']]
					k = pre
					for element in b:
						parts = element.split(',')
						for i in parts:
							if i not in a:
								a.append(i)
							else:
								pass
						
	return a

def count4():
    column,column2,column3 = pre_progress()
    all_precode = count3()
    mydict = dict()
    for i in all_precode:
        for pre in column2:
            with open('./csv/node.csv', 'rb') as csvfile:
			reader2 = csv.DictReader(csvfile)
			for row in reader2:
				if row['NODE Name'] == pre:
					b = [row['Pre-code']]
					for element in b:
						parts = element.split(',')
                                        if i in parts:
                                            mydict.setdefault(i,set()).add(pre) 
    countlist = []
    for value in mydict:
        value_list = mydict[value]
        count = len(value_list)
        name = ",".join(value_list)
        countlist.append([value,count,name])
    df = pd.DataFrame(countlist, columns=['pre_name', 'count', 'nodename'])
    df.to_csv('./result/count3.csv', index=False)
    print mydict
count4()
