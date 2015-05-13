from __future__ import division
from thinkbayes import Pmf

class Bowl():

    def __init__(self, mixes, name):
        self.Count = dict(mixes)
        total = sum(self.Count.values())
        self.Ratios = {i: self.Count[i]/total for i in self.Count.keys()}
        self.name = name

class Cookie(Pmf):

    def __init__(self, hypos):
        Pmf.__init__(self)
        for hypo in hypos:
            self.Set(hypo, 1)
        self.Normalize()

    def Update(self, data):
        for hypo in self.Values():
            like = self.Likelihood(data, hypo)
            self.Mult(hypo, like)
        self.Normalize()

    def Likelihood(self, data, hypo):

        like = hypo.Ratios[data]
        if like:
            hypo.Count[data] -= 1
        return like

def main():
    bowl1 = Bowl({'vanilla':30, 'chocolate':10}, "Bowl 1")
    bowl2 = Bowl({'vanilla':20, 'chocolate':20}, "Bowl 2")

    pmf = Cookie([bowl1, bowl2])

    print 'After 1 vanilla:'
    pmf.Update('vanilla')
    for hypo, prob in pmf.Items():
        print hypo.name, prob

    print '\nAfter 1 vanilla, 1 vanilla:'
    pmf.Update('vanilla')
    for hypo, prob in pmf.Items():
        print hypo.name, prob

main()