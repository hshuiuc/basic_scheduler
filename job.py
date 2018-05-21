# job.py

import time


class Job:
    """"This class holds a job information and runs it"""
    __slots__ = '__title', '__priority', '__length', '__steps'

    def __init__(self, title, priority, length, finished_steps=0):
        self.__title = title
        self._validate(priority, -20, 19)
        self.__priority = priority
        self._validate(length, 0, 100)
        self.__length = length
        self._validate(finished_steps, 0, length - 1)
        self.__steps = finished_steps

    def __lt__(self, other):
        if not isinstance(other, Job):
            return False
        if self.get_priority() < other.get_priority():
            return True
        elif self.get_priority() == other.get_priority():
            if self.get_length() < other.get_length():
                return True
            elif self.get_length() == other.get_length():
                if self.get_title() < other.get_title():
                    return True
        return False

    def __eq__(self, other):
        if not isinstance(other, self):
            return False
        if self.get_priority() == other.get_priority()\
                and self.get_length() == other.get_length()\
                and self.get_title() == other.get_title():
            return True
        return False

    def __ne__(self, other):
        return not (self == other)

    def __gt__(self, other):
        return not (self == other or self < other)

    @staticmethod
    def _validate(value, down_bound, up_bound, data_type=int):
        if not isinstance(value, data_type):
            raise TypeError('{} must be a value of type {}'.format
                            (value, data_type))
        if not down_bound <= value <= up_bound:
            raise ValueError('{} must be in range of {} and {}'.format
                             (value, down_bound, up_bound))

    def get_title(self):
        return self.__title

    def get_priority(self):
        return self.__priority

    def get_length(self):
        return self.__length

    def get_steps(self):
        return self.__steps

    def set_title(self, name):
        self.__title = name

    def set_priority(self, priority):
        self.__priority = priority

    def set_length(self, length):
        self.__length = length

    def run(self, time_slice):
        """This method runs a job
        and prints current job status after each turn"""
        self._step_up()
        if self.get_length() - self.get_steps() < 0:
            return False
        output = 'running {0!r} with priority {1}, step {2} out of {3}' \
            .format(self.get_title(), self.get_priority(),
                    self.get_steps(), self.get_length())
        time.sleep(float(time_slice))
        print(output)
        return self.get_length() - self.get_steps()

    def _step_up(self):
        self.__steps += 1

    def fix_step(self):
        self.__steps -= 1

    def __repr__(self):
        """Prints a job and it priority and length in a table format"""
        output = '{:15.13}{:^10}{:>10}'.format(
            self.get_title(), self.get_priority(),
            self.get_length()-self.get_steps())
        return output

if __name__ == '__main__':
    print("This is a job class")
