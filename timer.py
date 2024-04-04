import time

def chrono(time_begin):
    actual_time = time.time()
    time_elapsed = actual_time - time_begin
    seconds = int(time_elapsed % 60)
    return seconds