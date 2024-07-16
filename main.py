allowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]
menu = f"""
********************************
AutoCountry Vehicle Finder v0.1
********************************
Please Enter the following number below from the following menu:\n
1. PRINT all Authorized Vehicles
2. Exit"""


def mainMenu(menu):
  print(menu)
  return menu


def printCars(allowedVehiclesList):
  returnString = "\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:"
  print(returnString)
  returnString += "\n"
  
  for vehicle in allowedVehiclesList:
    print(vehicle)
    returnString += vehicle + "\n"
  
  return returnString


def selectChoice():
  choice = input("\nEnter Selection: ")
  return choice


def main(allowedVehiclesList, menu):
  while True:
    mainMenu(menu)
    choice = selectChoice()

    if choice == "1":
      printCars(allowedVehiclesList)
    elif choice == "2":
      exitString = "\nThank you for using the AutoCountry Vehicle Finder, good-bye!"
      print(exitString)
      return exitString   
    else:
      print("\nPlease enter 1 or 2.\n")


if __name__ == "__main__":
  main(allowedVehiclesList, menu)
  