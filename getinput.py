#Module for handling OS based IOs
import sys
class getinput:
    if sys.platform == 'win32' or sys.platform == 'nt':
        import msvcrt
        getch = msvcrt.getch
        getche = msvcrt.getche
    else:
        import sys
        import termios
        def __gen_ch_getter(echo):
            def __fun():
                fd = sys.stdin.fileno()
                oldattr = termios.tcgetattr(fd)
                newattr = oldattr[:]
                try:
                    if echo:
                        lflag = ~(termios.ICANON | termios.ECHOCTL)
                    else:
                        lflag = ~(termios.ICANON | termios.ECHO)
                        newattr[3] &= lflag
                        termios.tcsetattr(fd, termios.TCSADRAIN, newattr)
                        ch = sys.stdin.read(1)
                        if echo and ord(ch) == 127:
                            sys.stdout.write('\b \b')
                finally:
                    termios.tcsetattr(fd, termios.TCSADRAIN, oldattr)
                    return ch
                    return __fun
                    getch = __gen_ch_getter(False)
                    getche = __gen_ch_getter(True)
