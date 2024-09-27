import time
from rpi_ws281x import PixelStrip, Color
import threading


#回転  iteratonsに回転数
class Cycle(threading.Thread):
    def __init__(self,name,strip, color, wait_ms=80):
        super().__init__(name=name)
        self.strip=strip
        self.color=color
        self.wait_ms=wait_ms
        self.should_stop = False

    def run(self):
        self.strip.setPixelColor(12, 0)
        while not self.should_stop:
            for q in range(12):
                for i in range(0, self.strip.numPixels(), 12):
                    self.strip.setPixelColor(i + q, self.color)
                self.strip.show()
                time.sleep(self.wait_ms / 1000)
                for i in range(0, self.strip.numPixels(), 12):
                    self.strip.setPixelColor(i + q, 0)

    def stop(self):
        self.should_stop = True

class Turn_on(threading.Thread):
    def __init__(self,name,strip, color, wait_ms=80):
        super().__init__(name=name)
        self.strip=strip
        self.color=color
        self.wait_ms=wait_ms
        self.should_stop = False

    def run(self):
        self.strip.setPixelColor(12, 0)
        while not self.should_stop:
            for q in range(12):
                for i in range(0,self.strip.numPixels(), 12):
                    self.strip.setPixelColor(i + q, self.color)
                self.strip.show()
                time.sleep(self.wait_ms / 1000.0)
            time.sleep(1)

    def stop(self):
        self.should_stop = True
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
