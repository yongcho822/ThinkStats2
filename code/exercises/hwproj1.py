__author__ = 'yongcho822'

import sys
import thinkstats2
import nsfg
import math

def MakeFrames():

    preg = nsfg.ReadFemPreg()

    live = preg[preg.outcome == 1]
    firsts = live[live.birthord == 1]
    others = live[live.birthord != 1]

    return live, firsts, others

def WeightDiff(live, firsts, others):
    '''doing cohen's d effect size'''
    meanlive = live.totalwgt_lb.mean()
    meanfirsts = firsts.totalwgt_lb.mean()
    meanothers = others.totalwgt_lb.mean()

    varlive = live.totalwgt_lb.var()
    varfirsts = firsts.totalwgt_lb.var()
    varothers = others.totalwgt_lb.var()

    n1, n2 = len(firsts.totalwgt_lb), len(others.totalwgt_lb)

    wgtdiff = meanfirsts - meanothers

    pooled_wgt_var = (n1 * varfirsts + n2 * varothers)/(n1+n2)
    d = wgtdiff / math.sqrt(pooled_wgt_var)
    print "Cohen's D tells us the difference in means of firstborn babies weights and nonfirstborns weights is :", d,\
        "standard deviations.", "\n",\
          "Similar to the difference in pregnancy length (0.029), this may be slightly larger, but is still negligibly small."

    
def main(script):

    live, firsts, others = MakeFrames()
    WeightDiff(live, firsts, others)

if __name__ == '__main__':
    main(*sys.argv)
