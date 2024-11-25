import matplotlib.pyplot as plt
import numpy as np
import math

class polynomial():

    #Init function
    ######################################################################
    def __init__(self, coeff):
      self.coeff = coeff
    ######################################################################

    #String Function
    ######################################################################
    def __str__(self):

        base_string=""

        #Loop backwards through the coefficients
        for i in reversed(range(len(self.coeff))):

            #If a coefficient is nonzero, include the term in the polynomial
            if(self.coeff[i] != 0):

                #Add terms
                if (i==0):
                    base_string+=str(self.coeff[i])+" + "
                else:
                    base_string += str(self.coeff[i]) + "X^" + str(i)+" + "

        return base_string[:-3]
    ######################################################################

    #Function degree() - Return degree of polynomial
    ######################################################################
    def degree(self):

      #Return exponent of first nonzero coefficient
      for i in reversed(range(len(self.coeff))):
          if(self.coeff[i] !=0):
                return i
    ######################################################################

    #Function graph() - Plot the polynomial on the input range
    ######################################################################
    def graph(self, min, max):
        if min > max:
          print("Error:  Range mimimum cannot be greater than range maximum")
          return

        x=np.linspace(min, max, 1000)

        #Evaluate y
        y=x*0
        for i in reversed(range(len(self.coeff))):
            y+= self.coeff[i]*x**i

        plt.plot(x,y)
        plt.show()
    ######################################################################

    #Function find_roots() - Look for roots in the input range
    ######################################################################
    def find_roots(self, min, max):
        if min > max:
          print("Error:  Range mimimum cannot be greater than range maximum")
          return

        x=np.linspace(min, max, 100000000)

        #Evaluate y
        y=x*0
        for i in reversed(range(len(self.coeff))):
            y+= self.coeff[i]*x**i

        #List to store roots
        roots = []

        print("Finding roots...")

        for i in range(len(y)-1):

            #Roots between y values
            if (y[i] < 0 and y[i+1] > 0) or (y[i] > 0 and y[i+1] < 0):
                roots.append((x[i]+x[i+1])/2)

            #Roots at y values
            if(y[i]==0):
                roots.append(x[i])

        return roots
    ######################################################################

    #Function eval() - Evaluate the polynomial at an input value of x
    ######################################################################
    def eval(self, val):
        y=0

        for i in range(len(self.coeff)):
            y+= self.coeff[i] * val **i

        return y
    ######################################################################

    #Function copy() - Create copy of polynomial
    ######################################################################
    def copy(self):
        return polynomial(self.coeff)
    ######################################################################

    #Function scale() - scale the coefficients of a polynomial
    ######################################################################
    def scale(self, scale):
        for i in range(len(self.coeff)):
            self.coeff[i] = self.coeff[i]*scale
    ######################################################################

    #Function max() - find max of polynomial in given range
    ######################################################################
    def poly_max(self, min_range, max_range):

      if min_range > max_range:
        print("Error:  Range mimimum cannot be greater than range maximum")
        return

      x=np.linspace(min_range, max_range, 100000000)

      print("Finding max...")

      #Evaluate y
      y=x*0
      for i in reversed(range(len(self.coeff))):
        y+= self.coeff[i]*x**i

      return max(y)
    ######################################################################

    #Function min() - find min of polynomial in given range
    ######################################################################
    def poly_min(self, min_range, max_range):

        if min_range > max_range:
          print("Error:  Range mimimum cannot be greater than range maximum")
          return

        x=np.linspace(min_range, max_range, 100000000)

        print("Finding min...")

        #Evaluate y
        y=x*0
        for i in reversed(range(len(self.coeff))):
            y+= self.coeff[i]*x**i

        return min(y)
    ######################################################################

    #Function get_coeff() - Return coefficient of specified order of term
    ######################################################################
    def get_coeff(self, power):
        if power < 0 or (power*10)%10 != 0:
          print("Error: Power must be non-negative whole number")
          return

        return self.coeff[power]
    ######################################################################

    #Function plot_taylor() - Evaluate the Taylor Series at a given point
    ######################################################################
    def plot_taylor(self, center, order, min_range, max_range):

        if min_range > max_range:
          print("Error:  Range mimimum cannot be greater than range maximum")
          return


        x=np.linspace(min_range, max_range, 1000)

        #First plot y
        y=x*0
        for i in reversed(range(len(self.coeff))):
            y+= self.coeff[i]*x**i

        plt.plot(x,y, label= "Polynomial")

        #a is where the polynomial is centered
        a=center

        #Init output
        output=0*x
        output+=self.eval(a)*(x-a)**0
        ref=self.derive()

        #Taylor Series
        for i in range(1,order+1):

          output += ref.eval(a)*(x-a)**i/math.factorial(i)
          ref=ref.derive()

        #Plot
        plt.plot(x,output, label="Taylor Approx")
        plt.legend()
        plt.show()

    ######################################################################


    def add(self, poly2):
        if not isinstance(poly2, polynomial):
            return TypeError("Error")
        max_len = max(len(self.coeff), len(poly2.coeff))
        result = [0] * max_len
        for i in range(max_len):
            coef1 = self.coeff[i] if i < len(self.coeff) else 0
            coef2 = poly2.coeff[i] if i < len(poly2.coeff) else 0
            result[i] = coef1+coef2
        return polynomial(result)


    def sub(self, poly2):
        if not isinstance(poly2, polynomial):
            return TypeError("Error")
        max_len = max(len(self.coeff), len(poly2.coeff))
        result = [0] * max_len
        for i in range(max_len):
            coef1 = self.coeff[i] if i < len(self.coeff) else 0
            coef2 = poly2.coeff[i] if i < len(poly2.coeff) else 0
            result[i] = coef1-coef2
        return polynomial(result)


    def multiply(self, poly2):
        if not isinstance(poly2, polynomial):
            return TypeError("error")
        result = [0] * (len(self.coeff) + len(poly2.coeff) - 1)
        for i, coef1 in enumerate(self.coeff):
            for j, coef2 in enumerate(poly2.coeff):
                result[i + j] += coef1 * coef2
        return polynomial(result)


    def divide(self, poly2):
        if not isinstance(poly2, polynomial):
            return TypeError("Error")
        if len(poly2.coeff) == 0 or poly2.coeff[0] == 0:
            return ZeroDivisionError("Cannot Divide by 0")
        divisor = len(poly2.coeff) - 1
        dividend = self.coeff[:]
        result = [0] * (len(dividend) - divisor)
        for i in range(len(dividend) - divisor):
            if poly2.coeff[0]==0:
                raise ZeroDivisionError("Cannot Divide by 0")
            result[i] = dividend[i]/poly2.coeff[0]
            for j in range(divisor + 1):
                dividend[i+j] -= result[i] * poly2.coeff[j]
        return polynomial(result)


    def derive(self):
        if len(self.coeff) <= 1:
            return polynomial([0])
        self.coeff.reverse()
        result = [coef*(len(self.coeff)-i-1) for i, coef in enumerate(self.coeff[:-1])]
        result.reverse()
        self.coeff.reverse()
        return polynomial(result)


    def integrate(self, constant='C'):
        result = [constant] + [coef/(i+1) for i, coef in enumerate(self.coeff)]
        return polynomial(result)
