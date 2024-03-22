from P16_11 import convexHull
from P16_12 import Graham_algo
import time

def main():
    s = '400'
    fname = str(s)+".dat"
    infile = open(fname,"rb")
    points = pickle.load(infile)
    print(len(points))
    
