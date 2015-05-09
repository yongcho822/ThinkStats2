import chap01soln
import thinkstats2
import thinkplot

resp = chap01soln.ReadFemResp()
pmf = thinkstats2.Pmf(resp.numkdhh, label = 'actual')

# thinkplot.PrePlot(1)
# thinkplot.Pmfs([pmf])
# thinkplot.Show(xlabel = "number of kids under 18", ylabel = "PMF")

def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label = label)
    for x,p in pmf.Items():
        new_pmf.Mult(x, x)
    new_pmf.Normalize()
    return new_pmf

biased_pmf = BiasPmf(pmf, label = 'biased')

meanactual = pmf.Mean()
meanbiased = biased_pmf.Mean()

print("mean actual children under 18 count is", meanactual, '\n'+"mean perceived/biased children under 18 count is", meanbiased)
#for some reason, this doesn't print if you display the charts first, then try to print.

thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased_pmf])
thinkplot.Show(xlabel = "number of kids under 18", ylabel = "PMF")

