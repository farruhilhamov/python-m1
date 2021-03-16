#!/usr/bin/env/ python3

from functools import reduce


def main():
    people = [{"name":"Anna","height":160},{"name":"Lena","height":175},{"name":"Kate"}]
    h = list(map(lambda x:x["height"],list(filter(lambda x:"height" in x,people))))
    sred = reduce(lambda x,y:x+y,h)/len(h)
    print(sred)

if __name__ == "__main__":
    main()

