from constants import *


class Individual:
  def __init__(self, x = None, Va = None, e = None, c1 = None, c2 = None, f_f = None, f_g = None, k1_f = None, k2_f = None, k1_g = None, k2_g = None):
    self.x = x          # x Value
    self.Va = Va        # Result h(x)
    self.e = e          # Error %
    self.c1 = c1        # Constant 1 function
    self.c2 = c2        # Constant 2 function
    self.f_f = f_f      # Function f(x)
    self.f_g = f_g      # Function g(x)
    self.k1_f = k1_f    # Constant k1 of f(x)
    self.k2_f = k2_f    # Constant k2 of f(x)
    self.k1_g = k1_g    # Constant k1 of g(x)
    self.k2_g = k2_g    # Constant k2 of g(x)

  def _update(self, x, r, e, c1, c2, f_f, f_g, k1_f, k2_f, k1_g, k2_g):
    self.x = x      
    self.r = r      
    self.e = e      
    self.c1 = c1
    self.c2 = c2
    self.f_f = f_f  
    self.f_g = f_g  
    self.k1_f = k1_f
    self.k2_f = k2_f
    self.k1_g = k1_g
    self.k2_g = k2_g

  def printInfo(self):
    # >>>>>>>> sin || cos
    if(FUNCTIONS[self.f_f].__name__ in ["sin", "cos"] and FUNCTIONS[self.f_g].__name__ in ["sin", "cos"]):
      print('h({0}) = {1}{2}({3}*{0}) + {4}{5}({6}*{0})'.format(self.x, self.k1_f, FUNCTIONS[self.f_f].__name__, self.k2_f, self.k1_g, FUNCTIONS[self.f_g].__name__, self.k2_g))
  
    elif(FUNCTIONS[self.f_f].__name__ in ["sin", "cos"] and FUNCTIONS[self.f_g].__name__ == "constant"):
      print('h({0}) = {1}{2}({3}*{0}) + {4}'.format(self.x, self.k1_f, FUNCTIONS[self.f_f].__name__, self.k2_f, self.c2))

    elif(FUNCTIONS[self.f_f].__name__ in ["sin", "cos"] and FUNCTIONS[self.f_g].__name__ == "poli4"):
      print('h({0}) = {1}{2}({3}*{0}) + (5*{0})^4 + (4*{0})^3 + (3*{0})^2 + 2*{0} + 1'.format(self.x, self.k1_f, FUNCTIONS[self.f_f].__name__, self.k2_f))

    elif(FUNCTIONS[self.f_f].__name__ in ["sin", "cos"] and FUNCTIONS[self.f_g].__name__ == "expo"):
      print('h({0}) = {1}{2}({3}*{0}) + {4}*e^({5}*{0})'.format(self.x, self.k1_f, FUNCTIONS[self.f_f].__name__, self.k2_f, self.k1_g, self.k2_g))

    # >>>>>>>> constant
    elif(FUNCTIONS[self.f_f].__name__ == "constant" and FUNCTIONS[self.f_g].__name__ == "constant"):
      print('h({0}) = {1} + {2}'.format(self.x, self.c1, self.c2))

    elif(FUNCTIONS[self.f_f].__name__ == "constant" and FUNCTIONS[self.f_g].__name__ == "poli4"):
      print('h({0}) = {1} + (5*{0})^4 + (4*{0})^3 + (3*{0})^2 + 2*{0} + 1'.format(self.x, self.c1))
  
    elif(FUNCTIONS[self.f_f].__name__ == "constant" and FUNCTIONS[self.f_g].__name__ == "expo"):
      print('h({0}) = {1} + {2}*e^({3}*{0})'.format(self.x, self.c1, self.k1_g, self.k2_g))
    
    elif(FUNCTIONS[self.f_f].__name__ == "constant" and FUNCTIONS[self.f_g].__name__ in ["sin", "cos"]):
      print('h({0}) = {4} + {1}{2}({3}*{0})'.format(self.x, self.k1_g, FUNCTIONS[self.f_g].__name__, self.k2_g, self.c1))

    # >>>>>>>> poli4
    elif(FUNCTIONS[self.f_f].__name__ == "poli4" and FUNCTIONS[self.f_g].__name__ == "constant"):
      print('h({0}) = (5*{0})^4 + (4*{0})^3 + (3*{0})^2 + 2*{0} + 1 + {1}'.format(self.x, self.c2))

    elif(FUNCTIONS[self.f_f].__name__ == "poli4" and FUNCTIONS[self.f_g].__name__ == "poli4"):
      print('h({0}) = (5*{0})^4 + (4*{0})^3 + (3*{0})^2 + 2*{0} + 1 + (5*{0})^4 + (4*{0})^3 + (3*{0})^2 + 2*{0} + 1'.format(self.x))
  
    elif(FUNCTIONS[self.f_f].__name__ == "poli4" and FUNCTIONS[self.f_g].__name__ == "expo"):
      print('h({0}) = (5*{0})^4 + (4*{0})^3 + (3*{0})^2 + 2*{0} + 1 + {2}*e^({3}*{0}) '.format(self.x, self.k1_g, self.k2_g))
    
    elif(FUNCTIONS[self.f_f].__name__ == "poli4" and FUNCTIONS[self.f_g].__name__ in ["sin", "cos"]):
      print('h({0}) = (5*{0})^4 + (4*{0})^3 + (3*{0})^2 + 2*{0} + 1 + {1}{2}({3}*{0})'.format(self.x, self.k1_g, FUNCTIONS[self.f_g].__name__, self.k2_g))
  
    # >>>>>>>> expo
    elif(FUNCTIONS[self.f_f].__name__ == "expo" and FUNCTIONS[self.f_g].__name__ == "constant"):
      print('h({0}) = {2}*e^({3}*{0}) + {1}'.format(self.x, self.c2, self.k1_f, self.k2_f))

    elif(FUNCTIONS[self.f_f].__name__ == "expo" and FUNCTIONS[self.f_g].__name__ == "poli4"):
      print('h({0}) = {1}*e^({2}*{0}) + (5*{0})^4 + (4*{0})^3 + (3*{0})^2 + 2*{0} + 1'.format(self.x, self.k1_g, self.k2_g))
  
    elif(FUNCTIONS[self.f_f].__name__ == "expo" and FUNCTIONS[self.f_g].__name__ == "expo"):
      print('h({0}) = {1}*e^({2}*{0}) + {3}*e^({4}*{0})'.format(self.x, self.k1_f, self.k2_f, self.k1_g, self.k2_g))
    
    elif(FUNCTIONS[self.f_f].__name__ == "expo" and FUNCTIONS[self.f_g].__name__ in ["sin", "cos"]):
      print('h({0}) = {4}*e^({5}*{0}) + {1}{2}({3}*{0})'.format(self.x, self.k1_g, FUNCTIONS[self.f_g].__name__, self.k2_g, self.k1_f, self.k2_f))

    print("     = {0}\n".format(self.Va))
