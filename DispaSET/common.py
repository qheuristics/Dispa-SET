# -*- coding: utf-8 -*-
"""
This file defines the global variables to be used in Dispa-SET such as fluids, technologies, etc.

@author: 'Sylvain Quoilin'
"""
import itertools

def commonvars():
    '''
    Function providing a dictionary with the common variable definitions
    to be used in Dispa-SET
    '''
    commons={}
    # Timestep
    commons['TimeStep'] = '1h'

    # DispaSET technologies:
    commons['Technologies'] = ['COMC', 'GTUR', 'HDAM', 'HROR', 'HPHS', 'ICEN', 'PHOT', 'STUR', 'WTOF', 'WTON', 'CAES', 'BATS',
<<<<<<< Updated upstream
                    'BEVS', 'THMS', 'P2GS','HP','GEO','STH','BOIL']
=======
                    'BEVS', 'THMS', 'P2GS','HP','PHP','GEO','STH','BOIL']
>>>>>>> Stashed changes
    # List of renewable technologies:
    commons['tech_renewables'] = ['WTON', 'WTOF', 'PHOT', 'HROR']
    # List of storage technologies:
    commons['tech_storage'] = ['HDAM', 'HPHS', 'BATS', 'BEVS', 'CAES', 'THMS']
    ############
    # List of CHP types:
<<<<<<< Updated upstream
    commons['types_CHP'] = ['extraction','back-pressure']
    # List of heat generation:
    commons['types_HEAT'] = ['chp','hp','geo','solarth','biomass']
=======
    commons['types_CHP'] = ['extraction','back-pressure','p2h']
    # List of heat pumps:
    commons['HP_model'] = ['HP1','HP2','HP3']
    # List of heat generation type:
    commons['DH_gen'] = ['HP','CHP','Boiler']
>>>>>>> Stashed changes
    #############
    # DispaSET fuels:
    commons['Fuels'] = ['BIO', 'GAS', 'HRD', 'LIG', 'NUC', 'OIL', 'PEA', 'SUN', 'WAT', 'WIN', 'WST', 'OTH','ELEC','Geothermal','SUN']
    # Ordered list of fuels for plotting (the first ones are negative):
    commons['MeritOrder'] = ['Storage','FlowOut','NUC', 'SUN', 'WIN', 'LIG', 'HRD', 'BIO', 'GAS', 'OIL', 'PEA', 'WST', 'FlowIn', 'WAT']
    # Colors associated with each fuel:
    commons['colors'] = {'NUC': 'orange', 'LIG': 'brown', 'HRD': 'grey', 'BIO': 'darkgreen', 'GAS': 'red', 
           'OIL': 'chocolate','PEA':'green', 'WST': 'dodgerblue', 'SUN': 'yellow', 'WIN': 'lightblue', 'FlowIn': 'lightgreen', 'WAT': 'blue', 
           'Storage': 'blue','FlowOut': 'lightgreen'}
    commons['colorsDH'] = {'HP':'blue','CHP':'red','Boiler':'orange','Reservoir out':'green'}
    # Hatches associated with each fuel (random):
    hatches = itertools.cycle(['x', '//', '\\', '/'])
    commons['hatches'] = {}
    for x in commons['colors']:
        commons['hatches'][x] = next(hatches)
        
    return commons