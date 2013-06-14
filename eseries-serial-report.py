#!/usr/local/python-2.7.2/bin/python
##
#
# A simple tool to collect data from netapp e-series hosts.
# wy3oo&w4  <-- password by default on all eseries arrays.
#
# Blake Golliher - blakegolliher@gmail.com
#
##

import sys
import telnetlib
import getpass
import re

PROMPT = '->'

password = getpass.getpass()

## put in your list of array's here

eseries = (
            "eseries001",
            "eseries002",
            "eseries003",
            "eseries004",
            "eseries005",
            "eseries006")

for name in eseries:
        tn = telnetlib.Telnet(name)
        user= ('shellUsr')
        tn.read_until("login: ")
        tn.write(user + "\n")
        if password:
                tn.read_until("Password:")
                tn.write(password + "\n")

        tn.read_until(PROMPT)
        tn.write("cmgrShow\n")
        cmgrShow_output = tn.read_until(PROMPT)
        tn.write("exit\n")
        print "Array name: %s " % name
        for line in cmgrShow_output.split('\n'):
                if "Serial" in line:
                        line = re.sub(r':' , ' ', line)
                        line = re.sub(r'\s+',' ', line)
                        line = re.sub(r'\t+',' ', line)
  		print "Serial	: %s" % line.split(" ")[1]
