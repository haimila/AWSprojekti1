# #!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank, Motor, OUTPUT_A, SpeedRPM
from ev3dev2.sound import Sound
from threading import Thread
import time

# Lego EV3-muuttujat
m = LargeMotor(OUTPUT_C)
n = LargeMotor(OUTPUT_B)
p = Motor(OUTPUT_A)
sound = Sound()

# Pääfunktio, jota kutsutaan mainloopissa
def dance1():
        # äänitiedosto, joka määritellään myöhemmin toiseksi threadiksi
        def soundbyte1():
            sound.play_file('PartyHardCut.wav', volume=100, play_type=0)

        # robotin ajaminen, toimii luupilla niin pitkään kun toinen threadi pyörii
        def tank_driving1():

            while alt_thread.is_alive() == True:
                # prototyyppi ajosta funktiona, kopioitu legon omasta ohjeesta
                def square_drive():
                    p.run_forever()
                    edge_length_drive_time_s = 2.0
                    drive_straight(m, n, edge_length_drive_time_s)
                    turn_90(m, n)
                    time.sleep(0.1)
                    p.stop()

                def drive_straight(left_motor, right_motor, time_s):
                    left_motor.run_forever(speed_sp=1000)
                    right_motor.run_forever(speed_sp=1000)
                    time.sleep(time_s)
                    left_motor.stop(stop_action="brake")
                    right_motor.stop(stop_action="brake")

                def turn_90(n_motor, m_motor):
                    motor_turns_deg = 486
                    m.run_to_rel_pos(position_sp=motor_turns_deg, speed_sp=1000)
                    n.run_to_rel_pos(position_sp=-motor_turns_deg, speed_sp=1000)
                    m.wait_while(Motor.STATE_RUNNING)
                    n.wait_while(Motor.STATE_RUNNING)

                square_drive()

        # soundbyte-funktiosta tehdään oma threadinsa:
        alt_thread = Thread(target=soundbyte1)
        # suoritetaan järjestyksessä uusin thread, robotin ajo, ja threadin lopetus
        alt_thread.start()
        tank_driving1()
        alt_thread.join()






