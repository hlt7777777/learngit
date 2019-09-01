import time

def test1():
    start_time = time.time()
    print(start_time)

    for a in range(1, 1000):
        for b in range(1, 1000):
            if a**2 +b**2 == (1000-a-b)**2:
                print(a,b,(1000-a-b))

    end_time = time.time()
    print(end_time)
    print(end_time-start_time)

def test2():
    print(1)


if __name__ == '__main__':
    test1()