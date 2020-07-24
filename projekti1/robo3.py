# #!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank, Motor, OUTPUT_A
from ev3dev2.sound import Sound
from threading import Thread

# Lego EV3-muuttujat
m = LargeMotor(OUTPUT_C)
n = LargeMotor(OUTPUT_B)
p = Motor(OUTPUT_A)
sound = Sound()

# Pääfunktio, jota kutsutaan mainloopissa
def dance3():
        # äänitiedosto, joka määritellään myöhemmin toiseksi threadiksi
        def soundbyte1():
            sound.play_file('CarelessWhisperCut.wav', volume=100, play_type=0)

        # robotin ajaminen, toimii luupilla niin pitkään kun toinen threadi pyörii
        def tank_driving1():

            while alt_thread.is_alive() == True:
                p.run_forever()
                m.on_for_rotations(SpeedPercent(10), 3)
                n.on_for_rotations(SpeedPercent(-10), 3)
                p.stop()

        # soundbyte-funktiosta tehdään oma threadinsa:
        alt_thread = Thread(target=soundbyte1)
        # suoritetaan järjestyksessä uusin thread, robotin ajo, ja threadin lopetus
        alt_thread.start()
        tank_driving1()
        alt_thread.join()





