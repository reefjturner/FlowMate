# FlowMate
A convenient Hamiltonian based phase portrait visualiser.

![Particular phase portrait made from FlowMate](/images/onion_plot.png)

## Usage

Given some Hamiltonian $H$, we get through Hamiltons equations:

$$\dot q = \frac{\partial H}{\partial p}\quad \dot p = -\frac{\partial H}{\partial q}$$

Then, the associated Hamiltonian vector field $X$ is given by

$$X = \begin{bmatrix}
\dot q\\ 
\dot p
\end{bmatrix}$$

1. Define the Hamiltonian vector field as a callable function, with two arguments ``q``, ``p``, as well as optional additional arguments `*arg`, which returns $\dot q$, and $\dot p$.
```
def X(q,p,k,m):
  return p/m, -k*q
```
2. Create a coordinate grid of the phase space you would like to make the phase portraits over (such as through `np.meshgrid`)
```
q = np.linspace(-5, 5, 21)
p = np.linspace(-5, 5, 31)
PS = np.meshgrid(q, p)
```
3. Use `FlowMate.plot_phase_portrait` to visualise the phase portraits
```
m = 2
k = 5
FlowMate.plot_phase_portrait(X, PS, args=[m, k])
```
## See Also
[1]  V. I. Arnold (1978). Mathematical Methods of Classical Mechanics. Springer New York, NY.

[2]  H. Goldstein, C. Poole, J. Safko (2002). Classical Mechanics (3rd Edition). Addison Wesley.

[3]  J. R. Taylor (2005). Classical Mechanics. University Science Books.

[4]  N. A. Lemos (2018). Analytical Mechanics. Cambridge University Press.
