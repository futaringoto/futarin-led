import time
from rpi_ws281x import PixelStrip, Color



#回転  iteratonsに回転数
def cycle(strip, color, wait_ms=80, iterations=10):
    strip.setPixelColor(12, 0)
    for j in range(iterations):
        for q in range(12):
            for i in range(0, strip.numPixels(), 12):
                strip.setPixelColor(i + q, color)
            strip.show()
            time.sleep(wait_ms / 1000)
            for i in range(0, strip.numPixels(), 12):
              strip.setPixelColor(i + q, 0)
#点灯
def turn_on(strip, color, wait_ms=10, iterations=1):
    strip.setPixelColor(12, 0)
    for j in range(iterations):
        for q in range(12):
            for i in range(0, strip.numPixels(), 12):
                strip.setPixelColor(i + q, color)
            strip.show()
            time.sleep(wait_ms / 1000.0)
        time.sleep(5)
#点滅
def flash(strip, color, wait_ms=10, iterations=100):
    strip.setPixelColor(12, 0)
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
