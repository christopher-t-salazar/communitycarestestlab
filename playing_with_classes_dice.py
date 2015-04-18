#  playing_with_classes_dice.py
#  
#  Copyright 2015 Logan W. Bostick <logan.bostick@g.austincc.edu>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import random

def main():
  # Create three dice objects, sending the number of desired sides
  die20 = dice(20)
  die10 = dice(10)
  die6 = dice(6)

  print(die20.value)
  print(die10.value)
  print(die6.value)

  print("Let's roll some dice")
  print("Rolling a twenty sided die for hp ....", die20.roll())
  print("Rolling a ten sided for enemy hp ...", die10.roll())
  print("Rolling a standard die for characters ...", die6.roll())

class dice:
  def __init__(self, maxValue):
    # Find an initial value
    self.minValue = 1
    self.maxValue = maxValue
    self.value = random.randint(self.minValue, self.maxValue)

  def roll(self):
    self.value = random.randint(self.minValue, self.maxValue)
    return self.value
  
main()
