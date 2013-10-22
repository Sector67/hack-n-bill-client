import requests
import json
import datetime
import RFIDDataAccess
import SectorAdminSite
import sys
import time 
import datetime 
import RPi.GPIO as io 
import select

io.setmode(io.BCM) 
power_pin = 2
pir_pin = 24
io.setup(pir_pin, io.IN) 
io.setup(power_pin, io.OUT)
io.output(power_pin, False)

access = RFIDDataAccess.DataAccess()
access.DeleteAllAuthorizedUsers()

authService = SectorAdminSite.SectorAdmin()
data = authService.GetAuthorizedUsers(1)

for user in data:
    access.InsertAuthorizedUser(user['field_rfid_tag_value'],user['uid'],user['name'])

turnoff = datetime.datetime.now()    

while True:


    while sys.stdin in select.select([sys.stdin],[],[],0)[0]:
        rfid = sys.stdin.readline()
        if rfid:
            rfid = ''.join(rfid.splitlines())
            print(rfid)
            if access.IsRFIDAuthorized(rfid):
                print("POWER ON")
                io.output(power_pin, True)
                turnoff = datetime.datetime.now() + datetime.timedelta(0,10)


    if turnoff < datetime.datetime.now():            
        io.output(power_pin, False)         
    time.sleep(.25)
