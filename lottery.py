"""
Program: lottery.py

Author: Peter Rand 11/19/2021

Mega-Millions Lotto Generator Python Final using breezypythongui.py 
"""

from breezypythongui import EasyFrame
from tkinter.font import Font
import random

class Lottery(EasyFrame):
  
  def __init__(self):
    #Sets up the Mega-Millions Window
    EasyFrame.__init__(self, title = "Mega-Millions Lotto Generator", width = 500, height = 200, resizable = False, background = "blue")
    self.addLabel(text = "Mega-Millions Lotto Generator", row = 0, column = 0, columnspan = 5, sticky = "NSEW", background = "red", font = Font(family = "Impact", size = 24))
    self.addLabel(text = "Your Lotto Numbers:", row = 1, column = 0, columnspan = 5, sticky = "NSEW", background = "blue", font = Font(family = "Arial", size = 13))
    self.topFields = self.addPanel(row = 2, column = 0, background = "blue")
    self.field1 = self.addIntegerField(value = 0, row = 2, column = 0, width = 3)
    self.field2 = self.addIntegerField(value = 0, row = 2, column = 1, width = 3)
    self.field3 = self.addIntegerField(value = 0, row = 2, column = 2, width = 3)
    self.field4 = self.addIntegerField(value = 0, row = 2, column = 3, width = 3)
    self.field5 = self.addIntegerField(value = 0, row = 2, column = 4, width = 3)
    self.addLabel(text = "Your Mega Ball number:", row = 3, column = 2,  columnspan = 3, sticky = "NSEW", background = "blue", font = Font(family = "Arial", size = 9))
    self.mBall = self.addIntegerField(value = 0, row = 3, column = 1, columnspan = 5, width = 3)
    self.addButton(text = "Pick numbers", row = 4,  column = 0, columnspan = 5, command = self.pickNumbers)

  def pickNumbers(self):
    num1 = random.randint(1, 70)    
    num2 = random.randint(1, 70)
    num3 = random.randint(1, 70)
    num4 = random.randint(1, 70)
    num5 = random.randint(1, 70)
    mega = random.randint(1, 25)
    
    self.field1.setNumber(num1)
    self.field2.setNumber(num2)
    self.field3.setNumber(num3)
    self.field4.setNumber(num4)
    self.field5.setNumber(num5)
    self.mBall.setNumber(mega)

# definition of the main() function 
def main():
  
  Lottery().mainloop()

#global call to the main() function
main()