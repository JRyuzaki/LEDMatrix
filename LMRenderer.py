from neopixel import * 
import LMState 


class LMRenderer:
	def __init__(self, led_count, led_pin):
		self.led_count = led_count
		self.led_pin = led_pin
		self.led_brightness = 255
		self.ledStrip = Adafruit_NeoPixel(self.led_count, self.led_pin, 800000, 10, False, self.led_brightness)
		self.ledStrip.begin()
		self.ledStrip.setBrightness(255)

	def renderLEDMatrix(lmstate):
		for i in range(0, len(lmstate.getLEDCount())):
			self.ledStrip.setPixelColor(i, lmstate.getPixelColor(i))

		self.ledStrip.show()