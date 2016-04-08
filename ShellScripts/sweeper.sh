#!bin/bash/
# $1:  
#Auto-sweeper 
if [$1='PRO1']; then
	ssh iwmaster@{servername}
	bash ~/{buketName}/{shellName}.sh tape v1 PRO1 $2
	cd {folder path}
	ls -altr
elif [$1='PRO2']; then
	ssh iwmaster@{servername}
	bash ~/{buketName}/{shellName}.sh tape v1 PRO2 $2
	cd {folder path}
	ls -altr
elif [$1='PRO3']; then
	ssh iwmaster@{servername}
	bash ~/{buketName}/{shellName}.sh tape v1 PRO3 $2
	cd {folder path}
	ls -altr
elif [$1='PRO4']; then
	ssh iwmaster@{servername}
	bash ~/{buketName}/{shellName}.sh tape v1  PRO4 $2
	bash ~/{buketName}/{shellName}.sh  cc v1  PRO4 $2
	cd {folder path}
	ls -altr
fi
echo 'services: '+$1
echo 'MetaFile ID: '+$2
echo 'Sweeper Done'