import string


class Morse:
    dot = '.'
    dash = '-'
    separator = '/'
    dot_duration = 1
    dash_duration = 2
    separator_duration = 2
    equivalent = [
        ['A', '.-'],
        ['B', '-...'],
        ['C', '-.-.'],
        ['D', '-..'],
        ['E', '.'],
        ['F', '..-.'],
        ['G', '--.'],
        ['H', '....'],
        ['I', '..'],
        ['J', '.---'],
        ['K', '-.-'],
        ['L', '.-..'],
        ['M', '--'],
        ['N', '-.'],
        ['O', '---'],
        ['P', '.--.'],
        ['Q', '--.-'],
        ['R', '.-.'],
        ['S', '...'],
        ['T', '-'],
        ['U', '..-'],
        ['V', '...-'],
        ['W', '.--'],
        ['X', '-..-'],
        ['Y', '-.--'],
        ['Z', '--..'],
        ['0', '-----'],
        ['1', '.----'],
        ['2', '..---'],
        ['3', '...--'],
        ['4', '....-'],
        ['5', '.....'],
        ['6', '-....'],
        ['7', '--...'],
        ['8', '---..'],
        ['9', '----.'],
        [' ', '/'],
    ]
    def to_morse(msg : string):
        msg = msg.upper()
        output = ''
        for c in msg:
            for eq in Morse.equivalent:
                if c == eq[0]:
                    if c != ' ':
                        output += eq[1]
                    output += '/'
                    break
        return output
    def to_text(msg : string):
        msg = msg.upper()
        msg = msg.split('/')
        output = ''
        for c in msg:
            for eq in Morse.equivalent:
                if c == eq[1]:
                    output += eq[0]
                    break
                elif c == '':
                    output += ' '
                    break
        return output

if __name__ == '__main__':
    print(Morse.to_text(Morse.to_morse('Hello World 1234')))