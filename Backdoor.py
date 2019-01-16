import subprocess

#Process Check
Save_file=open("Process Check.txt","w")
Check_ps=subprocess.check_output('ps -ef', shell=True, universal_newlines=True)
Save_file.write(Check_ps)
Split_data=Check_ps.split("\n")

for i in Split_data:
    if 'pts' in i:
        print(i)


#SetUID Check
Save_file2=open("SetUID Check.txt", "w")
command="find / -user root -perm -4000 2> /dev/null"
Check_su=subprocess.Popen(command, shell=True, stdout=save_file2, stderr=None)







