import thinkstats2
import thinkplot
import numpy as np
import math

def RMSE(estimates, actual):
    e2 = [(estimate-actual)**2 for estimate in estimates]
    mse = np.mean(e2)
    return math.sqrt(mse)

def VertLine(x, y=1):
    thinkplot.Plot([x, x], [0, y], color='0.8', linewidth=3)

def Estimate(n=10, m=1000):
    lam = 2
    means = []
    for _ in range(m):
        xs = np.random.exponential(1./lam, n)
        L = 1/np.mean(xs)
        means.append(L)
    stderr = RMSE(means, lam)
    return stderr

def PlotInitial(n=10, m=1000):
    lam = 2
    means = []
    for _ in range(m):
        xs = np.random.exponential(1./lam, n)
        L = 1/np.mean(xs)
        means.append(L)
    cdf = thinkstats2.Cdf(means)
    ci = cdf.Percentile(5), cdf.Percentile(95)
    VertLine(ci[0])
    VertLine(ci[1])
    stderr = RMSE(means, lam)
    print("standard error:", stderr)
    print("90% CI is from", ci[0], "to", ci[1])
    thinkplot.Cdf(cdf)
    thinkplot.Show(xlabel = 'sample mean (L)', ylabel = 'CDF')

PlotInitial()

ranges = []
stderrs = []
for n in range(10,510,50):
    stderr = Estimate(n=n)
    ranges.append(n)
    stderrs.append(stderr)
    print(n, stderr)

thinkplot.Plot(ranges, stderrs)
thinkplot.Show(xlabel = 'sample size n', ylabel = 'standard error')

#the standard error decreases and approaches 0 as our sample size increases.
#This tells us that L is an unbiased estimator of lambda.