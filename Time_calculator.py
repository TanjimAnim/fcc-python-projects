def add_time(start_time, duration):
    start_time = start_time.split()
    duration = duration.split()
    start_time_hour = start_time[0].split()
    print(start_time_hour, duration)


add_time("3:00 PM", "3:10")
