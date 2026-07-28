# @Program: Time Module in Python
# @Author: Saloni Malhotra
# @Date: 28-07-2026

"""
 ============================================================
        TIME MODULE IN PYTHON (Quick Revision)
 ============================================================

 Definition:
 The time module is a built-in Python module used to work with
 current time, timestamps, delays, formatting, and execution time.

import time

 ------------------------------------------------------------
                Common Functions
 ------------------------------------------------------------

 time.time()
 Returns the current Unix timestamp
 (seconds since 1 January 1970).

 time.sleep(seconds)
 Pauses program execution for the given number of seconds.

 time.ctime([timestamp])
 Converts a timestamp into a human-readable date and time.

 time.localtime([timestamp])
 Returns local date and time as a struct_time object.

 time.gmtime([timestamp])
 Returns UTC (Greenwich Mean Time) as a struct_time object.

 time.strftime(format, time_object)
 Formats date and time into a custom string.

 time.perf_counter()
 High-precision timer used to measure execution time.

 time.process_time()
 Returns CPU time used by the current process.
 Sleep time is NOT included.

 ------------------------------------------------------------
 Common strftime() Format Codes
 ------------------------------------------------------------

 %d -> Day (01-31)
 %m -> Month (01-12)
 %Y -> Year (4 digits)
 %y -> Year (2 digits)
 %H -> Hour (24-hour)
 %I -> Hour (12-hour)
 %M -> Minutes
 %S -> Seconds
 %p -> AM / PM
 %A -> Full weekday name
 %a -> Short weekday name
 %B -> Full month name
 %b -> Short month name

 ------------------------------------------------------------
 Quick Revision
 ------------------------------------------------------------

 time.time()         -> Current Unix timestamp
 time.sleep(sec)     -> Pause program execution
 time.ctime()        -> Readable date & time
 time.localtime()    -> Local time (struct_time)
 time.gmtime()       -> UTC time (struct_time)
 time.strftime()     -> Format date & time
 time.perf_counter() -> Measure execution time (high precision)
 time.process_time() -> Measure CPU execution time

 ------------------------------------------------------------
 Interview Questions
 ------------------------------------------------------------

 Q1. What is the time module?
 Built-in module used for working with time, timestamps,
 delays, formatting, and execution time.

 Q2. Difference between time.time() and time.ctime()?
 time.time()  -> Returns Unix timestamp.
 time.ctime() -> Returns readable date & time.

 Q3. Difference between localtime() and gmtime()?
 localtime() -> Local system time.
 gmtime()    -> UTC (Greenwich Mean Time).

 Q4. Why is time.sleep() used?
 To pause program execution for a specified time.

 Q5. Which function is best for measuring execution time?
 time.perf_counter()

"""

import time

# 1st Program => dir
# ______________________________________________________________________________________

print(dir(time))
print("=" * 80, "\n")

# 2nd @Program => time.time()
# Returns the current time as the number of seconds since January 1, 1970 (Unix Epoch).
# ______________________________________________________________________________________

current_time = time.time()
print(current_time)
print("=" * 80, "\n")

# 3rd Program => time.sleep(seconds)
# Pauses (delays) the program for the specified number of seconds.
# ______________________________________________________________________________________

print("Start")
time.sleep(3)
print("End")
print("=" * 80, "\n")

# 4th Program => time.ctime()
# Converts a timestamp into a readable date and time.
# ______________________________________________________________________________________

print(time.ctime())

# Using timeStamp
timestamp = time.time()
print(time.ctime(timestamp))
print("=" * 80, "\n")

# 5th Program => time.localtime()
# Returns the current local time as a struct_time object
# ______________________________________________________________________________________

current = time.localtime()
print(current)

# Access individual values:
print(current.tm_year)
print(current.tm_mon)
print(current.tm_mday)
print("=" * 80, "\n")

# 6th Program => time.strftime(format)
# Formats date and time into a custom string.
# ______________________________________________________________________________________

current = time.localtime()
formatted = time.strftime("%d-%m-%Y %H:%M:%S", current)
print(formatted)
print("=" * 80, "\n")

# 7th Program => time.gmtime()
# Returns the current UTC (Greenwich Mean Time).
# ______________________________________________________________________________________

print(time.gmtime())
print("=" * 80, "\n")

# 8th Program => time.perf_counter()
# High-precision timer used to measure execution time.
# ______________________________________________________________________________________

start = time.perf_counter()
for i in range(1000000):
    pass

end = time.perf_counter()

print("Execution Time:", end - start)
print("=" * 80, "\n")

# 9th Program => time.process_time()
# Returns the CPU time used by the current process (ignores sleep time).
# ______________________________________________________________________________________

start = time.process_time()
for i in range(1000000):
    pass

end = time.process_time()
print(end - start)
print("=" * 80, "\n")
