



# Нужно собрать информацио об операционной системе и версии питона




import sys
import platform


info = 'OS info is \n{}\n\n Python version is {} {}'. format(
    platform.uname (), sys.version, platform.architecture())
print(info)

with open('os_info.txt', 'w') as ff:
    ff.write(info)