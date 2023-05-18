import time

### Timer Functions ###

# Timer duration in seconds
timer_duration = 720

def start_timer(duration):
        start_time = time.time()
        end_time = start_time + duration
        return end_time

def print_time_remaining(time):
        if time > 60:
            print(f"You have {round(time / 60)} minutes remaining.\n")
        elif 60 >= time > 1:
            print(f"You have {time} seconds remaining.\n")
        else:
            print(f"You have 1 second remaining.\n")