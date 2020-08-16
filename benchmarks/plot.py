import matplotlib.pyplot as plt
import numpy as np
import sys

if len(sys.argv) < 1:
    print("""usage: %s file1 file2 figure.svg
          """ % sys.argv[0])
    exit(1)

def parse(filename):
    lines = open(filename).readlines()
    label = lines[0].split()[1]
    num_sizes = len(lines) - 1
    size = np.zeros((num_sizes, 1))
    elapsed = np.zeros((num_sizes, 1))
    work_rate = np.zeros((num_sizes, 1))
    for i, line in enumerate(lines[1:]):
        fields = ' '.join(line.split()).split()
        size[i] = fields[0]
        elapsed[i] = fields[1]
        work_rate[i] = fields[3]
    return {"label" : label, "size" : size, "elapsed" : elapsed, "work_rate" : work_rate}


figfile = sys.argv[-1]
for arg in sys.argv[1:-1]:
    data = parse(arg)
    plt.loglog(data["size"][1:], data["work_rate"][1:], label=data["label"])
plt.legend(loc="best")
plt.xlabel("Number of elements")
plt.ylabel("Elements / ns")
plt.savefig(figfile)
plt.show()


