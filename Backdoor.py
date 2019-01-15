import subprocess

#Process Check
save_file1=open("Process Check.txt","w")
Check_ps=subprocess.check_output('ps -ef', shell=True)
save_file1.write(str_ps)


#SetUID Check
save_file2=open("SetUID Check.txt", "w")
#에러발생
Check_su=subprocess.check_output('find / -user root -perm -4000 2> /dev/null', shell=True)
save_file2.write(str(Check_su))
