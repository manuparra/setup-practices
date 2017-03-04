import sys


pupilsfile=sys.argv[1]
account_prefix=sys.argv[2]
default_passwd=sys.argv[3]
startingguid=sys.argv[4]
startinip=sys.argv[5]


pupilslistdata=[]
with open(pupilsfile) as f:
    pupilslist = f.read().splitlines() 

for pup in pupilslist:
    pupilslistdata.append({'username':pup.split("\t")[0],'name':pup.split("\t")[1]})

print "# GRANTED USER SSH"
print "# ----------------"
print ", ".join([account_prefix + pupil['username'] for pupil in pupilslistdata ])


for pupil in pupilslistdata:

	account_name=account_prefix + pupil['username']
	print  "# SYS USER"
	print  "# ------------"
	print  "adduser -c '"+pupil['name']+"' -u " + str(startingguid) + " " + account_name+ ";"
	print  "echo \""+ default_passwd +"\" | passwd "+ account_name +" --stdin" + ";"	

	startingguid=int(startingguid) + 1


for pupil in pupilslistdata:

	account_name=account_prefix + pupil['username']
	
	print "# OPENNEBULA USER SCRIPT"
	print "su - "+account_name
	print "echo '' | ssh-keygen -t rsa -f /home/" + account_name + "/.ssh/id_rsa "
	print "exit"
	print "oneuser create "+ account_name +" --ssh --key /home/"+ account_name +"/.ssh/id_rsa"
	print "oneuser login "+ account_name +" --ssh --force"

	"""
	f=open ("/home/"+account_name + "/vnet.opennebula","w")
	f.write("NAME = \""+account_name+"_vnet\"")
	f.write("BRIDGE = br0")
	f.write("DNS=150.214.191.10")
	f.write("GATEWAY=192.168.10.1")
	f.write("AR = [")
    f.write("TYPE = IP4,")
    f.write("IP = 192.168.10."+ip+",")
    f.write("SIZE = 2")
	f.write("]")
	f.close()	
	"""
	print startinip

	startinip= int(startinip) + 2




