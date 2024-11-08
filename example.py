'''
Onion
'''
import FlowMate
import numpy as np

# define a function which returns dq/dt, dp/dt from Hamiltons equations
def X(q,p,k):
    return q*p, -k

# define the phase space
q = np.linspace(-5, 5, 21)
p = np.linspace(-5, 5, 31)
PS = np.meshgrid(q, p)

# plot
FlowMate.plot_phase_portrait(X, PS, args=[3])


