import csv
import datetime

def main():
    current_time = datetime.datetime.now()
    timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
    count = 0
    tot_mpg = 0
    odo = input("current ODO?")
    gallon = input("Gallons?")
    with open("2024-Prius.csv", "a", newline='') as csvfile: 
        writer = csv.writer(csvfile)
        writer.writerow([timestamp, odo, gallon])
    with open("2024-Prius.csv", newline='') as csvfile2:
        reader = csv.DictReader(csvfile2)
        for row in reader:
            print(row['date'], row['odometer'], row['gal_used'])
            gal_used = float(row['gal_used'])
            new_od = int(row['odometer'])
            miles_trav = new_od - 169916
            mpg = miles_trav / gal_used
            count = count + 1
            tot_mpg = tot_mpg + mpg 
        aver = tot_mpg / count
        print(f"\naverage MPG is: {aver} ")
        
    
    #169,916
        #169,966
    #9.239 gallons
        #170,292
        #9.6
main()