import sys


pupilsfile=sys.argv[1]
account_prefix=sys.argv[2]
default_passwd=sys.argv[3]
startingguid=sys.argv[4]


with open(pupilsfile) as f:
    pupilslist = f.read().splitlines() 

print "# GRANTED USER SSH"
print "# ----------------"
print ", ".join([account_prefix + pupil for pupil in pupilslist ])


for pupil in pupilslist:

	account_name=account_prefix + pupil
	print  "# SYS USER"
	print  "# ------------"
	print  "adduser -u " + str(startingguid) + " " + account_name+ ";"
	print  "echo "+ default_passwd +" | passwd "+ account_name +" --stdin" + ";"
	print  "chmod 711 /home/" + default_passwd + ";"	

	startingguid=int(startingguid) + 1



