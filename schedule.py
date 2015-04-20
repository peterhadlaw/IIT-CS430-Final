

class Scheduler(object):

    def __init__(self, num_machines, jobs):
        self.num_machines = num_machines
        self.jobs = jobs

    def schedule(self):
        pass


def read_input(filename):
    # returns tuple
    # (num_machines,[(job_start,finish),...])
    f = open(filename)
    machines = f.readline()
    machines = int(machines)
    jobs = []
    while True:
        line = f.readline()
        if not line:
            break
        job = line.split()
        job = (int(job[0]), int(job[1]))
        jobs.append(job)
    return (machines, jobs)


if __name__ == '__main__':
    num_machines, jobs = read_input("jobs.txt")
    scheduler = Scheduler(num_machines, jobs)
    scheduler.schedule()
