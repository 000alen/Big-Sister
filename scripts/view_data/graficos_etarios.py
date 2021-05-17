import random
import numpy
from matplotlib import pyplot
import csv
import os

root = os.path.abspath("../")

csv_reader = csv.reader(open( root + "/Big-Sister/databases/OUT/servel/clean_etareo_comunas.csv"), delimiter = ',')
header = [18.5,22,27,32,37,42,47,52,57,62,67,72,77,82]

#for i in csv_reader:
#    if i[0] != "Sexo":
#        # Generate a normal distribution, center at x=0 and y=5
#        x = header
#        y = i[3:-1]

#        fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)

        # We can set the number of bins with the `bins` kwarg
#        axs[0].hist(x,bins=n_bins)
#       axs[1].hist(y,bins=n_bins)

#        plt.show()



x = [1738,5322,5833,5214,4374,4366,4267,5208,5361,3957,2760,1933,1462,2619]
y = [8241,20317,27172,35373,33733,30134,26242,25952,23694,19174,15522,12464,8418,16099]

bins = numpy.linspace(0, 16000, 100)

pyplot.hist(x, bins, alpha=0.5, label='x')
pyplot.hist(y, bins, alpha=0.5, label='y')

pyplot.legend(loc='upper right')
pyplot.show()