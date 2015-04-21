#  playing_with_classes_inheritance.py
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

def main():
  object1 = line(5)
  print("The length of object1 (line) is: " + str(object1.getLength()))

  object2 = rect(5, 10)
  print("The length of object2 (rect) is " + str(object2.getLength()))
  print("The height of object2 (rect) is " + str(object2.getHeight()))
  print("The area of object2 is " + str(object2.getArea()) + " sq units")

  object3 = cube(3,4,7)
  print(object3)

class line:
  def __init__(self, lenX):
    self.__lenX = lenX

  def getLength(self):
    return self.__lenX

class rect(line):
  def __init__(self, lenX, lenY):
    # Init the superclass of line
    line.__init__(self, lenX)

    # Init the lenY (height) attribute
    self.__lenY = lenY

  def getHeight(self):
    return self.__lenY

  def getArea(self):
    area = self.getLength()*self.getHeight()
    return area

class cube(rect):
  def __init__(self, lenX, lenY, lenZ):
    # Init class rect with lenX & lenY
    rect.__init__(self, lenX, lenY)
    # Init class cube with lenZ (depth)
    self.__lenZ = lenZ

  def getDepth(self):
    return self.__lenZ

  def __str__(self):
    return("lenX: " + str(self.getLength()) + "\n" \
           "lenY: " + str(self.getHeight()) + "\n" \
           "lenZ: " + str(self.getDepth()) + "\n")

main()
