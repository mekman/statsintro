'''Simple linear models.
- "model_formulas" is based on examples in Kaplan "Statistical Modeling".
- "polynomial_regression" shows how to work with simple design matrices, like MATLAB's "regress" command.

'''

'''
Author: Thomas Haslwanter
Date:   Jan-2013
Ver:    2.0
'''

from pandas import read_csv
from statsmodels.formula.api import ols
import statsmodels.regression.linear_model as sm
from statsmodels.stats.anova import anova_lm
import numpy as np

def model_formulas():
    ''' Define models through formulas '''
    # Get the dta
    data = read_csv(r'.\data_kaplan\swim100m.csv')
    
    # Different models
    model1 = ols("time ~ sex", data).fit()  # one factor
    model2 = ols("time ~ sex + year", data).fit()   # two factors
    model3 = ols("time ~ sex * year", data).fit()   # two factors with interaction
    
    # Model information
    print model1.summary()
    print model2.summary()
    print model3.summary()
    
    # ANOVAs
    print '-----------------------------------------------------------------'
    print anova_lm(model1)
    print '-----------------------------------------------------------------'
    print anova_lm(model2)
    print '-----------------------------------------------------------------'
    print anova_lm(model3)
    
def polynomial_regression():
    ''' Define the model directly through the design matrix. Similar to MATLAB's "regress" command '''

    # Generate the data
    t = np.arange(0,10,0.1)
    y = 4 + 3*t + 2*t**2 + 5*np.random.randn(len(t))
    
    # Make the fit. Note that this is another "OLS" than the one in "model_formulas"!
    M = np.column_stack((np.ones(len(t)), t, t**2))
    res = sm.OLS(y, M).fit()
        
    # Display the results
    print 'Summary:'
    print res.summary()
    print 'The fit parameters are: {0}'.format(str(res.params))
    print 'The confidence intervals are:'
    print res.conf_int()

if __name__ == '__main__':
    model_formulas()
    polynomial_regression()