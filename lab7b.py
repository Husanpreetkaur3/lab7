#!/usr/bin/env python3
# Student ID: husanpreet-kaur3

from lab7a import Time, format_time, valid_time

def change_time(time, seconds):
    """Modify a time object by adding or subtracting seconds."""
    time.second += seconds
    while time.second >= 60:
        time.second -= 60
        time.minute += 1
    while time.minute >= 60:
        time.minute -= 60
        time.hour += 1
    while time.second < 0:
        time.second += 60
        time.minute -= 1
    while time.minute < 0:
        time.minute += 60
        time.hour -= 1
    return None
