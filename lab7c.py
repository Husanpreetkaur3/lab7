#!/usr/bin/env python3
# Student ID: husanpreet-kaur3

class Time:
    """Simple object type for time of the day."""
    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for Time object."""
        self.hour = hour
        self.minute = minute
        self.second = second

    def valid_time(self):
        """Check if time is valid."""
        return 0 <= self.hour < 24 and 0 <= self.minute < 60 and 0 <= self.second < 60


def format_time(t):
    """Return time object as a formatted string."""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'


def time_to_sec(time):
    """Convert a time object to the total seconds since midnight."""
    return time.hour * 3600 + time.minute * 60 + time.second


def sec_to_time(seconds):
    """Convert total seconds since midnight into a Time object."""
    t = Time()
    t.hour, rem = divmod(seconds, 3600)
    t.minute, t.second = divmod(rem, 60)
    return t


def sum_times(t1, t2):
    """Add two time objects and return the sum."""
    total_seconds = time_to_sec(t1) + time_to_sec(t2)
    return sec_to_time(total_seconds)


def change_time(time, seconds):
    """Modify a time object by adding or subtracting seconds."""
    total_seconds = time_to_sec(time) + seconds
    total_seconds %= 86400  # Ensure seconds stay within one day
    updated_time = sec_to_time(total_seconds)
    time.hour, time.minute, time.second = updated_time.hour, updated_time.minute, updated_time.second
