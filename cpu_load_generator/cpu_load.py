#!/usr/bin/env python3

"""
CPU LOAD GENERATOR - Produces load on a CPU 
"""

import argparse
import time
import psutil


def generate_cpu_load(scrape_interval, start_time, segment, cpu_usage):
    while (time.time() - start_time) / segment < cpu_usage:
        if ((time.time() - start_time) / segment) > 1:
            print("too large")
        102224554 ** 2
    time.sleep(1 - cpu_usage)


def main():

    parser = argparse.ArgumentParser(__doc__)

    parser.add_argument("cpu_usage", help="CPU USAGE (0-1)")
    parser.add_argument("duration", help="Duration of CPU LOAD (seconds)")
    parser.add_argument("mem_usage", help="Memory usage in GB")
    args = parser.parse_args()

    if float(args.cpu_usage) < 0 or float(args.cpu_usage) > 1:
        raise RuntimeError("CPU usage must be a number between 0 and 1")

    if float(args.duration) < 0:
        raise RuntimeError("Duration needs to be a positive number in seconds")

    if int(args.mem_usage) < 0:
        raise RuntimeError("Memory usage needs to be a positive number in GB")

    start_time = time.time()
    total_time = start_time + float(args.duration)
    scrape_interval = 1
    segment = 0

    while time.time() < total_time:
        segment += 1
        generate_cpu_load(scrape_interval, start_time, segment, float(args.cpu_usage))
        print(psutil.cpu_percent(interval=None, percpu=True))

    mem_monitor = dict(psutil.virtual_memory()._asdict())
    tot_mem = mem_monitor.get("total") / 1e9
    avail_mem = mem_monitor.get("available") / 1e9
    free_mem = mem_monitor.get("used") / 1e9
    before = tot_mem - free_mem
    print(f"Available memory: {avail_mem} \nUsed memory: {free_mem}")
    a = ["A" * 1024 for _ in range(0, int(args.mem_usage) * 96 ** 3)]
    mem_monitor = dict(psutil.virtual_memory()._asdict())
    tot_mem = mem_monitor.get("total") / 1e9
    avail_mem = mem_monitor.get("available") / 1e9
    free_mem = mem_monitor.get("used") / 1e9
    after = tot_mem - free_mem
    array_size = before - after
    print(f"Available memory: {avail_mem} \nUsed memory: {free_mem}")
    print(f"Array size is: {array_size}")
    print("DONE")


if __name__ == "__main__":
    main()
