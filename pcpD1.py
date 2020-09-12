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

    if seqType == 'DNA':
        d = {
            'AA': [-5.37,2.9,35.5,0,0.97,-18.66,-1.2,1.9,66.51,35,35.1,3.9,0.96,1.9,9.1,24,11.4,3.9,7.9,0.97,16.3,1.14,1.02,8.4,23.6,7.6,54.5,5.37,1.2,8,21.9,26,0.026,0.038,0.02,1.69,2.26,7.65,-12,3.07,1.76,-1.43,12.15,9.12,3.98,3.38,5.3,9.03,2.98,2.94,35,54.5,1.18,1.04,-17.3,0.64,-8,-0.67,0.046,0.039,0.024,0.006,0.008,0.003,1.975,2.914,7.621,0.171,0.192,1.382,0.057,-0.218,-0.159,0.002,-0.008,-0.205,0.016,-0.022,-0.054,2.26,1.69,0.02,7.65,0.038,0.026,7.2,-154,13.72,5.35,-21.3,],
            'AC': [-10.51,2.3,33.1,1,0.13,-13.1,-1.5,1.3,108.8,60,31.5,4.6,4.52,1.3,6.5,17.3,19.8,1.3,5.4,0.13,5.4,2.47,1.43,8.6,23,14.6,97.73,10.51,1.5,9.4,25.5,34,0.036,0.038,0.023,1.32,3.03,8.93,-11.8,2.97,2,-0.11,12.37,9.41,3.98,3.03,6.04,8.79,3.26,4.22,60,97.73,1.06,1.1,-6.7,0.95,-9.4,-1.28,0.049,0.041,0.027,0.001,0.008,0.003,1.341,2.974,9.882,-0.157,-0.006,2.593,0.005,-0.201,-0.16,-0.005,-0.013,0.044,0.014,-0.002,0.109,3.03,1.32,0.023,8.93,0.038,0.036,1.1,143,9.57,9.73,-22.4,],
            'AG': [-6.78,2.1,30.6,1,0.33,-14,-1.5,1.6,85.12,60,31.9,3.4,0.79,1.6,7.8,20.8,19.8,3.4,6.7,0.33,14.2,2.47,1.16,6.1,16.1,8.2,58.42,6.78,1.5,6.6,16.4,34,0.031,0.037,0.019,1.46,2.03,7.08,-11.5,2.31,0.9,-0.92,13.51,8.96,4.7,3.36,5.19,8.98,3.98,2.79,60,58.42,1.06,1.09,-14.3,2.53,-6.6,-1.17,0.044,0.037,0.023,-0.003,0.006,-0.003,1.657,2.706,6.388,-0.026,-0.032,1.32,-0.031,-0.176,-0.144,-0.019,0.008,0.05,-0.014,-0.029,-0.001,2.03,1.46,0.019,7.08,0.037,0.031,8.4,2,7.58,8.98,-21,],
            'AT': [-6.57,1.6,43.2,0,0.58,-15.01,-0.9,0.9,72.29,20,29.3,5.9,6.82,1.5,8.6,23.9,11.4,2.4,6.3,0.58,10,1.14,0.73,6.5,18.8,25,57.02,6.57,0.9,5.6,15.2,26,0.033,0.036,0.022,1.03,3.83,9.07,-10.6,2.6,1.87,0,12.87,8.96,4.7,3.02,5.31,8.91,3.26,4.2,20,57.02,1.12,1.02,-16.9,1.68,-5.6,-0.62,0.046,0.04,0.027,0,0.008,0.001,1.193,3.31,10.499,-0.097,-0.023,2.481,-0.008,-0.116,-0.089,0.024,-0.01,0.006,0.009,-0.05,0.093,3.83,1.03,0.022,9.07,0.036,0.033,2.6,0,11.69,1.13,-20.4,],
            'CA': [-6.57,9.8,37.7,1,1.04,-9.45,-1.7,1.9,64.92,60,37.3,1.3,5.1,1.9,5.8,12.9,19.8,4.6,7.9,1.04,19.2,2.47,1.38,7.4,19.3,10.9,72.55,6.57,1.7,8.2,21,34,0.016,0.025,0.017,1.07,1.78,6.38,-12.3,3.58,-1.64,1.31,13.58,8.67,3.98,3.79,4.79,9.09,3.7,3.09,60,54.71,1.06,1.16,-8.6,0.8,-8.2,-1.19,0.021,0.028,0.018,-0.001,0.005,0.001,1.6,2.286,6.29,-0.283,-0.065,0.816,-0.01,-0.017,-0.126,0.004,-0.002,-0.016,-0.002,0.009,-0.087,1.78,1.07,0.017,6.38,0.025,0.016,3.5,-64,1.35,4.61,-22.7,],
            'CC': [-8.26,6.1,35.3,2,0.19,-8.11,-2.3,3.1,99.31,130,32.9,2.4,2.26,3.1,11,26.6,28.2,2.4,13,0.19,10,3.8,1.77,6.7,15.6,7.2,54.71,8.26,2.1,10.9,28.4,42,0.026,0.042,0.019,1.43,1.65,8.04,-9.5,2.16,0.71,-1.11,15.49,8.45,3.98,3.38,4.62,8.99,3.98,2.8,130,85.97,0.99,1.27,-12.8,1.78,-10.9,-1.55,0.048,0.041,0.024,0,0.004,-0.001,1.984,3.215,7.335,0.057,0.215,1.196,0.024,-0.225,-0.114,-0.065,0.005,-0.084,-0.004,-0.007,0.004,1.65,1.43,0.019,8.04,0.042,0.026,2.1,-57,7.36,5.51,-19.9,],
            'CG': [-9.61,12.1,31.3,2,0.52,-10.03,-2.8,3.6,88.84,85,36.1,0.7,10.79,3.6,11.9,27.8,28.2,4,15.1,0.52,16.7,3.8,2.09,10.1,25.5,8.9,54.71,9.69,2.8,11.8,29,42,0.014,0.026,0.016,1.08,2,6.23,-13.1,2.81,0.22,0,14.42,8.81,4.7,3.77,5.16,9.06,4.7,3.21,85,72.55,1.02,1.25,-11.2,2.42,-11.8,-1.87,0.023,0.028,0.015,0.001,0.003,0.001,1.346,2.034,4.39,-0.187,-0.041,1.467,0.023,-0.086,-0.124,-0.052,0.01,0.005,0.011,-0.021,-0.02,2,1.08,0.016,6.23,0.026,0.014,6.7,0,4.02,12.13,-27.2,],
            'CT': [-6.78,2.1,30.6,1,0.33,-14,-1.5,1.6,85.12,60,31.9,3.4,0.79,1.6,7.8,20.8,19.8,3.4,6.7,0.33,14.2,2.47,1.16,6.1,16.1,8.2,85.97,6.78,1.5,6.6,16.4,34,0.031,0.037,0.019,1.46,2.03,7.08,-11.5,2.31,0.9,0.92,13.51,8.96,4.7,3.36,5.19,8.98,3.98,2.79,60,58.42,1.04,1.16,-14.3,2.53,-6.6,-1.17,0.044,0.037,0.023,-0.003,0.006,-0.003,1.657,2.706,6.388,-0.026,-0.032,1.32,-0.031,-0.176,-0.144,-0.019,0.008,0.05,-0.014,-0.029,-0.001,2.03,1.46,0.019,7.08,0.037,0.031,8.4,-2,7.58,8.98,-21,],
            'GA': [-9.81,4.5,39.6,1,0.98,-13.48,-1.5,1.6,80.03,60,36.3,3.4,3.18,1.6,5.6,13.5,19.8,2.5,6.7,0.98,10.5,2.47,1.46,7.7,20.3,8.8,86.44,9.81,1.5,8.8,23.5,34,0.025,0.038,0.02,1.32,1.93,8.56,-11.4,2.51,1.35,-0.33,13.93,8.76,3.26,3.4,4.71,9.11,2.98,2.95,60,86.44,1.08,1.12,-15.1,0.03,-8.8,-1.12,0.042,0.039,0.021,0.001,0.009,0,1.43,2.518,8.33,0.026,0.025,1.153,-0.001,-0.206,-0.128,-0.026,-0.002,-0.083,0.011,-0.001,-0.012,1.93,1.32,0.02,8.56,0.038,0.025,5.3,120,10.28,5.44,-22.2,],
            'GC': [-14.59,4,38.4,2,0.73,-11.08,-2.3,3.1,135.83,85,33.6,4,8.28,3.1,11.1,26.7,28.2,0.7,13,0.73,2.9,3.8,2.28,11.1,28.4,11.1,136.12,14.59,2.3,10.5,26.4,42,0.025,0.036,0.026,1.2,2.61,9.53,-13.2,3.06,2.5,0,14.55,8.67,3.26,3.04,4.74,8.98,3.26,4.24,85,136.12,0.98,1.17,-11.7,0.22,-10.5,-1.85,0.042,0.04,0.028,0,0.007,-0.001,1.761,2.708,10.281,0.318,0.131,2.558,-0.001,-0.193,-0.16,-0.048,-0.018,-0.063,-0.002,0.006,0.126,2.61,1.2,0.026,9.53,0.036,0.025,5,180,4.34,1.98,-24.4,],
            'GG': [-8.26,6.1,35.3,2,0.19,-8.11,-2.3,3.1,99.31,130,32.9,2.4,2.26,3.1,11,26.6,28.2,2.4,13,0.19,10,3.8,1.77,6.7,15.6,7.2,85.97,8.26,2.1,10.9,28.4,42,0.026,0.042,0.019,1.43,1.65,8.04,-9.5,2.16,0.71,1.11,15.49,8.45,3.98,3.38,4.62,8.99,3.98,2.8,130,85.97,1,1.25,-12.8,1.78,-10.9,-1.55,0.048,0.041,0.024,0,0.004,-0.001,1.984,3.215,7.335,0.057,0.215,1.196,0.024,-0.225,-0.114,-0.065,0.005,-0.084,-0.004,-0.007,0.004,1.65,1.43,0.019,8.04,0.042,0.026,2.1,57,7.36,5.51,-19.9,],
            'GT': [-10.51,2.3,33.1,1,0.13,-13.1,-1.5,1.3,108.8,60,31.5,4.6,4.52,1.3,6.5,17.3,19.8,1.3,5.4,0.13,5.4,2.47,1.43,8.6,23,14.6,97.73,10.51,1.5,9.4,25.5,34,0.036,0.038,0.023,1.32,3.03,8.93,-11.8,2.97,2,0.11,12.37,9.41,3.98,3.03,6.04,8.79,3.26,4.22,60,97.73,1.02,1.11,-6.7,0.95,-9.4,-1.28,0.049,0.041,0.027,0.001,0.008,0.003,1.341,2.974,9.882,-0.157,-0.006,2.593,0.005,-0.201,-0.16,-0.005,-0.013,0.044,0.014,-0.002,0.109,3.03,1.32,0.023,8.93,0.038,0.036,1.1,-143,9.57,9.73,-22.4,],
            'TA': [-3.82,6.3,31.6,0,0.73,-11.85,-0.9,1.5,50.11,20,37.8,2.5,0.42,0.9,6,16.9,11.4,5.9,3.8,0.73,24.7,1.14,0.6,6.3,18.5,12.5,36.73,3.82,0.9,6.6,18.4,26,0.017,0.018,0.016,0.72,1.2,6.23,-11.2,6.74,6.7,0,12.32,9.6,3.26,3.81,6.4,9,2.7,2.97,20,36.73,1.07,1.05,-11.1,0,-6.6,-0.7,0.036,0.025,0.014,-0.001,0.008,0,1.529,2.269,5.055,0.052,-0.033,0.913,-0.006,-0.093,-0.093,0.023,0.005,-0.003,-0.01,-0.008,-0.037,1.2,0.72,0.016,6.23,0.018,0.017,0.9,0,7.13,4.28,-21.3,],
            'TC': [-9.81,4.5,39.6,1,0.98,-13.48,-1.5,1.6,80.03,60,36.3,3.4,3.18,1.6,5.6,13.5,19.8,2.5,6.7,0.98,10.5,2.47,1.46,7.7,20.3,8.8,86.44,9.81,1.5,8.8,23.5,34,0.025,0.038,0.02,1.32,1.93,8.56,-11.4,2.51,1.35,0.33,13.93,8.76,3.26,3.4,4.71,9.11,2.98,2.95,60,86.44,1.03,1.2,-15.1,0.03,-8.8,-1.12,0.042,0.039,0.021,0.001,0.009,0,1.43,2.518,8.33,0.026,0.025,1.153,-0.001,-0.206,-0.128,-0.026,-0.002,-0.083,0.011,-0.001,-0.012,1.93,1.32,0.02,8.56,0.038,0.025,5.3,-120,10.28,5.44,-22.2,],
            'TG': [-6.57,9.8,37.7,1,1.04,-9.45,-1.7,1.9,64.92,60,37.3,1.3,5.1,1.9,5.8,12.9,19.8,4.6,7.9,1.04,19.2,2.47,1.38,7.4,19.3,10.9,58.42,6.57,1.7,8.2,21,34,0.016,0.025,0.017,1.07,1.78,6.38,-12.3,3.58,-1.64,-1.31,13.58,8.67,3.98,3.79,4.79,9.09,3.7,3.09,60,54.71,1.03,1.23,-8.6,0.8,-8.2,-1.19,0.021,0.028,0.018,-0.001,0.005,0.001,1.6,2.286,6.29,-0.283,-0.065,0.816,-0.01,-0.017,-0.126,0.004,-0.002,-0.016,-0.002,0.009,-0.087,1.78,1.07,0.017,6.38,0.025,0.016,3.5,64,1.35,4.61,-22.7,],
            'TT': [-5.37,2.9,35.5,0,0.97,-18.66,-1.2,1.9,66.51,35,35.1,3.9,0.96,1.9,9.1,24,11.4,3.9,7.9,0.97,16.3,1.14,1.02,8.4,23.6,7.6,54.5,5.37,1.2,8,21.9,26,0.026,0.038,0.02,1.69,2.26,7.65,-12,3.07,1.76,1.43,12.15,9.12,3.98,3.38,5.3,9.03,2.98,2.94,35,54.5,1.09,1.04,-17.3,0.64,-8,-0.67,0.046,0.039,0.024,0.006,0.008,0.003,1.975,2.914,7.621,0.171,0.192,1.382,0.057,-0.218,-0.159,0.002,-0.008,-0.205,0.016,-0.022,-0.054,2.26,1.69,0.02,7.65,0.038,0.026,7.2,154,13.72,5.35,-21.3,],
            'p':  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],  # padding

        }
    else:
        if seqType == 'PROT' or seqType == 'RNA':
            print(CRED + 'Error: The \'Physicochemical Properties-D1\' feature is NOT applicable for PROT and RNA.' + CEND)
            return None
        else: None
    #end-if

    # print(X)

    X = utils.processDi(X, d, args)
    # print(X.shape)

    totalFeature = 0
    if seqType == 'DNA':
        totalFeature = 90
    else:
        if seqType == 'PROT' or seqType == 'RNA': None
        else:
            None
    # end-if

    save.datasetSave(X, totalFeature, 'pcpD1')
#end-def