CRED = '\033[91m'
CEND = '\033[0m'

# Reference: https://www.cs.cmu.edu/~02710/Lectures/ScoringMatrices2015.pdf

import utils
import numpy as np
import save

def generate(X, seqType, args):
    '''
    # Reference: repRNA
    :param X:
    :param seqType:
    :param args:
    :return:
    '''

    if seqType == 'RNA':
        d = {
            'AA': [2.000, 0.000, -6.600,  -6.820,  -18.400, -19.000, -0.900, -0.930, 0.000, 0.000, 0.023, 0.040, 0.000, 2.000, 3.180, 7.000,  -0.080, -1.270, -13.700, 0.000, -0.800, 31.000],
            'AC': [1.000, 1.000, -10.200, -11.400, -26.200, -29.500, -2.100, -2.240, 1.000, 0.000, 0.083, 0.140, 0.000, 1.000, 3.240, 4.800,   0.230, -1.430, -13.800, 0.000,  0.800, 32.000],
            'AG': [1.000, 0.000, -7.600,  -10.480, -19.200, -27.100, -1.700, -2.080, 1.000, 1.000, 0.035, 0.080, 0.000, 2.000, 3.300, 8.500,  -0.040, -1.500, -14.000, 0.000,  0.500, 30.000],
            'AU': [1.000, 0.000, -5.700,  -9.380,  -15.500, -26.700, -0.900, -1.100, 0.000, 0.000, 0.090, 0.140, 1.000, 1.000, 3.240, 7.100,  -0.060, -1.360, -15.400, 1.000,  1.100, 33.000],
            'CA': [1.000, 1.000, -10.500, -10.440, -27.800, -26.900, -1.800, -2.110, 1.000, 0.000, 0.118, 0.210, 0.000, 1.000, 3.090, 9.900,   0.110, -1.460, -14.400, 0.000,  1.000, 31.000],
            'CC': [0.000, 2.000, -12.200, -13.390, -29.700, -32.700, -2.900, -3.260, 2.000, 0.000, 0.349, 0.490, 0.000, 0.000, 3.320, 8.700,  -0.010, -1.780, -11.100, 0.000,  0.300, 32.000],
            'CG': [0.000, 1.000, -8.000,  -10.640, -19.400, -26.700, -2.000, -2.360, 2.000, 1.000, 0.193, 0.350, 1.000, 1.000, 3.300, 12.100,  0.300, -1.890, -15.600, 0.000, -0.100, 27.000],
            'CU': [0.000, 1.000, -7.600,  -10.480, -19.200, -27.100, -1.700, -2.080, 1.000, 0.000, 0.378, 0.520, 1.000, 0.000, 3.300,  8.500, -0.040, -1.500, -14.000, 1.000,  0.500, 30.000],
            'GA': [1.000, 0.000, -13.300, -12.440, -35.500, -32.500, -2.300, -2.350, 1.000, 1.000, 0.048, 0.100, 1.000, 2.000, 3.380, 9.400,   0.070, -1.700, -14.200, 0.000,  1.300, 32.000],
            'GC': [0.000, 1.000, -14.200, -14.880, -34.900, -36.900, -3.400, -3.420, 2.000, 1.000, 0.146, 0.260, 1.000, 1.000, 3.220, 6.100,   0.070, -1.390, -16.900, 0.000,  0.000, 35.000],
            'GG': [0.000, 0.000, -12.200, -13.390, -29.700, -32.700, -2.900, -3.260, 2.000, 2.000, 0.065, 0.170, 2.000, 2.000, 3.320, 12.100, -0.010, -1.780, -11.100, 0.000,  0.300, 32.000],
            'GU': [0.000, 0.000, -10.200, -11.400, -26.200, -29.500, -2.100, -2.240, 1.000, 1.000, 0.160, 0.270, 2.000, 1.000, 3.240, 4.800,   0.230, -1.430, -13.800, 1.000,  0.800, 32.000],
            'UA': [1.000, 0.000, -8.100,  -7.690,  -22.600, -20.500, -1.100, -1.330, 0.000, 0.000, 0.112, 0.210, 1.000, 1.000, 3.260, 10.700, -0.020, -1.450, -16.000, 1.000, -0.200, 32.000],
            'UC': [0.000, 1.000, -10.200, -12.440, -26.200, -32.500, -2.100, -2.350, 1.000, 0.000, 0.359, 0.480, 1.000, 0.000, 3.380, 9.400,   0.070, -1.700, -14.200, 1.000,  1.300, 32.000],
            'UG': [0.000, 0.000, -7.600,  -10.440, -19.200, -26.900, -1.700, -2.110, 1.000, 1.000, 0.224, 0.340, 1.000, 1.000, 3.090, 9.900,   0.110, -1.460, -14.400, 1.000,  1.000, 31.000],
            'UU': [0.000, 0.000, -6.600,  -6.820,  -18.400, -19.000, -0.900, -0.930, 0.000, 0.000, 0.389, 0.440, 2.000, 0.000, 3.180, 7.000,  -0.080, -1.270, -13.700, 2.000, -0.800, 31.000],
            'p':  [    0,     0,      0,       0,        0,       0,      0,      0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,       0,      0,       0,     0,      0,      0],  # padding
        }
    else:
        if seqType == 'PROT' or seqType == 'DNA':
            print(CRED + 'Error: The \'Physicochemical Properties-R1\' feature is NOT applicable for PROT and DNA.' + CEND)
            return None
        else: None
    #end-if

    # print(X)

    X = utils.processDi(X, d, args)
    # print(X.shape)

    totalFeature = 0
    if seqType == 'RNA':
        totalFeature = 22
    else:
        if seqType == 'PROT' or seqType == 'DNA': None
        else:
            None
    # end-if

    save.datasetSave(X, totalFeature, 'pcpR1')
#end-def