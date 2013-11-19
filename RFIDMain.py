import datetime
import sys
import time
import RPi.GPIO as io
import select

from HNBC.HNBC.models import RFIDKey, RFIDLog

io.setmode(io.BCM)
power_pin = 2
pir_pin = 24
io.setup(pir_pin, io.IN)
io.setup(power_pin, io.OUT)
io.output(power_pin, False)


turnoff = datetime.datetime.now()

while True:


    while sys.stdin in select.select([sys.stdin],[],[],0)[0]:
        rfid = sys.stdin.readline()
        if rfid:
            rfid = ''.join(rfid.splitlines())
            print(rfid)

            try:
                # Verify that there is a key, and that the user is active
                key = RFIDKey.objects.get(code='asdf', user__isnull=False)
                user = key.user
            except RFIDKey.DoesNotExist:
                continue # Key isn't in database
            except RFIDKey.MultipleObjectsReturned:
                continue # Possibly bad juju or mucked up database

            if key and user.is_active:
                RFIDLog(key=key).save()
                print("POWER ON")
                io.output(power_pin, True)
                turnoff = datetime.datetime.now() + datetime.timedelta(0,10)

    if turnoff < datetime.datetime.now():
        io.output(power_pin, False)

    time.sleep(.25)
