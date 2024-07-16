import unittest
import main
from main import allowedVehiclesList, menu
# allowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]

class testMain(unittest.TestCase):
  def test_menu(self):
    result = main.mainMenu(menu)
    expected = "\n  ********************************\n  AutoCountry Vehicle Finder v0.1\n  ********************************\n  Please Enter the following number below from the following menu:\n\n  1. PRINT all Authorized Vehicles\n  2. Exit"
    self.assertEqual(result, expected)

  def test_input1(self):
    result = main.main(allowedVehiclesList, menu)
    expected = "The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:\nFord F-150\nChevrolet Silverado\nTesla CyberTruck\nToyota Tundra\nNissan Titan\n\n********************************\nAutoCountry Vehicle Finder v0.1\n********************************\nPlease Enter the following number below from the following menu:\n\n1. PRINT all Authorized Vehicles\n2. Exit"
    # print(result)
    # print(expected)
    self.assertEqual(result, expected)

  def test_input2(self):
    result = main.main(allowedVehiclesList, menu)
    self.assertEqual(result, "\nThank you for using the AutoCountry Vehicle Finder, good-bye!")
  
    
if __name__ == "__main__":
  unittest.main()