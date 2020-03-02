#!/usr/bin/env python3

f=open("test.txt", "r")
if f.mode == 'r':
    fal =f.readlines()
    for x in fal:
        fsl = x.split()
        for y in fsl:
            if (y == "Rigol" or y == "rigol"):
                instrumentId = fsl[fsl.index(y) - 1]
                instrumentId = instrumentId.split(':')
                print('0x' + instrumentId[0] + ', ' + '0x' + instrumentId[1])
                # print("0x" +  )
