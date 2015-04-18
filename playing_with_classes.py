#  playing_with_classes.py
#  
#  Copyright 2015 Logan W. Bostick  
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

import random

def main():
  # Create three pocketChange objects
  coin1 = pocketChange()
  coin2 = pocketChange()
  coin3 = pocketChange()

  # Display the name, and value of the coins with calls to functions within pocketChange
  # Direct calls to the attributes (coin1.name/coin1.value) would work, but doing that is bad practice
  print("Coin1's name is: ", coin1.name, "and it's value is $", format(coin1.value, ".2f") + ".")
  print("Coin2's name is: ", coin2.getName(), "and it's value is $", format(coin2.getValue(), ".2f") + ".")
  print("Coin3's name is: ", coin3.getName(), "and it's value is $", format(coin3.getValue(), ".2f") + ".")

  # Add the value of the coins
  total = coin1.getValue() + coin2.getValue() + coin3.getValue()

  # Display the value of the coins
  print("Your total is: $", format(total, ".2f"))

class pocketChange:
  # Creates a coin
  def __init__(self):
    # Find a random number
    a = random.randint(1, 100)
    # Depending on value of random number(a), set coin attributes
    if a >= 1 and a <= 3:
      self.name = "penny"
      self.value = 0.01
    elif a >= 4 and a < 10:
      self.name = "nickle"
      self.value = 0.05
    elif a >= 10 and a < 25:
      self.name = "dime"
      self.value = 0.10
    elif a >= 25 and a < 50:
      self.name = "quarter"
      self.value = 0.25
    elif a >= 50 and a < 100:
      self.name = "half dollar"
      self.value = 0.50
    elif a == 100:
      self.name = "golden dollar"
      self.value = 1.00

  # Simple function to return the value of the coin
  def getValue(self):
    return self.value
  # Simple function to return the name of the coin
  def getName(self):
    return self.name

main()
