from flask import Flask,request,jsonify
import futarin_led as led
import argparse 
import time
import threading
from rpi_ws281x import PixelStrip, Color

LED_COUNT = 12        # Number of LED pixels.
LED_PIN = 12          # GPIO pin -connected to the pixels (18 uses PWM!).
# LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1-' for GPIOs 13, 19, 41, 45 or 53

app=Flask(__name__)

#@app.route("/")
#@app.route("/wifi/high",methods=["post"])
#def wifi_high():
 #   return jsonify({"status":"wifi high"}),202            
if __name__ == '__main__':
    # Process arguments
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

   # print('Press Ctrl-C to quit.')
    #if not args.clear:
     #   print('Use "-c" argument to clear LEDs on exit')
    
    try:
        @app.route("/")
        @app.route("/wifi/high",methods=["post"])
        def wifi_high():
           led.turn_on(strip,Color(0,0,100))
           return jsonify({"status":""}),202
        
        @app.route("/wifi/middle",methods=["post"])
        def wifi_middle():
           led.turn_on(strip,Color(100,100,0))
           return jsonify({"aa"}),202
        
        @app.route("/wifi/low",methods=["post"])
        def wifi_low():
           led.turn_on(strip,Color(200,100,0))
           return jsonify({"status":"wifi high"}),202
        
        @app.route("/wifi/disconnect",methods=["post"])
        def wifi_disconnect():
           led.turn_on(strip,Color(200,0,0))
           return jsonify({"status":"wifi high"}),202
        
        @app.route("/audio/listening",methods=["post"])
        def audio_listening():
           led.flash(strip,Color(200,100,0))
           return jsonify({"status":"wifi high"}),202
        
        @app.route("/audio/thinking",methods=["post"])
        def audio_thinking():
           led.cycle(strip,Color(0,0,100))
           return jsonify({"status":"wifi high"}),202
        
        @app.route("/audio/res-success",methods=["post"])
        def audio_success():
           led.turn_on(strip,Color(0,0,100))
           return jsonify({"status":"wifi high"}),202
        
        @app.route("/audio/res-fail",methods=["post"])
        def audio_fail():
           led.turn_on(strip,Color(100,0,0))
           return jsonify({"status":"wifi high"}),202
        
        if __name__ == "__main__":
            app.run(debug=True)
            
    except KeyboardInterrupt:
        if args.clear:
            led.cycle(strip, Color(0, 0, 0), 10)            
