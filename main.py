from sys import exit

print("Mäuserechner\nBerechne, wie viele Mäuse nach einer bestimmten Anzahl an Zyklen leben würden.")

youth = int(input("\nAnzahl der jungen Tiere: \n"))
boomers = int(input("\nAnzahl der erwachsenen Tiere: \n"))
old = int(input("\nAnzahl der alten Tiere: \n"))
cycles = int(input("\nAnzahl der Zyklen: \n"))

print("\nSoll die Anzahl der Tiere nach jedem Zyklus angezeigt werden?")
showAnimalsAfterEveryCycle = input("y/n\n")

print("\nSoll die einzelnen Werte verändert werden?")
alterEverything = input("y/n\n")
if alterEverything == "y":
  boomersToYouth = int(input("junge Tiere von erwachsenen Tieren: \n"))
  oldToYouth = int(input("junge Tiere von alten Tieren: \n"))
  youthToBoomers = int(input("junge Tiere zu erwachsenen Tieren: \n"))
  boomersToOld = int(input("erwachsene Tiere zu alten Tieren: \n"))
  decimalPlaces = int(input("Nachkommastellen: \n"))

elif alterEverything == "n":
  print("Normaleinstellungen werden übernommen.")
  boomersToYouth = 4
  oldToYouth = 2
  youthToBoomers = 2
  boomersToOld = 3
  decimalPlaces = 0

else:
  sys.exit(

for i in range(cycles):
  youthTemporarily = youth
  boomersTemporarily = boomers
  
  youth = round( ( ( boomers * boomersToYouth ) + ( old * oldToYouth ) ) , decimalPlaces ) 
  boomers = round( ( youthTemporarily / youthToBoomers ) , decimalPlaces )
  old = round( ( boomersTemporarily / boomersToOld ) , decimalPlaces )

  if showAnimalsAfterEveryCycle == "y":
    print("\nNach " + str(i+1) + " Zyklen:")
    print("Jungen Tiere: " + str(youth))
    print("Erwachsene Tiere: " + str(boomers))
    print("Alte Tiere: " + str(old))
    print(str(youth + boomers + old) + " Tiere.")

if showAnimalsAfterEveryCycle == "n":
  print("\nNach " + str(cycles) + " Zyklen:")
  print("Anzahl der jungen Tiere: " + str(youth))
  print("Anzahl der erwachsenen Tiere: " + str(boomers))
  print("Anzahl der alten Tiere: " + str(old))

