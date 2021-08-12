# Example of assimilating observation with different H

from simdkalman import KalmanFilter
import numpy as np 

# Prior state means 
m0 = np.zeros((2,3,1))
m0[0,:,:] = np.array([[1.5, 1.5, 1.5]]).transpose()
m0[1,:,:] = np.array([[1.5, 1.5, 1.5]]).transpose()

# Prior covariances
P0 = np.zeros((2, 3, 3))
P0[0, :, :] = np.eye(3)
P0[1, :, :] = 0.5 * np.eye(3)

# Observations
y_update = np.zeros((2, 1, 1))
y_update[0, :, :] = np.array([[-1.4]])
y_update[1, :, :] = np.array([[-0.33]])

# Measurement var
R = np.zeros((2, 1, 1))
R[0, :, :] = np.eye(1)
R[1, :, :] = 0.66*np.eye(1)

# Observation equations 
H0 = np.array([[0.8, 0.2, 0]])
H1 = np.array([[0.9, 0.1, 0]])
H0.shape = (1, 3)
H1.shape = (1, 3)
H = np.zeros((2, 1, 3))
H[0, :, :] = H0
H[1, :, :] = H1

# Transition, process noise
# This example only illustrates the update step, not evolution in time
# However we need to instantiate the KF
A = np.array([[0.5, 0.3, 0.2], [1, 0, 0], [0, 1, 0]])
Q = np.zeros((2,3,3))
Q[0,:,:] = np.eye(3)
Q[1,:,:] = np.eye(3)


kf = KalmanFilter(
    state_transition=A,  # A
    process_noise=Q,  # Q
    observation_model=H,  # H
    observation_noise=R)  # R
m1, P1, K, ll = kf.update(m0,P0,y_update, log_likelihood=True)
print(m1)



