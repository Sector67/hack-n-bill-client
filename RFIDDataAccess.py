#!/usr/bin/python

import sqlite3

class DataAccess:

    connectionString = "RFID.db"




    def DeleteAllAuthorizedUsers( waste):

        conn = sqlite3.connect(DataAccess.connectionString)
        conn.execute("Delete From AuthorizedUsers")
        conn.commit()
        conn.close()

        return


    def InsertAuthorizedUser( waste, rfid, uid, username):

        conn = sqlite3.connect(DataAccess.connectionString)
        command = "Insert Into AuthorizedUsers (RFID, uid, name) values ('{0}',{1},'{2}');".format(rfid,uid,username)
        conn.execute(command)
        conn.commit()
        conn.close()

        return
    
    def IsRFIDAuthorized(waste, rfid):
        allowed = False
        conn = sqlite3.connect(DataAccess.connectionString)
        command = "Select * From AuthorizedUsers Where RFID = '{0}'".format(rfid)
        
        for row in conn.execute(command):    
            allowed = True

        conn.close()

        return allowed        
