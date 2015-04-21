

from collections import defaultdict


class Scheduler(object):

    def __init__(self, num_machines, jobs):
        self.machines = [[] for x in range(num_machines)]
        self.not_processed = []
        self.jobs = jobs
        # self.m = job collision matrix / graph
        self.m = defaultdict(lambda: defaultdict(lambda: False))
        for jid1, job1 in enumerate(jobs):
            for jid2, job2 in enumerate(jobs):
                # Check if there was a collision
                j1_start, j1_end = job1
                j2_start, j2_end = job2
                if j2_start < j1_end and j2_end > j1_start:
                    self.m[jid1][jid2] = True  # Yes, there was a collision

    def find_machine(self, jid):
        """
        Search all machines for a place to put the job without it colliding
        with another. Prefer to fill up an already in use machine over an empty
        one for the optimal solution.

        If a job cannot find a machine that can accept it, it is a lost job and
        should be put into the list of not_processed.
        """
        for machine in self.machines:
            if machine == []:
                machine.append(jid)
                return
            conflict_found = False
            for scheduled_jid in machine:
                if self.m[jid][scheduled_jid] is True:
                    conflict_found = True
                    break
            if conflict_found is False:
                machine.append(jid)
                return
        self.not_processed.append(jid)
        return

    def schedule(self):
        """
        Schedule the jobs; get the jobs in order so to be passed into the
        find_machine function.

        Sort the collision matrix in increasing number of collisions.
        See proof as to why this will result in the optimal solution.
        """
        sorted_m = sorted(self.m.items(), key=lambda x: len(x[1]))
        for jid, collisions in sorted_m:
            self.find_machine(jid)

    def print_schedule(self):
        """
        Go through every machine, which lists the jobs assigned to it.
        Count all jobs that have been assigned to any machines to and
        print the each machine's jobs.

        Then print out all jobs that have not been assigned, thus have failed
        to be processed.

        Finally print the number of jobs processed out of the total submitted.
        """
        count = 0
        for i, machine in enumerate(self.machines):
            print "Machine #" + str(i) + " has jobs: "
            for jid in machine:
                count += 1
                print str(self.jobs[jid])
        if self.not_processed != []:
            print "Jobs not processed: "
            for jid in self.not_processed:
                print str(self.jobs[jid])
        print str(count) + " number of jobs out of a possible " + \
            str(len(self.jobs)) + " total submitted."


def read_input(filename):
    """
    Read the specified input file, return number of machines and list of jobs.
    Returned data format is a tuple containg the number of machines,
    and a list of tuples containing job start and end times.

    Arguments:
        filename - Path to input file. First line is the number of machines,
                all subsequent lines are jobs "JOB_START_TIME JOB_END_TIME".

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
    num_machines, jobs = read_input("input.txt")
    scheduler = Scheduler(num_machines, jobs)
    scheduler.schedule()
    scheduler.print_schedule()
