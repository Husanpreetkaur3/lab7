#!/usr/bin/env python3
# Student ID: husanpreet-kaur3

class Time:
    """Simple object type for time of the day."""
    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for Time object."""
        self.hour = hour
        self.minute = minute
        self.second = second

    def time_to_sec(self):
        """Convert a time object to the total seconds since midnight."""
        return self.hour * 3600 + self.minute * 60 + self.second

    def valid_time(self):
        """Check if time is valid."""
        return 0 <= self.hour < 24 and 0 <= self.minute < 60 and 0 <= self.second < 60

    def __add__(self, t2):
        """Overload the + operator to add two Time objects."""
        total_seconds = self.time_to_sec() + t2.time_to_sec()
        return sec_to_time(total_seconds)

    def __str__(self):
        """String representation for printing."""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        """Representation for interactive shell."""
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'

def sec_to_time(seconds):
    """Convert total seconds since midnight to a Time object."""
    t = Time()
    t.hour, rem = divmod(seconds, 3600)
    t.minute, t.second = divmod(rem, 60)
    return t
