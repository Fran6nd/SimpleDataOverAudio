from time import sleep
import numpy as np
import simpleaudio as sa
from morse import Morse
import sys

def sound(x,z):
    frequency = x # Our played note will be 440 Hz
    fs = 44100  # 44100 samples per second
    seconds = z  # Note duration of 3 seconds

    # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
    t = np.linspace(0, seconds, seconds * fs, False)

    # Generate a 440 Hz sine wave
    note = np.sin(frequency * t * 2 * np.pi)

    # Ensure that highest value is in 16-bit range
    audio = note * (2**15 - 1) / np.max(np.abs(note))
    # Convert to 16-bit data
    audio = audio.astype(np.int16)

    # Start playback
    play_obj = sa.play_buffer(audio, 1, 2, fs)

    # Wait for playback to finish before exiting
    play_obj.wait_done()

def emit(msg):
    for c in msg:
        if c == Morse.separator:
            sleep(Morse.separator_duration/2)
        else:
            if c == Morse.dash:
                sound(300, Morse.dash_duration)
                sleep(1)
            elif c == Morse.dot:
                sound(300,Morse.dot_duration)
                sleep(1)

if __name__ == '__main__':
    if(len(sys.argv) == 2):
        print('Sending: ' + sys.argv[1])
        print('which means: ' + Morse.to_morse(sys.argv[1]))
        emit(Morse.to_morse(sys.argv[1]))