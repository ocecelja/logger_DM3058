#!/usr/bin/env python3

import usbtmc

class Rigol():
    def __init__(self):
        self.instr = usbtmc.Instrument(0x1ab1, 0x09c4)

    def ask(self, string):
        return self.instr.ask(string)

    def write(self, string):
        return self.instr.write(string)

    def read(self):
        return self.instr.read()

    def getId(self):
        return self.ask("*IDN?")

    def getMeasurement(self, measurementType = "current", characteristic = "current", flow = "dc", samplingRate = "s", range = "2")
        if(str(measurementType) == "current"):
            if(flow):
                return self.ask(":measure:" + characteristic + ":" + flow + "?")
            else:
                return self.ask(":measure:" + characteristic + "?")    
        else:
            self.write(":rate:" + characteristic + ":" + flow + " " + samplingRate)
            self.write(":measure:" + characteristic + ":" + flow + " " + str(range))

            try:
                while True:
                    if(flow):
                        print(self.getMeasurement("current", characteristic, flow, samplingRate, range))
                    else:
                        print(self.ask("current", characteristic, flow, samplingRate, range))
            except KeyboardInterrupt:
                pass

    # def getCurrentCurrentDc(self):
    #     return self.ask(":measure:current:dc?")

    # def getCurrentVoltagetDc(self):
    #     return self.ask(":measure:voltage:dc?")

    # def getContinuousVoltagetDc(self, samplingRate = "s", range = "2"):
    #     self.write(":rate:voltage:dc " + samplingRate)
    #     self.write(":measure:voltage:dc " + str(range))
    #     try:
    #         while True:
    #             print(self.getCurrentVoltagetDc())
    #     except KeyboardInterrupt:
    #         pass

    # def getContinuousCurrenttDc(self, samplingRate = "s", range = "2"):
    #     self.write(":rate:current:dc " + samplingRate)
    #     self.write(":measure:current:dc " + str(range))
    #     try:
    #         while True:
    #             print(self.getCurrentCurrentDc())
    #     except KeyboardInterrupt:
    #         pass

    # def getCurrentCurrentAc(self):
    #     return self.ask(":measure:current:ac?")

    # def getCurrentVoltagetAc(self):
    #     return self.ask(":measure:voltage:ac?")

    # def getContinuousVoltagetDc(self, samplingRate = "s", range = "2"):
    #     self.write(":rate:voltage:ac " + samplingRate)
    #     self.write(":measure:voltage:ac " + str(range))
    #     try:
    #         while True:
    #             print(self.getCurrentVoltagetAc())
    #     except KeyboardInterrupt:
    #         pass

    # def getContinuousCurrenttAc(self, samplingRate = "s", range = "2"):
    #     self.write(":rate:current:ac " + samplingRate)
    #     self.write(":measure:current:ac " + str(range))
    #     try:
    #         while True:
    #             print(self.getCurrentCurrentAc())
    #     except KeyboardInterrupt:
    #         pass

if __name__ == "__main__":
    rigol = Rigol()