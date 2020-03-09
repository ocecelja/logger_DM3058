# logger_DM3058
Python script for data logging on varius versions of Rigol DM3058 made according to [documentation](https://www.batronix.com/files/Rigol/Multimeter/DM3058/DM3058_ProgrammingGuide_EN.pdf).

Possible compliance with whole DM3000 series. However, I didn't test it because I don't have a device except DM3058. Would appreciate feedback regarding this idea.

# Device selection
Script autotdetects connected rigol device. However, one Rigol device should be connected at the time. If experiencing some problems replace lines 33-34:
```
self.instrumentIdList = self.getInstrumentIdList()
self.instr = usbtmc.Instrument(int(self.instrumentIdList[0], 16), int(self.instrumentIdList[1], 16))
```
with
```
self.instr = usbtmc.Instrument("your device Id")
```
"your device Id" you can obtain by running ```lsusb``` on linux OS or using device manager on Windows.

#Running the script
You can start script by running ```sudo python -i rigol.py```. Using it should be straight forward, just take a look at script itself and documentation. All default values are set: single measuremnt of dc voltage at slow sampling rate with range of 20V.

After starting the script, every command can be called via ```rigol.name_of_command(command_arguments)```.
