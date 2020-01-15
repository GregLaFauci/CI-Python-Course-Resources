import gzip
import sys
import os

opener = gzip.open

if __name__ == "__main__":
    f = opener(sys.argv[1], 'wt')
    f.write(' '.join(sys.argv[2:]))
    f.close()