#Python calculator für mice population
#a school project
#by commandmars
#version: i forgot to count :)


#imports for crazy stuff
import sys
import csv

#some more crazy stuff noone will really need
def exit(reason):
  print(reason)
  sys.exit("\n\n" + reason)


print("Mäuserechner\nBerechne, wie viele Mäuse nach einer bestimmten Anzahl an Zyklen leben würden.")


#setup your own mice population
try:
  youth = int(input("\nAnzahl der jungen Tiere: \n"))
  boomers = int(input("\nAnzahl der erwachsenen Tiere: \n"))
  old = int(input("\nAnzahl der alten Tiere: \n"))
  cycles = int(input("\nAnzahl der Zyklen: \n"))
except ValueError:
  exit("Nope.")


print("\nSollen die einzelnen Werte verändert werden?")
alterEverything = input("y/n\n")
if alterEverything == "y":
  boomersToYouth = int(input("junge Tiere von erwachsenen Tieren: \n"))
  oldToYouth = int(input("junge Tiere von alten Tieren: \n"))
  youthToBoomers = int(input("junge Tiere zu erwachsenen Tieren: \n"))
  boomersToOld = int(input("erwachsene Tiere zu alten Tieren: \n"))
  decimalPlaces = int(input("Nachkommastellen: \n"))
elif alterEverything == "n":
  print("Normaleinstellungen werden übernommen. \n(4/2/2/3/0)")
  boomersToYouth = 4
  oldToYouth = 2
  youthToBoomers = 2
  boomersToOld = 3
  decimalPlaces = 0
else:
  exit("Stop it. Get some help.")


print("\nSoll die Anzahl der Tiere nach jedem Zyklus angezeigt werden?")
showAnimalsAfterEveryCycle = input("y/n\n")
try:
  
  if showAnimalsAfterEveryCycle == "y" or "n":
  
    try:
      
      startSimulation = input("\nMit Enter die Simulation starten.")
      
      if startSimulation == "":
        #open or create the csv file and run the mice simulation
        with open("table.csv", "w") as csvfile:
          writer = csv.writer(csvfile, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL)
          
          print("\nSimulation wird gestartet.")
          
          for i in range(cycles):
            youthTemporarily = youth
            boomersTemporarily = boomers
            youth = round( ( ( boomers * boomersToYouth ) + ( old * oldToYouth ) ) , decimalPlaces )
            boomers = round( ( youthTemporarily / youthToBoomers ) , decimalPlaces )
            old = round( ( boomersTemporarily / boomersToOld ) , decimalPlaces )
            try:
              writer.writerow([i + 1, youth, boomers, old])
              if (i+1) % 10 == 0:
                print("Zyklus " + str(i+1) + " erfolgreich")
            except:
              exit("Zyklus " + str(i+1) + " fehlgeschlagen.")
          
        
            #if the user wants to, it is possible to see the current status after every successful cycle
            if showAnimalsAfterEveryCycle == "y":
              print("\nNach " + str(i + 1) + " Zyklen:")
              print("Jungen Tiere: " + str(youth))
              print("Erwachsene Tiere: " + str(boomers))
              print("Alte Tiere: " + str(old))
              print("Insgesamt " + str(youth + boomers + old) + " Tiere.")
    except ValueError:
      exit("PRESS ENTER I SAID!")
    except:
      exit("I don't know, just don't do the same thing you did before. CHANGE IT!")

    print("\nSimulation beendet.")
    
except:
  exit("WHY? just WHY?")
  
#a review
if showAnimalsAfterEveryCycle == "n":
  print("\nErgebnis:")
  print("Nach " + str(cycles) + " Zyklen:")
  print("Anzahl der jungen Tiere: " + str(youth))
  print("Anzahl der erwachsenen Tiere: " + str(boomers))
  print("Anzahl der alten Tiere: " + str(old))


print("\n\n\n\n\nthe end")
#the end