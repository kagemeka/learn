from kagemeka.gen import (
  PathManager as PM,
  PklIF,
)


cfd = PM.cfd(__file__)



import pandas as pd 


a = pd.DataFrame(
  data=[
    [1, 2],
    [2, 3],
  ],
  columns=['a', 'b'],
)



b = {
  'a': 2,
  'b': 4,
}

b = pd.Series(b)

a = pd.DataFrame()
a = a.append(
  b, 
  ignore_index=1,
)



b = b.append(b, ignore_index=1)
print(b)
print(a)