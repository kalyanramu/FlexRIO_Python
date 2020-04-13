import subprocess

UIManager = "C:/Program Files/National Instruments/NI VeriStand UI Manager 2018/NationalInstruments.VeriStand.UIManager.Application.exe"
GUIPath = "C:/Users/Public/Documents/National Instruments/NI VeriStand 2018/Examples/Stimulus Profile/Engine Demo/Engine Demo.nivsprj"

cmd= [UIManager, '/nivsprj', GUIPath, '/gateway', 'localhost', '/connect']
subprocess.call(cmd)

