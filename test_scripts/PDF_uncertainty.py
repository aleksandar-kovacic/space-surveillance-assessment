from datetime import datetime
from matplotlib import cm
from configparser import ConfigParser
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sympy import factor, factor_nc
parameter_config = ConfigParser(converters={'list': lambda x: [i.strip() for i in x.split(',')]})
parameter_config.read("config.ini")

#####################################################################################################################################################
"""from scipy.stats import multivariate_normal
x = np.linspace(-4, 4, 100)
y = np.linspace(-4, 4, 100)
X, Y = np.meshgrid(x, y)
pos = np.dstack((X, Y))
mu = np.array([0, 0])
a=0.0001
cov = np.array([[1*a, 0],[0, 1*a]])
rv = multivariate_normal(mu, cov)
Z = rv.pdf(pos)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, zorder=3)



xx, yy = np.meshgrid(np.linspace(-4,4,100), np.linspace(-4,4,100))
z = xx*0+0.1
ax1 = plt.subplot(projection='3d')
ax1.plot_surface(xx, yy, z, alpha=1, zorder=4)
plt.show()"""
#####################################################################################################################################################
"""
# Imports

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import cm # Colormaps
import matplotlib.gridspec as gridspec
from mpl_toolkits.axes_grid1 import make_axes_locatable
import seaborn as sns

sns.set_style('darkgrid')
np.random.seed(42)


def multivariate_normal(x, d, mean, covariance):
    x_m = x - mean
    return (1. / (np.sqrt((2 * np.pi)**d * np.linalg.det(covariance))) * 
            np.exp(-(np.linalg.solve(covariance, x_m).T.dot(x_m)) / 2))

# Plot bivariate distribution
def generate_surface(mean, covariance, d):
    nb_of_x = 50 # grid size
    x1s = np.linspace(-5, 5, num=nb_of_x)
    x2s = np.linspace(-5, 5, num=nb_of_x)
    x1, x2 = np.meshgrid(x1s, x2s) # Generate grid
    pdf = np.zeros((nb_of_x, nb_of_x))
    # Fill the cost matrix for each combination of weights
    for i in range(nb_of_x):
        for j in range(nb_of_x):
            pdf[i,j] = multivariate_normal(
                np.matrix([[x1[i,j]], [x2[i,j]]]), 
                d, mean, covariance)
    return x1, x2, pdf  # x1, x2, pdf(x1,x2)

# subplot
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(8,4))
d = 2  # number of dimensions

a = 0.1

# Plot of independent Normals
bivariate_mean = np.matrix([[0.], [0.]])  # Mean
bivariate_covariance = np.matrix([
    [1*a, 0], 
    [0, 1*a]])  # Covariance
x1, x2, p = generate_surface(
    bivariate_mean, bivariate_covariance, d)
# Plot bivariate distribution
con = ax1.contourf(x1, x2, p, 33, cmap=cm.YlGnBu)
ax1.set_xlabel('$x_1$', fontsize=13)
ax1.set_ylabel('$x_2$', fontsize=13)
ax1.axis([-2.5, 2.5, -2.5, 2.5])
ax1.set_aspect('equal')
ax1.set_title('Independent variables', fontsize=12)

# Plot of correlated Normals
bivariate_mean = np.matrix([[0.], [1.]])  # Mean
bivariate_covariance = np.matrix([
    [1, 0], 
    [0, 1]]) # Covariance
x1, x2, p = generate_surface(
    bivariate_mean, bivariate_covariance, d)
# Plot bivariate distribution
con = ax2.contourf(x1, x2, p, 33, cmap=cm.YlGnBu)
ax2.set_xlabel('$x_1$', fontsize=13)
ax2.set_ylabel('$x_2$', fontsize=13)
ax2.axis([-2.5, 2.5, -1.5, 3.5])
ax2.set_aspect('equal')
ax2.set_title('Correlated variables', fontsize=12)

# Add colorbar and title
fig.subplots_adjust(right=0.8)
cbar_ax = fig.add_axes([0.85, 0.15, 0.02, 0.7])
cbar = fig.colorbar(con, cax=cbar_ax)
cbar.ax.set_ylabel('$p(x_1, x_2)$', fontsize=13)
plt.suptitle('Bivariate normal distributions', fontsize=13, y=0.95)
plt.show()"""
#####################################################################################################################################################
"""import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

# Our 2-dimensional distribution will be over variables X and Y
N = 60
X = np.linspace(-3, 3, N)
Y = np.linspace(-3, 4, N)
X, Y = np.meshgrid(X, Y)

# Mean vector and covariance matrix
mu = np.array([0, 0])
a=0.01
Sigma = np.array([[ 1*a , 0], [0,  1*a]])

# Pack X and Y into a single 3-dimensional array
pos = np.empty(X.shape + (2,))
pos[:, :, 0] = X
pos[:, :, 1] = Y

def multivariate_gaussian(pos, mu, Sigma):

    n = mu.shape[0]
    Sigma_det = np.linalg.det(Sigma)
    Sigma_inv = np.linalg.inv(Sigma)
    N = np.sqrt((2*np.pi)**n * Sigma_det)
    # This einsum call calculates (x-mu)T.Sigma-1.(x-mu) in a vectorized
    # way across all the input variables.
    fac = np.einsum('...k,kl,...l->...', pos-mu, Sigma_inv, pos-mu)

    return np.exp(-fac / 2) / N

# The distribution on the variables X, Y packed into pos.
Z = multivariate_gaussian(pos, mu, Sigma)

# Create a surface plot and projected filled contour plot under it.
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(X, Y, Z, rstride=3, cstride=3, linewidth=1, antialiased=True,
                cmap=cm.viridis)

cset = ax.contourf(X, Y, Z, zdir='z', offset=-0.15, cmap=cm.viridis)

# Adjust the limits, ticks and view angle
#ax.set_zlim(-0.15,1)
#ax.set_zticks(np.linspace(0,2,5))
ax.set_xticks(np.linspace(-3, 3, 6))
ax.set_yticks(np.linspace(-3, 3, 6))
ax.view_init(27, -21)

plt.show()"""
#####################################################################################################################################################
"""from intersect import intersection
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
x = np.linspace(-5, 5, 1000, endpoint=False)
y = multivariate_normal.pdf(x, mean=0, cov=0.01)
#print(max(y))
fig1 = plt.figure()
ax = fig1.add_subplot(111)
ax.plot(x, y)

x2=np.array([-5, 5])
y2=np.array([max(y)*0.99, max(y)*0.99])
plt.plot(x2, y2)
#plt.hlines(max(y)*0.99, -5, 5)
a, b = intersection(x, y, x2, y2)
print(a,b)

plt.show()"""
#####################################################################################################################################################
"""import matplotlib.pyplot as plt
from intersect import intersection
from scipy.stats import multivariate_normal

#3D Plot
steps = 0.001 #0.01
boundary = 0.05
x_3d, y_3d = np.mgrid[-boundary:boundary:steps, -boundary:boundary:steps] 
pos_3d = np.dstack((x_3d, y_3d))
a=0.01

rv_3d = multivariate_normal([0, 0], [[1*a, 0], [0, 1*a]])
fig2 = plt.figure(figsize=(12,5))
ax2 = fig2.add_subplot(121, projection='3d')
ax2.plot_surface(x_3d, y_3d, rv_3d.pdf(pos_3d))



#2D Plot
x = np.linspace(-5, 5, 1000, endpoint=False)
y = multivariate_normal.pdf(x, mean=0, cov=1*a)
#print(max(y))
#fig1 = plt.figure()
ax = fig2.add_subplot(122)
ax.plot(x, y)
#Intersection Calculation
x2=np.array([-5, 5])
y2=np.array([max(y)*0.99, max(y)*0.99])
plt.plot(x2, y2)
a, b = intersection(x, y, x2, y2)
print(a,b)

plt.show()"""

"""from mpl_toolkits import mplot3d
from scipy.stats import multivariate_normal
var = multivariate_normal(mean=[0,0], cov=[[0.01,0],[0,0.01]])

values = []
x_vector = []
y_vector = []
loop_range = list(np.linspace(-5,5,100))
for i in range(len(loop_range)):
    for j in range(len(loop_range)):
        a = var.pdf([loop_range[i],loop_range[j]])
        values.append(a)
        x_vector.append(i)
        y_vector.append(j)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot(x_vector,y_vector,values, zorder = 1)

#z = [max(values)] * 10000
#ax.plot(x_vector, y_vector, z, zorder = 0)

#plt.show()"""

from intersect import intersection
from scipy.stats import multivariate_normal
lower_plot_boundary = -5
upper_plot_boundary = 5
x = np.linspace(lower_plot_boundary, upper_plot_boundary, 5000)
satellite = 0.1
cov_factor = 0.1
y = multivariate_normal([0, 0], [[1*cov_factor+satellite, 0], [0, 1*cov_factor+satellite]])
probability_list = []
for i in range(len(x)):
    y_1 = y.pdf([x[i],0])
    probability_list.append(y_1)
plt.plot(x, probability_list, label = "PDF for\n$\u03C3_1$ = $\u03C3_2$ = " + str(cov_factor) + "km")

#Intersection Calculation
x_intersection = np.array([lower_plot_boundary, upper_plot_boundary])
#ACPL = 0.9998999536
ACPL = 0.425
#y_intersection=np.array([max(probability_list)*ACPL, max(probability_list)*ACPL])
y_intersection=np.array([ACPL, ACPL])
plt.plot(x_intersection, y_intersection, label = "ACPL = " + str(ACPL))
a, b = intersection(x, probability_list, x_intersection, y_intersection)
plt.hlines(xmin = a[0], xmax=a[1], y = ACPL, color = "red", label="$A_{ACPL}$ = " + str("{:.2f}".format(((a[0])**2)*np.pi)) + " km$^2$")
plt.ylim(0, 0.2)
plt.legend()
plt.xlabel("x [km]")
plt.ylabel("p")
print(a,b)
#plt.savefig("cov_"+str(cov_factor)+".pdf")

"""#3D Plot
steps = 0.1 #0.01
boundary = 5
x_3d, y_3d = np.mgrid[-boundary:boundary:steps, -boundary:boundary:steps] 
pos_3d = np.dstack((x_3d, y_3d))
a=1

rv_3d = multivariate_normal([0, 0], [[2*1*a, 0], [0, 2*1*a]])
fig2 = plt.figure(figsize=(12,5))
ax2 = fig2.add_subplot(121, projection='3d')
ax2.plot_surface(x_3d, y_3d, rv_3d.pdf(pos_3d))"""

plt.show()