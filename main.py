#!/usr/bin/env python3
"""
used to make the python file as executable file
This is the project to build the basic CMD with kali_linux
"""

class Bgcolor:
    bold = '\033[1m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    blue = '\033[94m'
    exit_ = '\033[0m'


import os  # importing the os module
import time  # importing the time module
import sys  # importing the sys module

history = []  # used to store the commands used in prompt


def hhelp():  # this function define all the help command
    print('Easy User (version 0.0.1)')
    print('Usage: ([command] {-format})')
    print('   BASIC COMMANDS:')
    print('      cwd - used to show the current working directory\n')
    print('      cd - just give the name of folder or file correctly\n'
          '           format correctly as in example')
    print('           Format:')
    print('            \'.fo\' use at the end to say that is folder')
    print('            \'.fi\' use at the end to say that is file')
    print('            eg:  cd fi_fo_finder .fo\n')
    print('      lis - used to list everything in current working directory')
    print('           .a - used to list hidden files also\n')
    print('      clr - used to clear the page\n')
    print('      read - used to read a file\n')
    print('            eg: read lara.py ')
    print('      edit - used to edit a file\n')
    print('            eg: edit python.txt ')
    print('      hist - used to list the command stored in history\n')
    print('      cfol - used to create a folder with sub-folder inside')
    print('             eg: mkfol ragav/lara\n')
    print('      cfil - used to create the file')
    print('             eg: cfil ragav.txt\n')
    print('      rm - used to remove a file or folder')
    print('            \'.fo\' use at the end to say that is folder')
    print('            \'.fi\' use at the end to say that is file')
    print('            eg:  cd pycharm.py .fi\n')
    print('      exit - used to close the terminal')


def rev(a):  # this function defined to reverse the given string
    fin = ''
    i = -1
    for _ in a:
        fin += a[i]
        i += -1
    return fin


def cd(a, c):  # used to enter a folder
    b = '/home'
    if c == 'fi':  # if the given is file
        for path_, folders, files in os.walk(b):
            if a in files:
                os.chdir(path_)
    elif c == 'fo':  # if the given is folder
        for path_, folders, files in os.walk(b):
            if a in folders:
                os.chdir(os.path.join(path_, a))
    else:
        sys.stderr.write('Error: Please check your command!!\n')
        time.sleep(1)
        MAIN()  # to rise


def MAIN():  # main function
    while True:
        print()
        u = os.environ.get('USER')
        cm = input(
            Bgcolor.bold + (
                    Bgcolor.blue + '|' + Bgcolor.exit_ + Bgcolor.red + 'user' + u'\U0001F480' + u + Bgcolor.exit_ +
                    Bgcolor.blue + '|~(' + Bgcolor.exit_ + os.getcwd() + Bgcolor.blue + ')' + Bgcolor.exit_ +
                    '\n' + Bgcolor.blue + '|---' + Bgcolor.exit_ + Bgcolor.red + '\u2765' + Bgcolor.exit_) + Bgcolor.exit_)
        # input function
        history.append(cm)
        if cm == 'help':
            hhelp()

        elif cm.startswith('cd'):  # enter a folder or search the file and enter the file location
            if cm.endswith('.fo'):
                cd(a=cm[3:cm.index('.fo')].strip(), c='fo')
            elif cm.endswith('.fi'):
                cd(a=cm[3:cm.index('.fi')].strip(), c='fi')
            else:
                sys.stderr.write('Error: Please check your command!!\n')
                time.sleep(1)
                MAIN()

        elif cm.strip() == 'lis':  # to list what is present in it
            k = 1
            a = os.listdir()
            for i in a:
                if i.startswith('.'):
                    pass
                else:
                    print(i, end='\n')

        elif cm.startswith('lis') and cm.endswith('.a'):  # to list all the hidden files
            ll = os.listdir()
            for i in ll:
                print(i)

        elif cm.strip() == 'cwd':  # to print the current working directory
            print(os.getcwd())

        elif cm.strip() == 'clr':  # to clear the screen
            os.system('clear')
            MAIN()

        elif cm.strip().startswith('bk'):  # to go back
            for _ in range(cm.strip().count('bk')):
                p = os.getcwd()
                p = rev(p)
                c = p.index('/')
                p = rev(p[c:])
                os.chdir(p)

        elif cm.strip() == 'hist':  # to list the history
            for i in history:
                print(i)

        elif cm.startswith('read'):  # to read a file
            fi = open(cm[4:].strip(), 'r')
            print(fi.read())
            fi.close()

        elif cm.strip().startswith('edit'):  # to edit a file
            os.system(cm)

        elif cm.startswith('cfol'):  # to create a folder
            os.makedirs(cm[4:].strip())

        elif cm.startswith('cfil'):  # to create a file
            o = open(cm[4:].strip(), 'x')
            o.close()

        elif cm.startswith('rm'):  # to remove a a file or folder
            if cm.endswith('.fo'):
                os.system('rm -r ' + cm[2:cm.find('.fo')].strip())
            elif cm.endswith('.fi'):
                os.remove(cm[2:cm.find('.fi')].strip())
            else:
                sys.stderr.write('Error: Please check your command!!\n')
                time.sleep(1)
                MAIN()

        elif cm == 'exit':
            exit()

        else:  # if the user enter a undefined command
            sys.stderr.write('Error: Please Command is not Found!!\n')
            time.sleep(1)
            MAIN()


if __name__ == '__main__':  # coding starts
    os.system('clear')
    # ---- heading to be display
    os.chdir('/home')
    b = '/home'
    for path_, folders, files in os.walk(b):
        if 'head.txt' in files:
            b = path_

    fi = open(b + '/head.txt', 'r')
    print(fi.read())
    fi.close()
    # -------

    hhelp()
    MAIN()  # calling the main function
