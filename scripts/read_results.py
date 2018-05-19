# -*- coding: utf-8 -*-
"""
Minimalist example file showing how to read the results of a Dispa-SET run

@author: Sylvain Quoilin
"""

# Change directory to the root folder of Dispa-SET:
from __future__ import division
import sys
sys.path.append("..")  

import DispaSET as ds
import pandas as pd
import numpy as np

#path = 'C:\Users\Gilles\Dropbox\Dispa-SET_actuel\Simulations\simulationNL'
path = 'C:\Users\Maric003\Dropbox\Dispa-SET_actuel\Simulations\simulationNL'
#path = 'C:\Users\Maric003\Dropbox\Dispa-SET-master\Simulations\simulationCY'

# Load the inputs and the results of the simulation
inputs,results = ds.get_sim_results(path,cache=True)

#Format the inputs as a dictionary of dataframes:
datain = ds.ds_to_df(inputs)

rng = pd.DatetimeIndex(start='2015-01-01 00:00:00',end='2015-1-08 00:00:00',freq='h')

Nzones = len(inputs['sets']['n'])
c = inputs['sets']['n'][np.random.randint(Nzones)]
print('Randomly selected zone for the detailed analysis: '+ c)

# Generate plots
ds.plot_country(inputs,results,c,rng=rng)
ds.plot_dispatch_heat(inputs,results,path,rng=rng,Country=False)

# Bar plot with the installed capacities in all countries:
#cap = ds.plot_country_capacities(inputs)
#a=ds.plot_country_capacitiesDH(inputs)
ds.plot_CHP(inputs,results,path,rng=rng) 

# Bar plot with the energy balances in all countries:
#ds.plot_energy_country_fuel(inputs,results,ds.get_indicators_powerplant(inputs,results))
#ds.plot_heat_balanceDH(inputs,results)
# Analyse the results for each country and provide quantitative indicators:
r = ds.get_result_analysis(inputs,results)






