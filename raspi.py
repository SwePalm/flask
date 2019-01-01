from sense_hat import SenseHat
from time import sleep


class Raspi(object):

  def __init__(self):
    self.sense = SenseHat()
    self.sense.clear()

  def read_sensor(self):
    return round(self.sense.get_temperature(), 1)

  def change_led(self, red = 255, green = 255, blue = 255):
    self.sense.clear(red, green, blue)
    sleep(3)
    self.sense.clear()
