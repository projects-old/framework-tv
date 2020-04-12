# -*- coding: utf-8 -*-

import sys

def FahrtoCel(fhr):
        FahrtoCel = ((fhr - 32)*5)/9
        return FahrtoCel
def CeltoFahr(cls):
        CeltoFahr = (cls * 1.8)+32
        return CeltoFahr
def MilestoKil(mk):
        MilestoKil = mk * 1.6093
        print("Length: " + str(mk) + " mi = " + str(MilestoKil) + " km")
def KiltoMiles(km):
        KiltoMiles = km * 0.6214
        print("Length: " + str(km) + " km = "+ str(KiltoMiles) + " mi")
def CupstoGal(gl):
        CupstoGal = (gl) / 16.0
	return CupstoGal
def GaltoCups(C):
        GaltoCups = C * 16
        print("Volume: " + str(C) + " gal (US) = " + str(GaltoCups) + " c") 
num = int(raw_input("\nSelect a conversion: \n\n1. Fahrenheit to Celsius \n2. Celsius to Fahrenheit \n3. Kilometers to Miles \n4. Miles to Kilometers \n5. Cups to Gallons (US) \n6. Gallons(US) to Cups \n7. Exit \n\nEnter Menu Number:  "))
if num == 1:
        num = int(raw_input("Enter a number (in F): "))
        print("Temperature: " + str(num) + "°F  = %4.2f" %  FahrtoCel(num) + "°C")
elif num == 2:
        num = int(raw_input("Enter a number (in C): "))
        print("Temperature: " + str(num)+ "°C = %4.2f" % CeltoFahr(num)+ "°F")
elif num == 3:
        num = int(raw_input("Enter a number (in km): "))
        KiltoMiles(num)
elif num == 4:
        num = int(raw_input("Enter a number (in mi): "))
        MilestoKil(num)
elif num == 5:
        num = int(raw_input("Enter a number (in cups): "))
        print("Volume: " + str(num) + " c = %4.3f" % CupstoGal(num) + " gal (US)")
elif num == 6:
        num = int(raw_input("Enter a number (in US Gallons): "))
        GaltoCups(num)
elif num == 7:
	sys.exit("Exiting program. Bye.")
