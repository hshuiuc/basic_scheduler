# project3.py


from scheduler import Scheduler
import sys
from Empty import Empty

if __name__ == '__main__':

    try:
        args_length = len(sys.argv)
        if args_length < 2:
            raise IndexError("First Argument is required!\n"
                             " project3.py <input-jobs> <sleep-time>")
        if args_length == 2:
            time_slice = 0
        else:
            time_slice = sys.argv[2]
        my_scheduler = Scheduler(time_slice)
        my_scheduler.read(sys.argv[1])
        my_scheduler.run()
        print("Quiting...")
    except Exception as e:
        print(e)

