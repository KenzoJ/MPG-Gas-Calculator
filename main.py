import sqlite3
import datetime

def main():
    new_readings = get_readings()
    add_data(new_readings[0], new_readings[1])

def get_readings():
    odo = input("current ODO?")
    gallon = input("Gallons?")
    return odo, gallon
  
def add_data(gas, odo):
    #static data for time
    now = datetime.datetime.now()
    now = now.strftime("%Y-%m-%d")

    #initializing table access 
    conn = sqlite3.connect('data/prius.sqlite')
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS prius')
    cur.execute('CREATE TABLE prius (date DATE, odo INTEGER, gallons FLOAT)')
    
    ## inserting data
    cur.execute('INSERT INTO Prius (date, odo, gallons) VALUES (?, ?, ?)',
    (now, odo, gas))
    conn.commit()

    ## removing the data for continue ## 
    """cur.execute('DELETE FROM Prius WHERE odo > 1')
    conn.commit()"""

    cur.close()

main()

