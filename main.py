from funcs import *
import time
import keyword


if __name__ == '__main__':
    print("Status: Successfully connected")
    filename = input('Open -port::start as ')

    start = time.time()

    with open(filename) as f:
        print("Status: Successfully opened")
        print('\n\n')
        s = f.read()
        for i in Keywords:
            s = s.replace(i, Keywords[i])
        exec(s)

    end = time.time()


    print(f"({filename} executed in {round(end-start, 5)} seconds)")
else:
    print("Status: Failed to connect")