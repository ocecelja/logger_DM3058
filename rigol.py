#!/usr/bin/env python3

import usbtmc
import threading
import time

class Rigol():
    def threadRead(self):
        while True:
            # time.sleep(1)
            if (self.continuousMeasure):
                try:
                    readData = self.measure("current", self.characteristic, self.flow, self.samplingRate, self.range)
                    if (readData.strip()):
                        print(readData)
                except:
                    pass

    def __init__(self):
        self.instr = usbtmc.Instrument(0x1ab1, 0x09c4)
        self.thread = threading.Thread(target=self.threadRead)
        self.continuousMeasure = False
        self.thread.start()

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

    def measure(self, measurementType = "current", characteristic = "current", flow = "dc", samplingRate = "s", range = "2"):
        if(str(measurementType) == "current"):
            if(flow):
                return self.ask(":measure:" + characteristic + ":" + flow + "?")
            else:
                return self.ask(":measure:" + characteristic + "?")    
        else:
            self.write(":rate:" + characteristic + ":" + flow + " " + samplingRate)
            self.write(":measure:" + characteristic + ":" + flow + " " + str(range))

            self.setMeasureFlag()
            self.characteristic = characteristic
            self.samplingRate = samplingRate
            self.flow = flow
            self.range = range
            self.setMeasureFlag()

    def calculateStatistic(self, measurementType = "single", value = "min"):
        if(str(measurementType) == "single"):
            self.write(":calculate:function " + value)
            return self.ask(":calculate:statistic:" + value + "?")

if __name__ == "__main__":
    rigol = Rigol()