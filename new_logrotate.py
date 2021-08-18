import sys
import os
import subprocess

line1 = input("Enter the logfile you want to rotate: \n")
line2 = input("How frequent you want to rotate..Weekly/monthly\n")
line3 = "missingok\n"
line4 = input("How many logfile you want on disk..\n")
line5 = "compress\n"
line6 = "delaycompress\n"
line7 = "notifempty\n"
line8 = "copytruncate\n"


def check_file():
    assert os.path.exists(line1), "I did not find the file at, "+str(line1)


def backup():
    subprocess.run(["sudo","cp","/etc/logrotate.conf","/bck/"])
    print("Backup of logrotate file is done!!")    


def write_file():
    f = open("/etc/logrotate.conf", 'a')
    print("Writing configuration file..!!")
    f.write(line1)
    f.write('{\n')
    f.write(line2)
    f.write('\n')
    f.write("missingok\n")
    f.write(line4)
    f.write("\n")
    f.write("compress\n")
    f.write("delaycompress\n")
    f.write("notifempty\n")
    f.write("copytruncate\n")
    f.write("}")
    f.close()
    print("Done!!")



check_file()
backup()
write_file()
