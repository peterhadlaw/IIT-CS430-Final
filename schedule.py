

class Scheduler(object):

    def __init__(self, num_machines, jobs):
        self.num_machines = num_machines
        self.jobs = jobs

    def schedule(self):
        pass


def read_input(filename):
    pass

if __name__ == '__main__':
    num_machines, jobs = read_input("input.txt")
    scheduler = Scheduler(num_machines, jobs)
    scheduler.schedule()
