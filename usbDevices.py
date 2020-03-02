#!/usr/bin/env python3

import subprocess

process = subprocess.run(['lsusb'], 
                         stdout=subprocess.PIPE, 
                         universal_newlines=True)
flsusbReturn = process.stdout
flsusbReturnList = flsusbReturn.split()
for x in flsusbReturnList:
    if (x == "Rigol" or x == "rigol"):
        instrumentId = flsusbReturnList[flsusbReturnList.index(x) - 1]
        instrumentId = instrumentId.split(':')
        print('0x' + instrumentId[0] + ', ' + '0x' + instrumentId[1])
        # print("0x" +  )