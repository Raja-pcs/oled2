import time
import board
import busio
from adafruit_ssd1306 import SSD1306_I2C
from adafruit_framebuf import FrameBuffer, MVLSB

# I2C Setup
i2c = busio.I2C(board.SCL, board.SDA)
WIDTH = 128
HEIGHT = 64

# Initialize SSD1306 OLED Display
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

# Turn off display (clears screen and sends OFF command)
def turn_off_display():
    oled.fill(0)  # Clear the display
    oled.show()
    oled.poweroff()  # Turn off the display hardware

# Turn on display
def turn_on_display():
    oled.poweron()  # Turn on the display hardware
    oled.fill(0)  # Clear the display
    oled.text("Display ON!", 10, 10, 1)  # Draw text
    oled.show()

# Draw Graphics Example
def draw_graphics():
    oled.fill(0)  # Clear the display
    oled.text("Shapes!", 10, 10, 1)
    oled.rect(20, 20, 40, 20, 1)  # Draw rectangle
    oled.circle(80, 40, 10, 1)    # Draw circle
    oled.show()

try:
    # Turn on the display
    print("Turning ON the display...")
    turn_on_display()
    time.sleep(2)

    # Draw graphics
    print("Drawing graphics...")
    draw_graphics()
    time.sleep(5)

    # Turn off the display
    print("Turning OFF the display...")
    turn_off_display()

except KeyboardInterrupt:
    print("Interrupted!")
finally:
    oled.fill(0)
    oled.show()
