
import sys
from time import sleep

# msg = "What is your name"

# for ch in msg:
#     sys.stdout.write(ch)
#     sleep(0.5)


def output_with_animate(msg, interval=0.1):

    for ch in msg:
        sys.stdout.write(ch)
        sleep(interval)

    sys.stdout.write('\n')


output_with_animate("wow that is cool")

output_with_animate("wow that is really cool", 1)
