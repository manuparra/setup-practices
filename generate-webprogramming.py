
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
	print  "mkdir /home/" + default_passwd + "/public_html/" + ";"
	print  "chmod 755 -R /home/"+ default_passwd+ "/public_html/" + ";"

	startingguid=int(startingguid) + 1



for pupil in pupilslist:
	
	account_name=account_prefix + pupil

	print  "# SQL USER"
	print  "# --------"
	print  "CREATE USER '"+account_name+"'@'localhost' IDENTIFIED BY '"+default_passwd+"';"
	print  "CREATE DATABASE '"+ account_name +"';"
	print  "GRANT ALL PRIVILEGES ON account_name.* TO '"+ account_name+ "'@'localhost';"

print "FLUSH PRIVILEGES;"

