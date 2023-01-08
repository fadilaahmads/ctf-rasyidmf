import os

flag = ""

#2026 is total count of files
for i in range(2026):
	flag = os.system("cat {}.txt".format(i))
