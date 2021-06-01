from dataclasses import (
  dataclass,
  field,
)
from typing import DefaultDict

from typing import (
  List,
)

import tensorflow as tf 



import numpy as np 

@dataclass
class Edge:
  from_: int 
  to: int



@dataclass
class Node:
  edges: List[Edge] = field(
    default_factory=list,
  )



def main():
  a: list[str] = None
  print(tf.__version__)
  print(
    tf.config.list_physical_devices('GPU'))

if __name__ == '__main__':
  main()
  