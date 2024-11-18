'''
# FlowMate

A convenient Hamiltonian based phase portrait visualiser.
'''
import numpy as np
import matplotlib.pyplot as plt

def get_vector_field(X: callable, phase_space: list, args=[]):
    '''
    Returns the Hamiltonian Vector field from Hamiltons equations.

    Parameters:
        X (callable): Hamiltons equations as a funciton of phase space.

        phase_space (array_like): Numpy meshgrid of position and conjugate momenta coordinates.

        args (list, optional): The arguments to be put into ``X``.

    Returns:
        (position_derivatives, momentum_derivatives) (array_like): The Hamiltonian vector field calculated at each point.

    Examples:
    >>> import numpy as np
    >>> import FlowMate
    >>> def X(q,p,m,k):
    >>>     return p/m, -k*q
    >>> # define the phase space
    >>> q = np.linspace(-5, 5, 21)
    >>> p = np.linspace(-5, 5, 31)
    >>> PS = np.meshgrid(q, p)
    >>> # define constants
    >>> m = 2
    >>> k = 10
    >>> # evaluate Hamiltonian vector field
    >>> (dot_q, dot_p) = FlowMate.get_vector_field(X, PS, args=[m, k])
    >>> # plot
    >>> l = np.sqrt(dot_q**2 + dot_p**2)
    >>> plt.quiver(q,p,dot_q/l, dot_p/l,l, cmap=cmap, pivot='mid', angles='xy')
    >>> plt.show()
    '''
    (position, momentum) = phase_space
    if args == []:
        position_derivatives, momentum_derivatives = X(position, momentum)
    else:
        position_derivatives, momentum_derivatives = X(position, momentum, *args)
    return position_derivatives * np.ones_like(position), momentum_derivatives * np.ones_like(momentum)

def plot_phase_portrait(X: callable, phase_space: list, args=[], vec_field=False, save_fig=False, density=3.0, cmap='inferno_r', dpi=300.0, dark_mode=True):
    '''
    Creates phase portrait plot from Hamiltons equations.

    Parameters:
        X (callable): Hamiltons equations as a function of phase space.

        phase_space (array_like): Numpy meshgrid of position and conjugate momenta coordinates.

        args (list, optional): The arguments to be put into ``X``.

        vec_field (bool, default = ``False``): If true, plots the Hamiltonian vector field underneath the orbits.

        save_fig (bool, default = ``False``): If true, saves plot as a png image.
        
        density (float, default = ``3.0``): Number of streamlines in streamplot. See matplotlib documentation.

        cmap (str, default = ``'inferno_r'``): Colour map for streamlines and vector field. See matplotlib documentation.

        dpi (float, default = ``300.0``): Dots Per Inch (dpi) of png image if ``save_fig==True``.

        dark_mode (bool, default = ``True``): If ``True``, renders image with black background.

    Examples:
    >>> import numpy as np
    >>> import FlowMate
    >>> def X(q,p,m,k):
    >>>     return p/m, -k*q
    >>> # define the phase space
    >>> q = np.linspace(-5, 5, 21)
    >>> p = np.linspace(-5, 5, 31)
    >>> PS = np.meshgrid(q, p)
    >>> # define constants
    >>> m = 2
    >>> k = 10
    >>> # plot
    >>> FlowMate.plot_phase_portrait(X, PS, args=[m, k])
    '''
    if dark_mode:
        plt.rcParams['figure.facecolor'] = 'black'
    ax = plt.axes(aspect='equal')
    ax.set_axis_off()
    (position, momentum) = phase_space
    position_derivatives, momentum_derivatives = get_vector_field(X, phase_space, args=args)
    magnitude = np.sqrt(position_derivatives**2 + momentum_derivatives**2)
    ax.streamplot(position,momentum, position_derivatives, momentum_derivatives, cmap=cmap, density=density, linewidth=0.2, arrowstyle='-', color=magnitude, broken_streamlines=False)
    if vec_field:
        ax.quiver(position,momentum,position_derivatives/magnitude, momentum_derivatives/magnitude, magnitude, cmap=cmap, pivot='mid', angles='xy')
    if save_fig:
        plt.savefig("phase_portrait.png", dpi=dpi)
    plt.show()
