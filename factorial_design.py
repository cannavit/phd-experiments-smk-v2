import pandas as pd
import numpy as np
from numpy.random import rand


inputs_labels = {'x1' : 'Length of specimen (mm)',
                 'x2' : 'Amplitude of load cycle (mm)',
                 'x3' : 'Load (g)'}

dat = [('x1',250,350),
       ('x2',8,10),
       ('x3',40,50)]

inputs_df = pd.DataFrame(dat,columns=['index','low','high'])
inputs_df = inputs_df.set_index(['index'])
inputs_df['label'] = inputs_df.index.map( lambda z : inputs_labels[z] )

inputs_df

