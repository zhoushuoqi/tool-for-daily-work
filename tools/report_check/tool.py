# -*- coding: utf-8 -*-
import csv
import os
import glob
import re
import pandas
import pandas as pd


def covert(fpath):
	df = pd.read_excel(fpath)
	df.to_csv('./tools/report_check/file/report.csv', encoding='utf-8')

def check_report(logpath):
	#logpath = raw_input("Input the log file path:")


	with open('./tools/report_check/file/report.csv', 'rb') as csvfile:
		reader = csv.reader(csvfile)
		next(reader)
		column = [row[4] for row in reader]
	with open('./tools/report_check/file/all.csv', 'rb') as csvfile:
		reader = csv.reader(csvfile)
		column2 = [row[0] for row in reader]

	list_of_lists = []
	with open('./tools/report_check/file/report.csv', 'rb') as csvfile,open('./tools/report_check/file/all.csv', 'rb') as csvfile2:
		reader2 = csv.DictReader(csvfile)
		reader3 = csv.DictReader(csvfile2)
		list2 = list(reader2)
		list3 = list(reader3)
		for i in column:
			for row in list2: 
				for row2 in list3:
					if row['Case Id'] == i and row2['name'] == i:
						a=row['Status']
						link=row['Result Link']
						code1=row['Error Code']
						msg=row['Error Message']
						msg = msg[11:]
						b = row2['Expected result']
						checkpoint = [row2['CheckNo']]
						code2 = row2['Code']
						if b == 'Success':
							if a == b:
								partscheck = checkpoint[0]
								if partscheck == 'manual check':
									list_of_lists.append([i,b,a,msg,partscheck,'fail','manual check',link])
									print i,'ok'
								else:
									checkpointlist = []
									path2 = glob.glob('%s/*_%s'%(logpath,i))
									path2 = path2[0]
									file='case_log.txt'
									full_path=os.path.join(path2,file)
									with open(full_path,'r') as f2: 
										contents = f2.read()
										for element in checkpoint:
											parts = element.split(',')
											flag = True
											for element3 in parts:
												if element3 not in contents:
													flag=False
													error = element3
													break
												else:
													flag=True
											if flag:
												list_of_lists.append([i,b,a,'','','pass','',link])
												print i,'ok'
											else:
												list_of_lists.append([i,b,a,'','','fail',error,link])
												print i,'not',error
							else:
								list_of_lists.append([i,b,a,'','','fail','Expected result not match',link])
								print i,'not because excpection'
						elif b == 'Failed' or b == 'Error':
							if a == b:
								partscheck = checkpoint[0]
								if partscheck == 'manual check':
									list_of_lists.append([i,b,a,msg,partscheck,'fail','manual check',link])
									print i,'ok'
								else:
									if code1 == code2:
										if msg == partscheck:
											list_of_lists.append([i,b,a,'','','pass','',link])
											print i,'ok'
										else:
											list_of_lists.append([i,b,a,msg,partscheck,'fail','msg not match',link])
											print i,'not'
									else:
										list_of_lists.append([i,b,a,'','','fail','error code not match',link])
										print i,'not'
							else:
								list_of_lists.append([i,b,a,'','','fail','Expected result not match',link])
								print i,'not because excpection'
						else:
							list_of_lists.append([i,b,a,'','','TBC','TBC',link])
							print i, 'TBC'
	df = pd.DataFrame(list_of_lists, columns=['case_id','Expected result','Actual result','Msg','check','result','error point','link'])
	df.to_csv('./tools/report_check/result.csv',index = False)
