# scheduler.py

from job import Job
import os
from adaptable_heap_priority_queue import AdaptableHeapPriorityQueue as AHPQ


class Scheduler(AHPQ):
    """Scheduler class gets job schedules from a file
    and runs each job based on it priority and length"""
    __slots__ = '__time_slice', '__locations', '__headers'

    def __init__(self, time_slice=0):
        super().__init__()
        self.__time_slice = time_slice
        self.__locations = dict()
        self.__headers = {'job': 0, 'priority': 1, 'length': 2}

    def read(self, filename):
        """Parse a job file and save the jobs to memory"""
        with open(filename, 'r') as jobs:
            self._parse_header(jobs)
            self._parse_jobs(jobs)

    def _parse_header(self, lines):
        headers = lines.readline().strip().lower().split(',')
        for i, header in enumerate(headers):
            self.__headers[header] = i

    def _parse_jobs(self, lines):
        lines = lines.readlines()
        for line in lines:
            line = line.strip().lower().split(',')
            job = Job(line[self.__headers['job']],
                      int(line[self.__headers['priority']]),
                      int(line[self.__headers['length']]))
            loc = self.add(job, job)
            self.__locations[job.get_title()] = loc

    def run(self):
        """Executes all of the jobs in order of priority"""
        while not self.is_empty():
            try:
                while True:
                    if not self.min()[0].run(self.__time_slice):
                        break
                self.remove_min()
            except KeyboardInterrupt:
                self.min()[0].fix_step()
                self.halt()
        print("All jobs has been successfully executed.")

    def halt(self):
        """Pause the job execution process to show current remaining jobs
        and/or add or alternate a job"""
        try:
            print('\nScheduler has been halted...\n')
            print(self)

            ans = input("New job? (y/n):")
            if 'y' in ans.strip().lower():
                title = input("New job name:")
                priority = int(input("New job priority:"))
                length = int(input("New job length:"))
                job = Job(title, priority, length)
                self.add(job, job)

            ans = input("Alter priority? (y/n):")
            if 'y' in ans.strip().lower():
                title = input("Job name:")
                if not title in self.__locations.keys():
                    raise KeyError \
                    (title + " is not in the list of running scheduled jobs!")
                priority = int(input("New job priority:"))
                loc = self.__locations[title]
                loc._value.set_priority(priority)
                self.update(loc, loc._key, loc._value)

        except KeyboardInterrupt:
            print("\nScheduler has been successfully stopped!")
            quit()
        except Exception as e:
            print(e)
            answer = input("Do you want to continue? (y/n)")
            if 'n' in answer.strip().lower():
                quit()

        print('\nRestarting scheduler...\n')

    def __repr__(self):
        """Prints jobs with priority and length"""
        output = '{:15}{:^10}{:>10}'.format('Job', 'Priority', 'Length')
        output += os.linesep
        output += '-' * 36
        output += os.linesep

        for item in self._data:
            output += repr(item._value)
            output += os.linesep
        return output

if __name__ == '__main__':
    print("This is a job scheduler class")