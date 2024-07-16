import unittest
import main
from io import StringIO
import sys
from main import main, allowedVehiclesList, menu
from unittest.mock import patch

class testMain(unittest.TestCase):
  def setUp(self):
    self.vehicles = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]
  # @patch('builtins.input', side_effect=['1','2'])
  def test_input1(self):
    output = StringIO()
    sys.stdout = output
    main(allowedVehiclesList, menu)
    # printCars(allowedVehiclesList)
    sys.stdout = sys.__stdout__
    expected = "The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:\n  Ford F-150\n  Chevrolet Silverado\n  Tesla CyberTruck\n  Toyota Tundra\n  Nissan Titan\n\n  ********************************\n  AutoCountry Vehicle Finder v0.1\n  ********************************\n  Please Enter the following number below from the following menu:\n\n  1. PRINT all Authorized Vehicles\n  2. Exit"
    self.assertEqual(output.getvalue(), expected)
    # self.assertEqual(result, expected)


if __name__ == "__main__":
  unittest.main()