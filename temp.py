from astropy.io import fits as fit
import numpy as np
from scipy.optimize import curve_fit as cfit
import scipy.constants as s
import matplotlib.pyplot as plt
from scipy.signal import find_peaks as fp
k = input("Enter the name of file:\n")
k = k+".fits"
dat = fit.open(k)
dat = dat[0].data
wvl=np.arange(1150,25001,5)
l=wvl*10**-10
def B(l,T,n):
    t=(n*2*s.h*s.c**2)/((l**5)*(np.exp((s.h*s.c)/(l*s.k*T))-1))
    return t
plt.plot(wvl,dat)
plt.show()
inp = input("Where to cut:\n")
if inp=='max':
    cut = np.argmax(dat)
else:
    cut=wvl.tolist().index(int(inp))

cut=int(cut)
spec=wvl.tolist().index(3500)
val, var = cfit(B,l[cut:],dat[cut:],p0=[1000,1])
peaks,_=fp((B(l,val[0],val[1])-dat), height=0,prominence=0.05)
wvlpk = (peaks*5+1150)
specpk=[]
for i in range(len(peaks)):
    if wvlpk[i]>6550 and wvlpk[i]<6650:
        specpk.append(wvlpk[i])
    elif wvlpk[i]>4750 and wvlpk[i]<4850:
        specpk.append(wvlpk[i])
    elif wvlpk[i]>4300 and wvlpk[i]<4400:
        specpk.append(wvlpk[i])
specpk=(np.array(specpk)+(-1150))/5
wvlpk=np.array(specpk).astype(int)
plt.plot((peaks*5+1150),dat[peaks],"x")
plt.plot((wvlpk*5+1150),dat[wvlpk],"o")
plt.plot(wvl,B(l,val[0],val[1])-dat)
plt.plot(wvl,dat)
plt.title(val[0])
plt.plot(wvl,B(l,val[0],val[1]))
plt.show()
