from common.runtime import Runtime
import os, sys, getopt

dir_path = os.path.dirname(os.path.realpath(__file__))
runtime = Runtime(dir_path)


def main(argv):
    try:
        opts, args = getopt.getopt(argv,"i",["init",])
    except getopt.GetoptError:
        print('Aufruf: test.py --init')
        sys.exit(2)
    for opt, arg in opts:
        print(opt)
        if opt == '-h':
            print('test.py --init')
            sys.exit()
        elif opt in ("-i", "--init"):
            runtime.init()
            runtime.close()


if __name__ == "__main__":
    main(sys.argv[1:])
