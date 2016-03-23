# -*- coding: utf-8 -*-
# Author: Jia, En-luan /2014/10/19
# Final Update Time /2014/10/25

import os
import time

Fnames = os.listdir(os.path.abspath('.'))
cmr = time.strftime('%Y-%m-%d-%H%M%S', time.localtime(time.time()))

# Function Description:  Replace Delimiter
def Change_Dlim(Ftpe, Fnames, cmr):
    # add branches, default setting, customize delimiter,
    Dlim_Setting = input("1. '|' to 'FS'[Char28] | 2. Customize | Input Here: ")
    if Dlim_Setting == 1:
        Sdli, Tdli = '|', ''
    elif Dlim_Setting == 2:
        Sdli, Tdli = raw_input("Current delimiter: "), raw_input("Expect delimiter: ")
    for Fname in Fnames:
        try:
            if Ftpe in Fname and 'Transfered' not in Fname:
                print "Start..." + Fname
                lines = open(Fname).readlines()
                Fp = open('DelimiterTransfered_' + Fname[:-4] + '_' + cmr + Fname[-4:], 'w')
                for line in lines:
                    Fp.writelines(line.replace(Sdli, Tdli))
                print 'Success..' + 'DelimiterTransfered_' + Fname[:-4] + '_' + cmr + Fname[-4:]
                Fp.close()
        except:
            print "Something Wrong with the " + Fname + ' Transfer'
            pass

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
            print "Something Wrong with the " + Fname + " Transfer"
            pass

def MenuOrNext(str,FuncName):
    if 'enu' in str: pass
    else: FuncName(str,Fnames, cmr)

def ViewIns():
        print "Instructions:"
        print "Step1: Place files and the '.exe' in the same folder."
        print "Step2: Remove 'Transfered' from Filename (unique for dat/txt file and Function1)"
        print "Step3: Remove 'Retrieve' from Filename (unique for dat file and Function2)"
        print "-"*80

def Main():
    print "-*- I am Case Sensitive -*-"
    str=raw_input("Do you want to view intructions? Input Y/N:")
    if str in ['Y','y']:ViewIns()
    print "-*- Input '1', '2', 'Exit' for choice. -*-"
    while True:
        ChooseFunc = raw_input("1.Change Delimiter | 2.Retrieve Top lines (only dat) | 3.Exit | Input Here: ")
        try:
               if ChooseFunc == '1':
                    Ftpe = '.' + raw_input("Input (dat, txt or HomeMenu): ")
                    MenuOrNext(Ftpe,Change_Dlim)
               elif ChooseFunc == '2':
                    LineNbr = raw_input('Input Expect LineNbr | HomeMenu:  ')
                    MenuOrNext(LineNbr, GetTopLines)
               else:
                   print "ByeBye~"
                   break
        except:
            print "Something Wrong with Function. Please contact Jia, En-luan(Serena)"

usr=Main()
