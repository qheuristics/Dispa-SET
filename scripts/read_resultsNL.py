

# -*- coding: utf-8 -*-
"""
Minimalist example file showing how to read the results of a Dispa-SET run

@author: Sylvain Quoilin
"""
# Change directory to the root folder of Dispa-SET:
# Import Dispa-SET
#%matplotlib inline
from __future__ import division
import sys
sys.path.append("..")  

import DispaSET as ds
import pandas as pd
import numpy as np

path = 'C:\Users\Maric003\gilles\Dispa-SET_test\Simulations\simulationNL'

# Load the inputs and the results of the simulation
inputs,results = ds.get_sim_results(path=path,cache=True)

#Format the inputs as a dictionary of dataframes:
datain = ds.ds_to_df(inputs)

rng = pd.DatetimeIndex(start='2015-01-02 00:00:00',end='2015-12-10 00:00:00',freq='h')

Nzones = len(inputs['sets']['n'])
c = inputs['sets']['n'][np.random.randint(Nzones)]
print('Randomly selected zone for the detailed analysis: '+ c)

# Generate plots
ds.plot_country(inputs,results,c,rng=rng)

r = ds.get_result_analysis(inputs,results)

results['ShadowPrice'].plot()

if 'OutputStorageLevel' in results:
   results['OutputStorageLevel'].plot()

#PPindicators = ds.get_indicators_powerplant(inputs,results)
#ax = ds.plot_energy_country_fuel(datain,results,PPindicators)    


#
#inputs['units'].groupby(['Fuel']).sum()['PowerCapacity']
#
#inputs['units']

