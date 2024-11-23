import time
import board
import busio
from adafruit_ssd1306 import SSD1306_I2C
from PIL import Image, ImageDraw, ImageFont

# I2C setup
i2c = busio.I2C(board.SCL, board.SDA)

# OLED display dimensions
WIDTH = 128
HEIGHT = 64

# Initialize the SSD1306 OLED display
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

# Clear the OLED display
oled.fill(0)
oled.show()

# Create a blank image for drawing
image = Image.new("1", (WIDTH, HEIGHT))  # 1-bit color
draw = ImageDraw.Draw(image)

# Load default font
font = ImageFont.load_default()

# Function to display text
def display_message(message):
    draw.rectangle((0, 0, WIDTH, HEIGHT), outline=0, fill=0)  # Clear screen
    draw.text((10, 25), message, font=font, fill=255)         # Display message
    oled.image(image)
    oled.show()

# Main loop: display messages
try:
    print("Displaying LED ON...")
    display_message("LED ON")
    time.sleep(2)  # Show "LED ON" for 2 seconds

    print("Displaying LED OFF...")
    display_message("LED OFF")
    time.sleep(2)  # Show "LED OFF" for 2 seconds

    print("Displaying Hello World...")
    display_message("Hello World")
    time.sleep(2)  # Show "Hello World" for 2 seconds

except KeyboardInterrupt:
    print("Program interrupted!")

finally:
    # Clear display on exit
    oled.fill(0)
    oled.show()
