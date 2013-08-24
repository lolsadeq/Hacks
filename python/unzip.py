
# Unzip all compressed archives in a directory

import zipfile
import os

d = r'C:\ted'
dl = os.listdir(d)

def unzipme(x):
    f = os.path.join(d, x)
    zf = zipfile.ZipFile(f)

    print 'Unzipping %s to .\\' % f,

    for i, fn in enumerate(zf.namelist()):
        of = open(os.path.join(d, fn), 'wb')
        print '%s ...' % fn,
        of.write(zf.read(fn))
        of.flush()
        of.close()

    print 'Done!'
    
    
map(unzipme, dl)


