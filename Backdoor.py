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
save_file2=open("SetUID Check.txt", "w")
#에러발생...해결중..
Check_su=subprocess.check_output('find / -user root -perm -4000 2> /dev/null', shell=True)
save_file2.write(str(Check_su))











