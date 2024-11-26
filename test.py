import os, shutil

workdir = '/Volumes/WPP/00_data/oldPre/data_raw'
files = sorted(os.listdir(workdir))  ##以按顺序读取
for sub in files:
	pathImg = workdir+'/'+sub+'/resting'
	# pathImg = workdir+'/011/011_wm1'

	n = 0
	try:
		for dcm in os.listdir(pathImg):
			n = n+1
		print(sub+','+str(n))
	except (FileNotFoundError, OSError) as e:
		print(sub+' error')
		continue





	# if file[0:5]=='IPCAS':
	# 	# print(file[-4:])
	# 	pathImg = workdir+'/'+file+'/scans/Task4/resources/DICOM/files'

	# 	n = 0
	# 	try:
	# 		for dcm in os.listdir(pathImg):
	# 			n = n+1
	# 		print(file[-3:]+','+str(n))
	# 	except (FileNotFoundError, OSError) as e:
	# 		print("Skipping {file} due to error: {e}")
	# 		continue



