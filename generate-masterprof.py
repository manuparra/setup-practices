import sys


pupilsfile=sys.argv[1]
account_prefix=sys.argv[2]
default_passwd=sys.argv[3]
startingguid=sys.argv[4]
startinip=sys.argv[5]
startinipdocker=sys.argv[6]


pupilslistdata=[]

with open(pupilsfile) as f:
    pupilslist = f.read().splitlines() 

for pup in pupilslist:
	username=pup.split("\t")[0]
	name=pup.split("\t")[1]
	pupilslistdata.append({'username':username,'name':name})


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
	print "cat /home/" + account_name + "/.ssh/id_rsa.pub"
	print "# Copy id_rsa.pub to opennebula user Public SSH Key"
	

startinip=sys.argv[5]
for pupil in pupilslistdata:

	account_name=account_prefix + pupil['username']


	print "# ACCOUNT: " + account_name + " forwarding"
	print "-A PREROUTING -i eno1 -p tcp --dport 15"+ str(startinip).zfill(3) + " -j DNAT --to 192.168.10."+str(startinip)+":80"
	print "-A PREROUTING -p tcp --dport 15"+str(startinip).zfill(3)+" -j DNAT --to 192.168.10."+str(startinip)+":80"
	print "-A PREROUTING -i eno1 -p tcp --dport 15"+ str(startinip).zfill(3) + " -j DNAT --to 192.168.10."+str(startinip)+":443"
	print "-A PREROUTING -p tcp --dport 15"+str(startinip).zfill(3)+" -j DNAT --to 192.168.10."+str(startinip)+":443"
	nextip= int(startinip) +1
	print "-A PREROUTING -i eno1 -p tcp --dport 15"+ str(nextip).zfill(3) + " -j DNAT --to 192.168.10."+str(nextip)+":80"
	print "-A PREROUTING -p tcp --dport 15"+str(nextip).zfill(3)+" -j DNAT --to 192.168.10."+str(nextip)+":80"
	print "-A PREROUTING -i eno1 -p tcp --dport 15"+ str(nextip).zfill(3) + " -j DNAT --to 192.168.10."+str(nextip)+":443"
	print "-A PREROUTING -p tcp --dport 15"+str(nextip).zfill(3)+" -j DNAT --to 192.168.10."+str(nextip)+":443"
	startinip= int(startinip) + 2


startinip=sys.argv[5]
for pupil in pupilslistdata:

	account_name=account_prefix + pupil['username']

	print "# ACCOUNT: " + account_name + " forwarding"
	print "-A POSTROUTING -p tcp -d 192.168.10."+str(startinip)+" --dport 80 -j MASQUERADE"
	print "-A POSTROUTING -p tcp -d 192.168.10."+str(startinip)+" --dport 443	 -j MASQUERADE"
	nextip= int(startinip) +1
	print "-A POSTROUTING -p tcp -d 192.168.10."+str(nextip)+" --dport 80 -j MASQUERADE"
	print "-A POSTROUTING -p tcp -d 192.168.10."+str(nextip)+" --dport 443	 -j MASQUERADE"


	startinip= int(startinip) + 2


startinipdocker=sys.argv[6]
for pupil in pupilslistdata:

	account_name=account_prefix + pupil['username']

	print "# DOCKER PORTS redirected. User " + account_name + " "
	for ni in range(0,5):
		nextip=int(startinipdocker) + ni
		print "Docker: "+str(nextip)		

	startinipdocker=int(startinipdocker)+5
	


for pupil in pupilslistdata:

	account_name=account_prefix + pupil['username']

	print "# HDFS working dir creation:  " + account_name + " "
	print "hdfs dfs -mkdir -p /user/" + account_name
	print "hdfs dfs -chown "+account_name+":supergroup /user/" + account_name
	#print "hdfs dfs -rmdir /user/masterprofcc/" + account_name
	
	


startinip=sys.argv[5]
print len(pupilslistdata)
for pupil in pupilslistdata:

	account_name=account_prefix + pupil['username']
	
	#f=open ("/tmp/"+account_name + "vnet.opennebula","w")
	#f.write("NAME = \""+account_name+"_vnet\"\n")
	#f.write("BRIDGE = br0\n")
	#f.write("DNS=150.214.191.10\n")
	#f.write("GATEWAY=192.168.10.1\n")
	#f.write("AR = [\n")
	#f.write("TYPE = IP4,\n")
	#f.write("IP = 192.168.10."+str(startinip)+",\n")
	#f.write("SIZE = 2\n")
	#f.write("]\n")
	#f.close()	
	
	print startinip

	startinip= int(startinip) + 2




