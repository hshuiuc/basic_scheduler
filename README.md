Description
-----
This application is a batch job schedule runner with ability of adding new jobs
and changing job priorities. It demonstrates a simplified version of operation
system multi threading.
This application accepts a job schedule list as input argument
and runs a batch based on job priorities.

Dependencies
-----
- job.py
- scheduler.py
- adaptable_heap_priority_queue.py
- Empty.py
- heap_priority_queue.py
- priority_queue_base.py


Requirements
-----
- Python 3
- python libraries:
    - sys
    - os
    - time

Run as
-----
$ python project3.py <input-job-listing> <sleep-time>

Operation
-----
Ctrl/Command + C -> halts the process to add or alternate a job
Ctrl/Command + C (X2) -> quits the scheduler

Output
-----
a table of current jobs in the scheduler.

Disclaimer
-----
This application doesn't guarantee correct output with a none standard file
format. Check job file as an example.
