
# coding: utf-8

# In[24]:

import numpy as np
import nsfg
from __future__ import division

class DiffMeansPermute(object):
    def __init__(self, data):
        self.data = data
        self.MakeModel()
        self.actual = self.TestStatistic(data)
    def PValue(self, iters = 1000):
        self.test_stats = [self.TestStatistic(self.RunModel()) for i in range(iters)]
        count = sum(1 for x in self.test_stats if x >= self.actual)
        return count/iters
    def TestStatistic(self, data):
        group1, group2 = data
        test_stat = abs(group1.mean() - group2.mean())
        return test_stat
    def MakeModel(self):
        group1, group2 = self.data
        self.n, self.m = len(group1), len(group2)
        self.pool = np.hstack((group1, group2))
    def RunModel(self):
        np.random.shuffle(self.pool)
        data = self.pool[:self.n], self.pool[self.n:]
        return data

class DiffMeansResample(DiffMeansPermute):
    def RunModel(self):
        group1 = np.random.choice(self.pool, self.n, replace=True)
        group2 = np.random.choice(self.pool, self.m, replace=True)
        return group1, group2
    
preg = nsfg.ReadFemPreg()

live = preg[preg.outcome == 1]
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

dataprglngth = firsts.prglngth.values, others.prglngth.values
databirthweight = firsts.totalwgt_lb.values, others.totalwgt_lb.values

permuteprglngth = DiffMeansPermute(dataprglngth)
resampleprglngth = DiffMeansResample(dataprglngth)
print 'Preg Length Hypo Testing with Permutations - PValue:', permuteprglngth.PValue()
print 'Preg Length Hypo Testing with Resampling - PValue:', resampleprglngth.PValue()

permutebirthweight = DiffMeansPermute(databirthweight)
resamplebirthweight = DiffMeansResample(databirthweight)
print 'Birth Weight Hypo Testing with Permutations - PValue:', permutebirthweight.PValue()
print 'Birth Weight Hypo Testing with Resampling - PValue:', resamplebirthweight.PValue()

'''
With these results:

Preg Length Hypo Testing with Permutations - PValue: 0.182
Preg Length Hypo Testing with Resampling - PValue: 0.172
Birth Weight Hypo Testing with Permutations - PValue: 0.0
Birth Weight Hypo Testing with Resampling - PValue: 0.0

The different model affects the result slightly, but seems like it isn't an earth-shattering difference.
It seems that it would be a good idea to try multiple sampling methods when carrying out experiments
such as these to test for outliers and/or found an average P-Value across all these methods.
'''


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



