import board
import busio
from adafruit_ssd1306 import SSD1306_I2C

# I2C setup
i2c = busio.I2C(board.SCL, board.SDA)

# OLED display dimensions
WIDTH = 128
HEIGHT = 64

# Initialize SSD1306 OLED display
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

# Test: Clear and display text
oled.fill(0)
oled.text("Hello, OLED!", 0, 0, 1)
oled.show()
