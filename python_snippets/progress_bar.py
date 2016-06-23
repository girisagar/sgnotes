import sys
import time

class ProgressBar():
    def __init__(self, total, prefix = '', suffix = '', decimals = 2, bar_length = 100):
        self.total = total
        self.prefix = prefix
        self.suffix = suffix
        self.decimals = decimals
        self.bar_length = bar_length

    def print_progress(self, iteration):
        # time.sleep(1)
        filled_length = int(round(self.bar_length * iteration / float(self.total)))
        percents = round(100.00 * (iteration / float(self.total)), self.decimals)
        bar = '=' * filled_length + '=>' + ' ' * (self.bar_length - filled_length)
        sys.stdout.write('%s [%s] %s%s %s\r' % (self.prefix, bar, percents, '%', self.suffix)),
        sys.stdout.flush()
        if iteration == self.total:
            print("\n")

def test_progress_bar():
    items = ["a", "b", "c", "d", "e"]
    i = 0
    total = len(items)
    progress = ProgressBar(total, prefix='Iterations', suffix='Complete', bar_length=50)

    for item in items:

        # Do stuff
	time.sleep(0.5)
        # print i
        i += 1
        progress.print_progress(i)

if __name__ == "__main__":
    test_progress_bar()
