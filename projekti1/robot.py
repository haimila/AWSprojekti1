# #!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sound import Sound
from threading import Thread
from datetime import datetime

m = LargeMotor(OUTPUT_C)
sound = Sound()

tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)

def dance1():
    while True:
        def soundbyte1():
            sound.play_file('PartyHardCut.wav', volume=100, play_type=0)

        def tank_driving1():

            for i in range(0,15):
                # drive in a turn for 5 rotations of the outer motor
                # the first two parameters can be unit classes or percentages.
                tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(75), 10)

                # drive in a different turn for 3 seconds
                tank_drive.on_for_seconds(SpeedPercent(60), SpeedPercent(30), 3)

        daemonthread = Thread(target=tank_driving1)
        daemonthread.setDaemon(True)

        daemonthread.start()
        soundbyte1()
        break

dance1()