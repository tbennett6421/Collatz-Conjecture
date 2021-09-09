#!/usr/bin/env python3

__code_desc__ = "Given start/stop integers, the program brute forces collatz conjecture"
__code_version__ = 'v0.0.1'
__code_debug__ = False

## Standard Libraries
import sys
import argparse
import atexit
import signal

# Store last successful number
STATE = 1

def do_odd(i):
    return i*3+1

def do_even(i):
    return i // 2

def do_mod(i):
    if (i % 2) == 0:
        return do_even(i)
    else:
        return do_odd(i)

def apply_logic(i):
    loop = [1, 2, 4]
    if i in loop:
        return True
    else:
        while i not in loop:
            i = do_mod(i)
            if i in loop:
                return True

def response(i):
    print("%d loops" % i)

def process(i):
    return apply_logic(i)

def cleanup():
    global STATE
    print("AtExit, ended on %s" % (STATE) )
    sys.exit(0)

def signal_handler(sig, frame):
    cleanup()

def main():
    global STATE
    parser = argparse.ArgumentParser(description=__code_desc__)
    parser.add_argument('-V', '--version', action='version', version=__code_version__)
    parser.add_argument('-v', '--verbose', action='count', default=0)
    parser.add_argument('-i', '--initial', default='1')
    parser.add_argument('-s', '--stop')
    args = parser.parse_args()

    # Register handlers
    atexit.register(cleanup)
    for i in [x for x in dir(signal) if x.startswith("SIG")]:
        try:
            signum = getattr(signal, i)
            signal.signal(signum, signal_handler)
        except (OSError, RuntimeError, ValueError) as m:
            print("Skipping {}".format(i))
    try:
        if args.stop and args.initial:
            i = int(args.initial)
            j = int(args.stop)
            for k in range(i, j):
                b = process(k)
                if b:
                    STATE = k
                    response(k)
                k = k + 1
        elif args.initial:
            i = int(args.initial)
            while True:
                b = process(i)
                if b:
                    STATE = i
                    response(i)
                i = i + 1
    except KeyboardInterrupt:
        print("Caught Exception, ended on %s" % (STATE) )
    except Exception:
        print("Caught Exception, ended on %s" % (STATE) )

if __name__=="__main__":
    main()
