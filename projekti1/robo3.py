# #!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank, Motor, OUTPUT_A
from ev3dev2.sound import Sound
from threading import Thread

m = LargeMotor(OUTPUT_C)
n = LargeMotor(OUTPUT_B)
p = Motor(OUTPUT_A)
sound = Sound()

def dance3():

        def soundbyte1():
            sound.play_file('CarelessWhisperCut.wav', volume=100, play_type=0)

        def tank_driving1():

            while alt_thread.is_alive() == True:
                p.run_forever()
                m.on_for_rotations(SpeedPercent(10), 3)
                n.on_for_rotations(SpeedPercent(-10), 3)
                p.stop()

        alt_thread = Thread(target=soundbyte1)

        alt_thread.start()
        tank_driving1()
        alt_thread.join()





