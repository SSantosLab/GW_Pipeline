import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

outs = ['/pnfs/des/persistent/gw/exp/20151227/506432/506432.out','/pnfs/des/persistent/gw/exp/20170701/658115/658115.out']
            
for o in outs:
    odf = pd.read_table(o,delim_whitespace=True,header=None,names=['expnum','band','ccd','ra1','dec1','ra2','dec2','ra3','dec3','ra4','dec4'])

    odf = odf.drop_duplicates()
    odf = odf.reset_index(drop=True)

    odf.ix[odf.ra1 > 270., 'ra1'] = odf.ix[odf.ra1 > 270., 'ra1'] - 360.
    odf.ix[odf.ra2 > 270., 'ra2'] = odf.ix[odf.ra2 > 270., 'ra2'] - 360.
    odf.ix[odf.ra3 > 270., 'ra3'] = odf.ix[odf.ra3 > 270., 'ra3'] - 360.
    odf.ix[odf.ra4 > 270., 'ra4'] = odf.ix[odf.ra4 > 270., 'ra4'] - 360.

    ras = np.concatenate((odf['ra1'].tolist(),odf['ra2'].tolist(),odf['ra3'].tolist(),odf['ra4'].tolist()),axis=0)

    decs = np.concatenate((odf['dec1'].tolist(),odf['dec2'].tolist(),odf['dec3'].tolist(),odf['dec4'].tolist()),axis=0)

    for i in range(len(odf)):
        ra = odf.ix[i,['ra1','ra2','ra3','ra4']]
        dec = odf.ix[i,['dec1','dec2','dec3','dec4']]
        chip = str(odf.ix[i,'ccd'])
        midra = (max(ra)+min(ra))/2.
        middec = (max(dec)+min(dec))/2.
        middle = tuple([midra,middec])
        cs = zip(ra,dec)
        cent=(sum([c[0] for c in cs])/len(cs),sum([c[1] for c in cs])/len(cs))
        cs.sort(key=lambda c: math.atan2(c[1]-cent[1],c[0]-cent[0]))
        cs.append(cs[0])
        if '115' in o:
            plt.scatter([c[0] for c in cs],[c[1] for c in cs],marker='.',s=5,c='k')
        else:
            plt.scatter([c[0] for c in cs],[c[1] for c in cs],marker='*',s=5,c='b')
        plt.annotate(chip, xy=middle, ha='center',va='center',family='sans-serif',fontsize=12,alpha=0.3)

    plt.xlim(min(ras)-0.2,max(ras)+0.2)
    plt.ylim(min(decs)-0.2,max(decs)+0.2)

plt.show()
