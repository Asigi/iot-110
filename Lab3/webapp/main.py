import time
from gpio import PiGpio
from debouncer import Debouncer
from flask import *

app = Flask(__name__)
pi_gpio = PiGpio()
db = Debouncer()


# =========================== Endpoint: /myData ===============================
# read the gpio states by GET method from curl for example
# curl http://iot8e3c:5000/myData
# -----------------------------------------------------------------------------
@app.route('/myData')
def myData():
    def get_state_values():
        while True:
            # return the yield results on each loop, but never exits while loop
            raw_switch = pi_gpio.read_switch()
            debounced_switch = str(db.debounce(raw_switch))
            led_red = str(pi_gpio.get_led(1))
            led_grn = str(pi_gpio.get_led(2))
            led_blu = str(pi_gpio.get_led(3))
            yield('data: {0} {1} {2} {3}\n\n'.format(debounced_switch,led_red,led_grn,led_blu))
            time.sleep(0.1)
    return Response(get_state_values(), mimetype='text/event-stream')



@app.route("/")
def index():
    # create an instance of my pi gpio object class.
    pi_gpio = PiGpio()
    switch_state = pi_gpio.read_switch()
    led1_state = pi_gpio.get_led(1)
    led2_state = pi_gpio.get_led(2)
    led3_state = pi_gpio.get_led(3)
    return render_template('index.html', switch=switch_state,
                                led1=led1_state,
                                led2=led2_state,
                                led3=led3_state)


@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, threaded=True)
