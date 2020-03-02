#!/usr/bin/env python3

import usbtmc
import threading
import time
import subprocess

class Rigol():
    def threadRead(self):
        while True:
            # time.sleep(1)
            if (self.continuousMeasure):
                try:
                    readData = self.measure("single", self.characteristic, self.flow)
                    if (readData.strip()):
                        print(readData)
                except:
                    pass

    def getInstrumentIdList(self):
        process = subprocess.run(['lsusb'], 
                         stdout=subprocess.PIPE, 
                         universal_newlines=True)
        flsusbReturn = process.stdout
        flsusbReturnList = flsusbReturn.split()
        for x in flsusbReturnList:
            if (x == "Rigol" or x == "rigol"):
                instrumentId = flsusbReturnList[flsusbReturnList.index(x) - 1]
                instrumentIdList = instrumentId.split(':')
                return instrumentIdList

    def __init__(self):
        self.instrumentIdList = self.getInstrumentIdList()
        self.instr = usbtmc.Instrument(int(self.instrumentIdList[0], 16), int(self.instrumentIdList[1], 16))
        self.thread = threading.Thread(target=self.threadRead)
        self.continuousMeasure = False
        self.thread.start()
        self.measure()
        self.setRange()
        self.setRate()

    def setMeasureFlag(self):
        self.continuousMeasure = True

    def destroyMeasureFlag(self):
        self.continuousMeasure = False

    def ask(self, string):
        return self.instr.ask(string)

    def write(self, string):
        return self.instr.write(string)

    def read(self):
        return self.instr.read()

    def getId(self):
        return self.ask("*IDN?")

    def measure(self, measurementType = "single", characteristic = "voltage", flow = "dc"):
        self.measurementType = measurementType
        self.characteristic = characteristic
        self.flow = flow

        if(str(measurementType) == "single"):
            if(flow):
                return self.ask(":measure:" + self.characteristic + ":" + self.flow + "?")
            else:
                return self.ask(":measure:" + self.characteristic + "?")    
        else:
            self.setMeasureFlag()
    
    def getStatistic(self):
        return self.ask(":calculate:statistic:" + self.description + "?")

    def setStatistic(self, description = "min"):
        self.description = description
        self.write(":calculate:function " + self.description)
    
    def setRate(self, samplingRate = "s"):
        self.samplingRate = samplingRate

        if(self.flow):
            self.write(":rate:" + self.characteristic + ":" + self.flow + " " + self.samplingRate)
        else:
            self.write(":rate:" + self.characteristic + " " + self.samplingRate)

    def setRange(self, measurementRange = "2"):
        self.measurementRange = measurementRange

        if(self.flow):
            self.write(":measure:" + self.characteristic + ":" + self.flow + " " + self.measurementRange)
        else:
            self.write(":measure:" + self.characteristic + " " + slef.measurementRange)

if __name__ == "__main__":
    rigol = Rigol()