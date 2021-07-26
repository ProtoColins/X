import numpy as np
import pandas as pd
import matplotlib.pyplot as mplt

dtb_path = r"Dummies\pydata-book-2nd-edition\datasets\bitly_usagov\example.txt"

#--------------------tz challenge-------------------
#find most freq- tz:


DT = pd.read_json(dtb_path,lines=True)
tz_pile = DT['tz']
tz_pile.fillna('Datalost')
tz_pile[tz_pile == ''] = 'Unknown'
tz_count = tz_pile.value_counts()

import seaborn

seaborn.barplot(y= tz_count.index , x=tz_count.values)
mplt.show()

#---------------------'headers'-------------

print()
