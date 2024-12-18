#!/usr/bin/env python3
# Student ID: husanpreet-kaur3

class Time:
    def __init__(self, hour=12, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def format_time(self):
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def time_to_sec(self):
        return self.hour * 3600 + self.minute * 60 + self.second

    def valid_time(self):
        return 0 <= self.hour < 24 and 0 <= self.minute < 60 and 0 <= self.second < 60

    def change_time(self, seconds):
        total_seconds = self.time_to_sec() + seconds
        time_obj = sec_to_time(total_seconds)
        self.hour, self.minute, self.second = time_obj.hour, time_obj.minute, time_obj.second

    def sum_times(self, t2):
        total_seconds = self.time_to_sec() + t2.time_to_sec()
        return sec_to_time(total_seconds)

def sec_to_time(seconds):
    t = Time()
    t.hour, rem = divmod(seconds, 3600)
    t.minute, t.second = divmod(rem, 60)
    return t
