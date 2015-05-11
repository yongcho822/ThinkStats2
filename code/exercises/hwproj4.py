import numpy as np
import thinkplot
import thinkstats2
import nsfg

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]
live = live.dropna(subset = ['agepreg', 'totalwgt_lb'])

bins = np.arange(10,50,3)
indices = np.digitize(live.agepreg, bins)
groups = live.groupby(indices)

ages = [group.agepreg.mean() for i, group in groups]
cdfs = [thinkstats2.Cdf(group.totalwgt_lb) for i, group in groups]

for percent in [75, 50, 25]:
    weights = [cdf.Percentile(percent) for cdf in cdfs]
    label = '%dth' %percent
    thinkplot.Plot(ages, weights, label=label)
thinkplot.Show(xlabel = "mother's age", ylabel = "birth weight")

ages_scatter = live.agepreg
weights_scatter = live.totalwgt_lb
thinkplot.Scatter(ages_scatter, weights_scatter, alpha = 0.2)
thinkplot.Show(xlabel = "mother's age", ylabel = "birth weight", axis = [10, 45, 0, 15])

Pearsons = thinkstats2.Corr(live.agepreg, live.totalwgt_lb)
print("Pearson's Corr:", Pearsons)

Spearmans = thinkstats2.SpearmanCorr(live.agepreg, live.totalwgt_lb)
print("Spearman's Corr:", Spearmans)

#Judging by the scatterplot, these two variables seem to have minimal correlation, as the dense chunk
#of the scatterplot is basically horizontal.The small correlation values reinforce what we see. Older
#mothers tend to have slightly heavier babies, but ever the slightest with correlation coefficients lower
#than 0.1. Pearson's Correlation coefficient might be smaller as baby weights may slightly be skewed
#lower with some really light babies as outliers. Or perhaps this is a nonlinear relationship, as plotting
#percentiles of weight vs age show us that baby weights increase at a faster rate during the early 20s
#then slows down.
