# Demonstrate key persistence for ET-312
#
# Demonstrates reuse of keys for ET-312 sessions.

import sys
import buttshock.et312
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", dest="serial_port",
                        help="Serial Port to use")

    args = parser.parse_args()

    if not args.serial_port:
        print("Serial port argument is required!")
        sys.exit(1)

    with buttshock.et312.ET312SerialSync(args.serial_port) as et312:
        print("Key is {0:#x} ({0})".format(et312.key, et312.key))

        # Get the current mode
        print("Current box key: {0:#x}".format(et312.read(0x4213)))
        print("Current host key: {0:#x}".format(et312.read(0x4212)))

if __name__ == "__main__":
    main()
