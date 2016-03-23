# -*- coding: utf-8 -*-
# Author: Jia, En-luan /2014/10/19
# Final Update Time /2014/10/25

import os
import time

Fnames = os.listdir(os.path.abspath('.'))
cmr = time.strftime('%Y-%m-%d-%H%M%S', time.localtime(time.time()))


def GetTopLines(LineNbr, Fnames, cmr):
    for Fname in Fnames:
        try:
            if '.dat' in Fname and 'Retrieve' not in Fname:
                init = 0
                lines = open(Fname, 'r').readlines()
                print "Start..." + Fname
                FnameNew = 'Retrieve' + LineNbr + 'Lines_' + Fname[:-4] + '_' + cmr + Fname[-4:]
                Fp = open(FnameNew, 'w')
                for line in lines:
                    Fp.writelines(line)
                    init += 1
                    if init > int(LineNbr):
                        break
                print "Success.." + FnameNew + ' Generated'
                Fp.close()
        except:
            print "Exceptions. End Process"
def Main():
    print "-*- Retrieve Top Lines|Unique for Dat Files -*-"
    print "-*- Step1. Place the 'exe' and dat files in same folder Step2. Execute the 'exe' -*-"
    LineNbr=raw_input("Input Line nbr: ")
    GetTopLines(LineNbr, Fnames, cmr)

usr= Main()
