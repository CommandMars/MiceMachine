import sys
import csv
import os

def exit(reason):
  print(reason)
  sys.exit()


print(
    "Mäuserechner\nBerechne, wie viele Mäuse nach einer bestimmten Anzahl an Zyklen leben würden."
)

try:
  youth = int(input("\nAnzahl der jungen Tiere: \n"))
  boomers = int(input("\nAnzahl der erwachsenen Tiere: \n"))
  old = int(input("\nAnzahl der alten Tiere: \n"))
  cycles = int(input("\nAnzahl der Zyklen: \n"))
except:
  exit("\nNope.")

print("\nSoll die Anzahl der Tiere nach jedem Zyklus angezeigt werden?")
showAnimalsAfterEveryCycle = input("y/n\n")

if showAnimalsAfterEveryCycle != ("y" or "n"):
  exit("WHY? just WHY?")

print("\nSollen die einzelnen Werte verändert werden?")
alterEverything = input("y/n\n")
if alterEverything == "y":
  boomersToYouth = int(input("junge Tiere von erwachsenen Tieren: \n"))
  oldToYouth = int(input("junge Tiere von alten Tieren: \n"))
  youthToBoomers = int(input("junge Tiere zu erwachsenen Tieren: \n"))
  boomersToOld = int(input("erwachsene Tiere zu alten Tieren: \n"))
  decimalPlaces = int(input("Nachkommastellen: \n"))

elif alterEverything == "n":
  print("\nNormaleinstellungen werden übernommen.")
  boomersToYouth = 4
  oldToYouth = 2
  youthToBoomers = 2
  boomersToOld = 3
  decimalPlaces = 0

else:
  exit("\n\nStop it. Get some help.")

with open("table.csv", "w") as csvfile:
  writer = csv.writer(csvfile, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL)

  print("\n\nSimulation wird gestartet.")
  
  for i in range(cycles):
    youthTemporarily = youth
    boomersTemporarily = boomers

    youth = round(((boomers * boomersToYouth) + (old * oldToYouth)),decimalPlaces)
    boomers = round((youthTemporarily / youthToBoomers), decimalPlaces)
    old = round((boomersTemporarily / boomersToOld), decimalPlaces)

    writer.writerow([i + 1, youth, boomers, old])

    if showAnimalsAfterEveryCycle == "y":
      print("\nNach " + str(i + 1) + " Zyklen:")
      print("Jungen Tiere: " + str(youth))
      print("Erwachsene Tiere: " + str(boomers))
      print("Alte Tiere: " + str(old))
      print("Insgesamt " + str(youth + boomers + old) + " Tiere.")

if showAnimalsAfterEveryCycle == "n":
  print("\nNach " + str(cycles) + " Zyklen:")
  print("Anzahl der jungen Tiere: " + str(youth))
  print("Anzahl der erwachsenen Tiere: " + str(boomers))
  print("Anzahl der alten Tiere: " + str(old))

print("\nSimulation beendet.")
