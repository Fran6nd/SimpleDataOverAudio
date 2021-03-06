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
    squelch = 5

    def read_audio_input(indata, outdata, frames, time, status):
        if MorseRecv.running:
            MorseRecv.volume_norm = np.linalg.norm(indata)*10
            delay = MorseRecv.millis() - MorseRecv.status_last_change
            if MorseRecv.volume_norm > MorseRecv.squelch:
                MorseRecv.current_status = 1
            else:
                MorseRecv.current_status = 0
            if MorseRecv.current_status != MorseRecv.last_status:
                MorseRecv.status_last_change = MorseRecv.millis()
                if MorseRecv.last_status == 0:
                    if delay > 1000 * Morse.separator_duration * 1.5 and MorseRecv.output != '':
                        MorseRecv.output += '//'
                    elif delay > 1000 * Morse.separator_duration:
                        MorseRecv.output += '/'
                    
                    
                elif MorseRecv.last_status == 1:
                    if delay > Morse.dot_duration * 1000 * 1.5:
                        MorseRecv.output += Morse.dash
                    elif delay>Morse.dot_duration*1000:
                        MorseRecv.output += Morse.dot

            MorseRecv.last_status = MorseRecv.current_status
        
            # Useful for self shutdown.
            # if delay > 4000 and MorseRecv.current_status == 0:
            #    MorseRecv.running = False
            
        #print ("|" * int(volume_norm))

    def recv():
        import curses
        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)

        stdscr.nodelay(1)

        MorseRecv.running = True
        with sd.Stream(callback=MorseRecv.read_audio_input):
            while MorseRecv.running:
                stdscr.clear()
                stdscr.addstr( 'Audio Morse Receiver by Fran6\n')
                stdscr.addstr( 'Press \'q\' to exit.\n')
                stdscr.addstr( 'Morse received: ' + MorseRecv.output + '\nText received: ' +   Morse.to_text(MorseRecv.output) + '\n' +  '|' * int(MorseRecv.volume_norm) + '\n' + ' ' * (MorseRecv.squelch-1) + '^')
                c = stdscr.getch()
                if c == ord('q'):
                    break  # Exit the while loop
                elif c == curses.KEY_HOME:
                    x = y = 0

        MorseRecv.running = False
        curses.endwin()
        #        print("|" * int(MorseRecv.volume_norm))
        #return MorseRecv.output

if __name__ == '__main__':
    MorseRecv.recv()
