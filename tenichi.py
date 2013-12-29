#!/usr/bin/env python
import numpy
import datetime
import pylab

def readdta( path ):
    data = numpy.loadtxt(path, \
	dtype = { 'names': ('date', 'name'), \
		'formats': ('S10', 'S20')} )
    return data['date']

def converter( x ):
    return datetime.datetime.strptime(x, "%m/%d")

if __name__ == "__main__":
    vconverter=numpy.vectorize(converter)
    interval=numpy.array(map(lambda x:x.days, numpy.diff(vconverter(readdta("date")))))
    pylab.hist( interval, bins=6, range=(0,42) )

    pylab.title("mean = %.1lf, median = %.1lf" \
	 % (interval.mean(), numpy.median(interval)))
    pylab.xlabel("Interval in days")
    pylab.ylabel("Frequency")
    pylab.show()
    
