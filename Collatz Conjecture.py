#!/usr/bin/env python3
__code_desc__ = "Given start/stop integers, the program brute forces collatz conjecture chains"
__code_version__ = 'v0.0.1'
__code_debug__ = False

## Standard Libraries
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
    chain = [i]
    while i not in loop:
        i = do_mod(i)
        chain.append(i)
    return chain

def response(i, chain, verbose):
    if verbose == 1:
        print(f"{i} → Length: {len(chain)}")
    elif verbose >= 2:
        print(f"{i} → Length: {len(chain)} → Chain: {chain}")
    else:
        print(f"{i} loops")

def process(i, verbose):
    chain = apply_logic(i)
    if chain:
        response(i, chain, verbose)
        return True
    return False

def cleanup():
    global STATE
    print("AtExit, ended on %s" % (STATE) )

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
    for i in dir(signal):
        if i.startswith("SIG") and '_' not in i:
            signum = getattr(signal, i)
            if isinstance(signum, int):
                try:
                    signal.signal(signum, signal_handler)
                except (OSError, RuntimeError, ValueError):
                    pass
    try:
        if args.stop and args.initial:
            idx = int(args.initial)
            jdx = int(args.stop)
            for kdx in range(idx, jdx):
                if process(kdx, args.verbose):
                    STATE = kdx
        elif args.initial:
            idx = int(args.initial)
            while True:
                if process(idx, args.verbose):
                    STATE = idx
                idx = idx + 1
    except KeyboardInterrupt:
        print("Caught Exception, ended on %s" % (STATE) )
    except Exception:
        print("Caught Exception, ended on %s" % (STATE) )

if __name__=="__main__":
    main()
