'''
#This is exercise 4.1:

import nsfg
import thinkstats2
import thinkplot

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]
firsts = live[live.birthord == 1]

def birthweightpercentilerank(myweight, population):
    cdf = thinkstats2.Cdf(population.totalwgt_lb, label='birthweight')
    rank = cdf.PercentileRank(myweight)
    print(live.totalwgt_lb.shape)
    # print(sorted(live.totalwgt_lb, reverse=True))
    return rank

print(birthweightpercentilerank(8.3, firsts))
'''



'''
#This is exercise 5.1:

import thinkstats2
import thinkplot
import scipy.stats
import numpy as np

mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)
print(dist.cdf(185.42) - dist.cdf(177.8))


#just for kicks, lets practice plotting the normal CDF given these parameters:

thinkplot.PrePlot(1)
xs, ps = thinkstats2.RenderNormalCdf(mu=mu, sigma=sigma, low = 150, high = 200)
label = r'$\mu=%g$, $\sigma=%g$' % (mu, sigma)
thinkplot.Plot(xs, ps, label=label)
thinkplot.Show()

#lets also plot the normal probability plot:
sample = np.random.normal(mu, sigma, 100)
xs1, ys1 = thinkstats2.NormalProbability(sample)
label = '$\mu=%d$, $\sigma=%d$' % (mu, sigma)
thinkplot.Plot(xs1, ys1, label=label)
thinkplot.Show()
'''