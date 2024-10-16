from flask import Flask, jsonify
import futarin_led as led
from rpi_ws281x import PixelStrip, Color

LED_COUNT = 12  # Number of LED pixels.
LED_PIN = 12  # GPIO pin -connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10  # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0  # set to '1-' for GPIOs 13, 19, 41, 45 or 53

thread = None
app = Flask(__name__)
strip = PixelStrip(
    LED_COUNT,
    LED_PIN,
    LED_FREQ_HZ,
    LED_DMA,
    LED_INVERT,
    LED_BRIGHTNESS,
    LED_CHANNEL,
)

strip.begin()


@app.route("/")
@app.route("/system/on", methods=["post"])
def power_on():
    global thread
    if thread:
        thread.stop()
        thread.join()
    thread = led.Turn_on("power_on", strip, Color(250, 250, 250))
    thread.start()
    return jsonify({"status": "power on"}), 202


@app.route("/system/setup", methods=["post"])
def setup():
    global thread
    if thread:
        thread.stop()
        thread.join()
    thread = led.Cycle("setup", strip, Color(250, 250, 250))
    thread.start()
    return jsonify({"status": "setup"}), 202


@app.route("/system/off", methods=["post"])
def power_off():
    global thread
    if thread:
        thread.stop()
        thread.join()
    thread = led.Turn_on("power_off", strip, Color(250, 250, 250))
    thread.start()
    return jsonify({"status": "power off"}), 202


@app.route("/system/turn_off", methods=["post"])
def turn_off():
    global thread
    if thread:
        thread.stop()
        thread.join()
    thread = led.Turn_on("turn_off", strip, Color(0, 0, 0))
    thread.start()
    return jsonify({"status": "turn_off"}), 202


@app.route("/wifi/high", methods=["post"])
def wifi_high():
    global thread
    if thread:
        thread.stop()
        thread.join()
    thread = led.Turn_on("wifi_high", strip, Color(0, 250, 0))
    thread.start()
    return jsonify({"status": "wifi high"}), 202


@app.route("/wifi/middle", methods=["post"])
def wifi_middle():
    global thread
    if thread:
        thread.stop()
        thread.join()
    thread = led.Turn_on("wifi_middle", strip, Color(150, 100, 0))
    thread.start()
    return jsonify({"status": "wifi middle"}), 202


@app.route("/wifi/low", methods=["post"])
def wifi_low():
    global thread
    if thread:
        thread.stop()
        thread.join()
    thread = led.Turn_on("wifi_low", strip, Color(250, 60, 0))
    thread.start()
    return jsonify({"status": "wifi low"}), 202


@app.route("/wifi/disconnect", methods=["post"])
def wifi_disconnect():
    global thread
    if thread:
        thread.stop()
        thread.join()
    thread = led.Turn_on("wifi_disconnect", strip, Color(250, 0, 0))
    thread.start()

    return jsonify({"status": "wifi disconnect"}), 202


@app.route("/audio/listening", methods=["post"])
def audio_listening():
    global thread
    if thread:
        thread.stop()
        thread.join()
    thread = led.Flash("audio_listening", strip, Color(0, 250, 0))
    thread.start()

    return jsonify({"status": "listening"}), 202


@app.route("/audio/thinking", methods=["post"])
def audio_thinking():
    global thread
    if thread:
        thread.stop()
        thread.join()
    thread = led.Cycle("audio_thinking", strip, Color(0, 250, 0))
    thread.start()

    return jsonify({"status": "thinking"}), 202


@app.route("/audio/res-success", methods=["post"])
def audio_success():
    global thread
    if thread:
        thread.stop()
        thread.join()
    thread = led.Turn_on("audio_response_success", strip, Color(0, 250, 0))
    thread.start()
    return jsonify({"status": "response success"}), 202


@app.route("/audio/res-fail", methods=["post"])
def audio_fail():
    global thread
    if thread:
        thread.stop()
        thread.join()
    thread = led.Turn_on("audio_response_fail", strip, Color(250, 0, 0))
    thread.start()
    return jsonify({"status": "response fail"}), 202


@app.route("/audio/uploading", methods=["post"])
def audio_uploading():
    global thread
    if thread:
        thread.stop()
        thread.join()
    thread = led.Cycle("audio_uploading", strip, Color(250, 70, 70))
    thread.start()
    return jsonify({"status": "uploading"}), 202


@app.route("/audio/receive", methods=["post"])
def audio_receive():
    global thread
    if thread:
        thread.stop()
        thread.join()
    thread = led.Turn_on("audio_receive", strip, Color(250, 70, 70))
    thread.start()
    return jsonify({"status": "receive"}), 202


if __name__ == "__main__":
    thread = led.Turn_on("power_on", strip, Color(250, 250, 250))
    thread.start()

    app.run(port=8080)
