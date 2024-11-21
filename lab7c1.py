#!/usr/bin/env python3
# Student ID: husanpreet-kaur3

from lab7c import *

# Define time objects
t1 = Time(8, 0, 0)
t2 = Time(8, 55, 0)
t3 = Time(9, 50, 0)

# Define duration object
td = Time(0, 50, 0)

# Perform operations
tsum1 = sum_times(t1, td)  # Sum t1 and td
tsum2 = sum_times(t2, td)  # Sum t2 and td
change_time(t3, 1800)      # Add 1800 seconds to t3

# Format and print results
ft = format_time
print(ft(t1), '+', ft(td), '-->', ft(tsum1))
print(ft(t2), '+', ft(td), '-->', ft(tsum2))
print('09:50:00 + 1800 sec', '-->', ft(t3))
