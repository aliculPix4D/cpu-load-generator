#!/usr/bin/env python3

"""
CPU LOAD GENERATOR - Produces load on all available CPU cores
"""

import argparse
from multiprocessing import Pool
from multiprocessing import cpu_count
import signal
import sys
import time

import yaml


def f(x):
    x * x
    x + 1


def main():

    parser = argparse.ArgumentParser(__doc__)

    parser.add_argument("cpu_usage", help="CPU USAGE (0-1)")
    parser.add_argument("duration", help="Duration of CPU LOAD (seconds)")
    args = parser.parse_args()

    if float(args.cpu_usage) < 0 or float(args.cpu_usage) > 1:
        raise RuntimeError("CPU usage must be a number between 0 and 1")

    if float(args.duration) < 0:
        raise RuntimeError("Duration needs to be a positive number in seconds")

    processes = cpu_count()

    print("-" * 20)
    print("Running load on CPU")
    print(f"Utilizing {processes} cores")
    print("-" * 20)

    pool = Pool(processes)
    interval = time.time() + float(args.duration)

    # generates some CPU load for duration of x args.duration seconds
    while time.time() < interval:
        (pool.map(f, list(range(processes))))

    print("DONE")
    sys.exit(0)


if __name__ == "__main__":
    main()
