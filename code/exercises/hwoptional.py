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

'''
#This is exercise 6.1:

import numpy as np
import density
import hinc
import thinkplot
import thinkstats2

def InterpolateSample(df, log_upper = 6.0):
    df['log_upper'] = np.log10(df.income)
    df['log_lower'] = df.log_upper.shift(1)
    df['log_lower'][0] = 3.0
    df['log_upper'][41] = log_upper

    arrays = []
    for _, row in df.iterrows():
        vals = np.linspace(row.log_lower, row.log_upper, row.freq)
        arrays.append(vals)
    log_sample = np.concatenate(arrays)
    return log_sample

df = hinc.ReadData()
log_sample = InterpolateSample(df)

log_cdf = thinkstats2.Cdf(log_sample)
thinkplot.Cdf(log_cdf)
thinkplot.Show(xlabel = 'household income', ylabel = 'CDF')

sample = np.power(10, log_sample)

mean = sample.mean()
print("mean:",mean)
std = sample.std()
print("std:",std)
median = thinkstats2.Median(sample)
print("median",median)
skewness = thinkstats2.Skewness(sample)
print("skewness",skewness)
PearsonSkewness = thinkstats2.PearsonMedianSkewness(sample)
print("Pearson Skewness:", PearsonSkewness)
cdf_mean = thinkstats2.Cdf(sample)[mean]
print("cdf mean (fraction of households reporting below the mean:", cdf_mean)

pdf = thinkstats2.EstimatedPdf(sample)
thinkplot.Pdf(pdf, label="sample KDE")
thinkplot.Show(xlabel = "income", ylabel = "PDF")

#when you change the upper bound, it seems as though mean and std both increase with a higher upper bound,
#decrease, with a lower bound. The traditional skewness increases with a higher upper bound, but the Pearson
#skewness does not. This seems to be because the much larger increase in std is in the denominator, and
#thus actually decreases the Pearson's Skewness value in this case.
'''
