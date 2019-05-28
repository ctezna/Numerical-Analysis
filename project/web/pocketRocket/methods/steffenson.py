"""
Requirements :python 2.7,python-matplotlib,python-numpy
Note :plot function is tweaked for discussed example, may not function properly for other scenario.
"""
from math import *
#import matplotlib.pyplot as pyplot
import numpy as np
from sympy import sympify, symbols

def plot(h,roots):
    x=np.linspace(.66,.71,1000)
    y=h(x)    
    yr=[0]*len(roots)    
    pyplot.plot(x,y)
    pyplot.axhline(0)
    pyplot.axvline(0.66)    
    pyplot.plot(roots,yr,marker="o",color='r')
    for i in xrange(len(roots)):
        pyplot.text(roots[i], 0.06, 'guess '+str(i),rotation=90,va='bottom')
        pyplot.axvline(x=roots[i], ymin=0.69, ymax=.75, linewidth=1,color='black')
    pyplot.text(0.69,-.1,'f(x)=x^3-9*(x^2)+3.8197',rotation=323)
    pyplot.grid()
    pyplot.show()

def arerror(old,new):
    """
    Return absolute relative error as percentage, considering new as the new guess and old as the previous guess.
    """
    return abs((new-old)/float(new))*100

def sigdigit(err):
    """
    Calculate # of signifficant digits in answer, using the relative error.
    """
    sigdigit=0
    count=0
    
    while err<1:
        err*=10
        count+=1
        
    fact=err/5.0
    
    if fact<=1:  sigdigit=count+1
    else:       sigdigit=count
    
    return sigdigit

def f(x):
    """
    Definition of the desired function to solve.
    """   
    y=x**3-9*(x**2)+3.8197
    
    return y

def steff(f,x0,tol,maxiter):
    x0 = float(x0)
    tol = float(tol)
    maxiter = int(maxiter)
    """
    Implementation of Steffensen's method
    Two versions of Steffensen's method implemented in the code shown below can be found using the Aitken's delta-squared process for accelerating convergence of a sequence & the genaral equation for Steffensen's method. To compare the two formulas, notice that xn_genral = x_atk - xn_atk . This method assumes starting with a linearly convergent sequence and increases the rate of convergence of that sequence.  
    REF: http://en.wikipedia.org/wiki/Steffensen's_method
    """
    data = {"N": [], "xi": [], "root": []}
    roots=[]
    x_list = []
    cont = 0
    #x_list = []
    #n = 0
    for i in range(1,maxiter):
        
        roots.append(x0)
        """
        formula derivated from Aitken's delta-squared process
        """
        x = x0
        x1=x0 + eval(f)
        x = x1
        x2=x1 + eval(f)
        x_0=x0-((x1-x0)**2/(x2-2*x1+x0))
        x_list.append(x_0)
        #print(x_0)
        #print ("x0: %s x1: %s" % (str(evalu), str(evalu2)))
        """
        here is the genaral formula
        """
        
        #~ x=x0-(f(x0)**2/(f(x0+f(x0))-f(x0)))
        
        err=arerror(x0,x_0)
        #print '%d: x_old(x0) = %f x_new(x) = %f error = %f percent num of signifficant digits in x: %d' % (i,x0,x,err,sigdigit(err))
        if err<=tol:
            #print 'converged to %e in %d iterations' % (x,i)
            return {'N': [i for i in range(len(roots))], 'xi':x_list, 'roots': roots}
        x0=x_0
    #print 'failed to converge in %d iterations' % maxiter

    return {'N': [i for i in range(len(roots))], 'xi':x_list, 'roots': roots}

#roots=steff(f,.7)
#print (roots)
#plot(f,roots)
