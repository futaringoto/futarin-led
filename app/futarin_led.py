import time
from rpi_ws281x import PixelStrip, Color
import argparse
from flask import Flask,render_template,request


# LED strip configuration:
LED_COUNT = 12        # Number of LED pixels.
LED_PIN = 12          # GPIO pin -connected to the pixels (18 uses PWM!).
# LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1-' for GPIOs 13, 19, 41, 45 or 53

app=Flask(__name__)

#回転  iteratonsに回転数
def cycle(strip, color, wait_ms=80, iterations=4):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(12):
            for i in range(0, strip.numPixels(), 12):
                strip.setPixelColor(i + q, color)
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, strip.numPixels(), 12):
              strip.setPixelColor(i + q, 0)
#点灯
def turn_on(strip, color, wait_ms=10, iterations=1):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(12):
            for i in range(0, strip.numPixels(), 12):
                strip.setPixelColor(i + q, color)
            strip.show()
            time.sleep(wait_ms / 1000.0)
        time.sleep(5)
#点滅
def flash(strip, color, wait_ms=10, iterations=5):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(12):
            for i in range(0, strip.numPixels(), 12):
                strip.setPixelColor(i + q, color)
            strip.show()
            time.sleep(wait_ms / 1000.0)
        time.sleep(1)
        for q in range(12):
            for i in range(0, strip.numPixels(), 12):
                strip.setPixelColor(i + q,0)
            strip.show()
            time.sleep(wait_ms / 1000.0)
        time.sleep(1)

    # Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    print('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:
        @app.route("/")
        @app.route("wifi/high",methods=["post"])
        def wifi_high():
            return "wifi high"
            
        if __name__ == "__main__":
            app.run(debug=True)
            
    except KeyboardInterrupt:
        if args.clear:
            cycle(strip, Color(0, 0, 0), 10)
