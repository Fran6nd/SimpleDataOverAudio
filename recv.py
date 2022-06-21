# Print out realtime audio volume as ascii bars

import sounddevice as sd
import numpy as np
import time

from morse import Morse

class MorseRecv:
    running = False
    def millis():
        return round(time.time() * 1000)

    last_status = 0
    status_last_change = millis()
    current_status = 0
    output = ''
    volume_norm = 0

    def print_sound(indata, outdata, frames, time, status):
        if MorseRecv.running:
            MorseRecv.volume_norm = np.linalg.norm(indata)*10
            delay = MorseRecv.millis() - MorseRecv.status_last_change
            if MorseRecv.volume_norm > 5:
                MorseRecv.current_status = 1
            else:
                MorseRecv.current_status = 0
            if MorseRecv.current_status != MorseRecv.last_status:
                MorseRecv.status_last_change = MorseRecv.millis()
                if MorseRecv.last_status == 0:
                    if delay > 1000 * Morse.separator_duration * 1.5:
                        MorseRecv.output += '//'
                    elif delay > 1000 * Morse.separator_duration:
                        MorseRecv.output += '/'
                    
                    
                elif MorseRecv.last_status == 1:
                    if delay > Morse.dot_duration * 1000 * 1.5:
                        MorseRecv.output += Morse.dash
                    else:
                        MorseRecv.output += Morse.dot

            MorseRecv.last_status = MorseRecv.current_status
        

            if delay > 4000 and MorseRecv.current_status == 0:
                MorseRecv.running = False
            
        #print ("|" * int(volume_norm))

    def recv():
        with sd.Stream(callback=MorseRecv.print_sound):
            MorseRecv.running = True
            #sd.sleep(20000)
            #wait for [return] key.
            #input()
            while(MorseRecv.running):
                time.sleep(1)
                print("|" * int(MorseRecv.volume_norm))
        return MorseRecv.output

if __name__ == '__main__':
    msg = MorseRecv.recv()
    print(msg)
    print(Morse.to_text(msg))
