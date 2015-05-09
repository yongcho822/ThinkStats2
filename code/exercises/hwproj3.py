import random
import nsfg
import thinkstats2
import thinkplot

sample = [random.random() for x in range(1000)]

pmf = thinkstats2.Pmf(sample)
cdf = thinkstats2.Cdf(sample)

thinkplot.PrePlot(1, cols=2)
thinkplot.Pmfs([pmf])
thinkplot.Show(xlabel = 'random numbers between 0 and 1', ylabel = 'PMF')

thinkplot.PrePlot(1)
thinkplot.SubPlot(2)
thinkplot.Cdfs([cdf])
thinkplot.Show(xlabel = 'random numbers between 0 and 1', ylabel = 'CDF')

'''
The distribution is uniform, as we can tell no single probability exceeds 0.001,
and the CDF is approximately a straight line, with no extreme dips or peaks,
telling us the distribution is a uniform one.
'''






'''
This is exercise 4.1: Ignore

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]

def birthweightpercentilerank(myweight, population):
    cdf = thinkstats2.Cdf(population.totalwgt_lb, label='birthweight')
    rank = cdf.PercentileRank(myweight)
    print(live.totalwgt_lb.shape)
    # print(sorted(live.totalwgt_lb, reverse=True))
    return rank

print(birthweightpercentilerank(8.3, live))
'''
