

class Scheduler(object):

    def __init__(self, num_machines, jobs):
        self.num_machines = num_machines
        self.jobs = jobs

    def schedule(self):
        pass


def read_input(filename):
    """
    Read the specified input file, return number of machines and list of jobs.
    Returned data format is a tuple containg the number of machines,
    and a list of tuples containing job start and end times.

    Arguments:
        filename - Path to input file. First line is the number of machines, all
                subsequent lines are jobs "JOB_START_TIME JOB_END_TIME".

                Example:

                3               <- number of machines
                0 3             <- job starting at 0, ending at 3
                0 1             <- job starting at 0, ending at 1
                1 2             <- job starting at 1, ending at 2
                1 4             <- job starting at 1, ending at 4

    Return Value:
        Note: job listing is in no particular order
        (number_machines, [(job_start, job_end), (job_start, job_end), ...])
    """
    f = open(filename)
    machines = int(f.readline())
    jobs = []
    while True:
        line = f.readline()
        if not line:
            break
        job = line.split()
        jobs.append((int(job[0]), int(job[1])))
    return (machines, jobs)


if __name__ == '__main__':
    num_machines, jobs = read_input("jobs.txt")
    scheduler = Scheduler(num_machines, jobs)
    scheduler.schedule()
