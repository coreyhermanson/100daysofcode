import time
from datetime import datetime
from datetime import timedelta
import itertools


def main():
    # print header
    header()

    # Execute timer
    timer()


def header():
    print('==========================================================')
    print('====== Pomodoro Timer using only date and datetime ======')
    print('==========================================================')
    print('')
    print('Press CTRL + C to cancel the timer')
    print('')


def timer():
    sequence = [25, 5, 25, 5, 25, 5, 25, 20, ]

    try:
        work_time = True

        for duration in itertools.cycle(sequence):
            alarm_time = datetime.now() + timedelta(minutes=duration)

            if work_time:
                print(f"Time to work! The current time is {datetime.now().strftime('%H:%M')}. "
                      f"The current work period is {duration} minutes and the next alarm will go"
                      f" off at {alarm_time.strftime('%H:%M')}")
            else:
                next_work = datetime.now() + timedelta(minutes=duration)
                print(f"Break time! Take a break for {duration} minutes. "
                      f"You will resume working at {next_work.strftime('%H:%M:%S')}")

            while True:
                time.sleep(1)
                current_time = datetime.now()
                if current_time > alarm_time:
                    work_time = not work_time
                    break

    except KeyboardInterrupt:
        print("You have aborted the Pomodoro Timer")


if __name__ == '__main__':
    main()
