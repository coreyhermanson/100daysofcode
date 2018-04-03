from datetime import datetime
from datetime import timedelta
import itertools


def header():
    print('==========================================================')
    print('==== Pomodoro Timer using only date and datetime ====')
    print('==========================================================')


def main():
    # print header
    header()

    # Execute timer
    timer()


def timer():
    sequence = [25, 5, 25, 5, 25, 5, 25, 20, ]

    try:
        while True:
            work_time = True
            for duration in itertools.cycle(sequence):
                current_time = datetime.now()
                alarm_time = current_time + timedelta(minutes=duration)
                print(f"The current time is {current_time.strftime('%H:%M')}. The next alarm will go off at "
                      f"{alarm_time.strftime('%H:%M')}")

                if current_time > alarm_time:
                    if work_time:
                        next_break = current_time + timedelta(minutes=25)
                        print(f"Time to get to work for 25 minutes. Your next break will be at "
                              f"{next_break}")
                    else:
                        next_work = current_time + timedelta(minutes=duration)
                        print(f"Break time for {duration} minutes. You will resume working at {next_work}")

                    work_time = not work_time

    except KeyboardInterrupt:
        print("You have aborted the Pomodoro Timer")


if __name__ == '__main__':
    main()
