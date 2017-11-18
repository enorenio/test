import time, sys, signal

x = 1
signal.signal(signal.SIGINT, signal.default_int_handler)
while True:
    try:
        print x
        time.sleep(.3)
        x += 1
    except KeyboardInterrupt:
        print "Bye"
        sys.exit()
