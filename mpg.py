import sqlite3
#get mpg of previous records
def main():
    conn = sqlite3.connect('data/prius.sqlite')
    cur = conn.cursor()
    print('Prius:')
    cur.execute('SELECT * FROM Prius')
    for row in cur:
        print(row)
"""
    count = 0
    tot_mpg = 0
    row['date'], row['odometer'], row['gal_used']
    gal_used = float(row['gal_used'])
    new_od = int(row['odometer'])
    miles_trav = new_od - 169916
    mpg = miles_trav / gal_used
    count = count + 1
    tot_mpg = tot_mpg + mpg
        aver = tot_mpg / count
        print(f"\naverage MPG is: {aver} ")"""

main()