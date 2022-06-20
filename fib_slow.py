#!/usr/bin/env python3


def main():
    i = 1
    while True:
        print(fib_at(i))
        print('\n')
        i = i+1


def fib_at(position_n):
    if position_n ==1:
        return 1
    if position_n == 2:
        return 1
    return fib_at(position_n-1) + fib_at(position_n-2)


if __name__ == '__main__':
    main()
