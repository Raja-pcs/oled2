import Adafruit_DHT
import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont
import time

# Configuration for DHT sensor
DHT_SENSOR = Adafruit_DHT.DHT22  # Specify the DHT sensor type (DHT11, DHT22, or DHT21)
DHT_PIN = "P9_12"  # Replace with the GPIO pin connected to the DHT sensor

# OLED display dimensions
SCREEN_WIDTH = 128
SCREEN_HEIGHT = 64

# Initialize the OLED display (I2C address 0x3C)
display = Adafruit_SSD1306.SSD1306_128_64(rst=None)

# Initialize the display
display.begin()
display.clear()
display.display()

# Create a blank image to draw on
image = Image.new("1", (SCREEN_WIDTH, SCREEN_HEIGHT))
draw = ImageDraw.Draw(image)

# Load fonts
font_small = ImageFont.load_default()  # Small font
font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 18)  # Large font

# Function to display text on the OLED
def display_text(temperature, humidity):
    draw.rectangle((0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), outline=0, fill=0)  # Clear the display

    # Display temperature
    draw.text((0, 0), "Temperature:", font=font_small, fill=255)
    draw.text((0, 15), f"{temperature:.1f}°C", font=font_large, fill=255)

    # Display humidity
    draw.text((0, 40), "Humidity:", font=font_small, fill=255)
    draw.text((0, 55), f"{humidity:.1f}%", font=font_large, fill=255)

    # Update the display
    display.image(image)
    display.display()

# Main loop
try:
    while True:
        # Read temperature and humidity from the DHT sensor
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

        if humidity is not None and temperature is not None:
            print(f"Temp: {temperature:.1f}°C  Humidity: {humidity:.1f}%")
            display_text(temperature, humidity)
        else:
            print("Failed to read from DHT sensor!")
            draw.rectangle((0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), outline=0, fill=0)  # Clear the display
            draw.text((0, 25), "Sensor Error", font=font_small, fill=255)
            display.image(image)
            display.display()

        time.sleep(5)  # Wait 5 seconds before next reading

except KeyboardInterrupt:
    print("Program stopped.")
    display.clear()
    display.display()
