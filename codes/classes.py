from constants import *
from functions import error


class Individual:
  def __init__(self, f = None, g = None, cf = None, cg = None, k1_f = None, k2_f = None, k1_g = None, k2_g = None, e = None, rank = None):
    self.f = f      # Function f(x)
    self.g = g      # Function g(x)
    self.cf = cf        # Constant 1 function
    self.cg = cg        # Constant 2 function
    self.k1_f = k1_f    # Constant k1 of f(x)
    self.k2_f = k2_f    # Constant k2 of f(x)
    self.k1_g = k1_g    # Constant k1 of g(x)
    self.k2_g = k2_g    # Constant k2 of g(x)
    self.e = e          # Error %
    self.rank = rank          # Rank %

  def printData(self):
    print('f : ', self.f)
    print('g : ', self.g)
    print('cf : ', self.cf)
    print('cg : ', self.cg)
    print('k1_f : ', self.k1_f)
    print('k2_f : ', self.k2_f)
    print('k1_g : ', self.k1_g)
    print('k2_g : ', self.k2_g)
    print('e : ', self.e)
  
  def printInfo(self, x, ind__):
    self.rank = ind__
    # print('\033[94m', end='\n')
    # >>>>>>>> sin || cos
    if(FUNCTIONS[self.f].__name__ in ["sin", "cos"] and FUNCTIONS[self.g].__name__ in ["sin", "cos"]):
      print(ind__ + 'h({0}) = {1}{2}({3}*{0}) + {4}{5}({6}*{0})'.format(x, self.k1_f, FUNCTIONS[self.f].__name__, self.k2_f, self.k1_g, FUNCTIONS[self.g].__name__, self.k2_g), end='\n')
  
    elif(FUNCTIONS[self.f].__name__ in ["sin", "cos"] and FUNCTIONS[self.g].__name__ == "constant"):
      print(ind__ + 'h({0}) = {1}{2}({3}*{0}) + {4}'.format(x, self.k1_f, FUNCTIONS[self.f].__name__, self.k2_f, self.cg), end='\n')

    elif(FUNCTIONS[self.f].__name__ in ["sin", "cos"] and FUNCTIONS[self.g].__name__ == "poli4"):
      print(ind__ + 'h({0}) = {1}{2}({3}*{0}) + 5*({0}**4) + 4*({0}**3) + 3*({0}**2) + 2*{0} + 1'.format(x, self.k1_f, FUNCTIONS[self.f].__name__, self.k2_f), end='\n')

    elif(FUNCTIONS[self.f].__name__ in ["sin", "cos"] and FUNCTIONS[self.g].__name__ == "expo"):
      print(ind__ + 'h({0}) = {1}{2}({3}*{0}) + {4}*e**({5}*{0})'.format(x, self.k1_f, FUNCTIONS[self.f].__name__, self.k2_f, self.k1_g, self.k2_g), end='\n')

    # >>>>>>>> constant
    elif(FUNCTIONS[self.f].__name__ == "constant" and FUNCTIONS[self.g].__name__ == "constant"):
      print(ind__ + 'h({0}) = {1} + {2}'.format(x, self.cf, self.cg), end='\n')

    elif(FUNCTIONS[self.f].__name__ == "constant" and FUNCTIONS[self.g].__name__ == "poli4"):
      print(ind__ + 'h({0}) = {1} + 5*({0}**4) + 4*({0}**3) + 3*({0}**2) + 2*{0} + 1'.format(x, self.cf), end='\n')
  
    elif(FUNCTIONS[self.f].__name__ == "constant" and FUNCTIONS[self.g].__name__ == "expo"):
      print(ind__ + 'h({0}) = {1} + {2}*e**({3}*{0})'.format(x, self.cf, self.k1_g, self.k2_g), end='\n')
    
    elif(FUNCTIONS[self.f].__name__ == "constant" and FUNCTIONS[self.g].__name__ in ["sin", "cos"]):
      print(ind__ + 'h({0}) = {1} + {2}{3}({4}*{0})'.format(x, self.cf, self.k1_g, FUNCTIONS[self.g].__name__, self.k2_g), end='\n')

    # >>>>>>>> poli4
    elif(FUNCTIONS[self.f].__name__ == "poli4" and FUNCTIONS[self.g].__name__ == "constant"):
      print(ind__ + 'h({0}) = 5*({0}**4) + 4*({0}**3) + 3*({0}**2) + 2*{0} + 1 + {1}'.format(x, self.cg), end='\n')

    elif(FUNCTIONS[self.f].__name__ == "poli4" and FUNCTIONS[self.g].__name__ == "poli4"):
      print(ind__ + 'h({0}) = 5*({0}**4) + 4*({0}**3) + 3*({0}**2) + 2*{0} + 1 + 5*({0}**4) + 4*({0}**3) + 3*({0}**2) + 2*{0} + 1'.format(x), end='\n')
  
    elif(FUNCTIONS[self.f].__name__ == "poli4" and FUNCTIONS[self.g].__name__ == "expo"):
      print(ind__ + 'h({0}) = 5*({0}**4) + 4*({0}**3) + 3*({0}**2) + 2*{0} + 1 + {1}*e**({2}*{0}) '.format(x, self.k1_g, self.k2_g), end='\n')
    
    elif(FUNCTIONS[self.f].__name__ == "poli4" and FUNCTIONS[self.g].__name__ in ["sin", "cos"]):
      print(ind__ + 'h({0}) = 5*({0}**4) + 4*({0}**3) + 3*({0}**2) + 2*{0} + 1 + {1}{2}({3}*{0})'.format(x, self.k1_g, FUNCTIONS[self.g].__name__, self.k2_g), end='\n')
  
    # >>>>>>>> expo
    elif(FUNCTIONS[self.f].__name__ == "expo" and FUNCTIONS[self.g].__name__ == "constant"):
      print(ind__ + 'h({0}) = {1}*e**({2}*{0}) + {3}'.format(x, self.k1_f, self.k2_f, self.cg), end='\n')

    elif(FUNCTIONS[self.f].__name__ == "expo" and FUNCTIONS[self.g].__name__ == "poli4"):
      print(ind__ + 'h({0}) = {1}*e**({2}*{0}) + 5*({0}**4) + 4*({0}**3) + 3*({0}**2) + 2*{0} + 1'.format(x, self.k1_f, self.k2_f), end='\n')
  
    elif(FUNCTIONS[self.f].__name__ == "expo" and FUNCTIONS[self.g].__name__ == "expo"):
      print(ind__ + 'h({0}) = {1}*e**({2}*{0}) + {3}*e**({4}*{0})'.format(x, self.k1_f, self.k2_f, self.k1_g, self.k2_g), end='\n')
    
    elif(FUNCTIONS[self.f].__name__ == "expo" and FUNCTIONS[self.g].__name__ in ["sin", "cos"]):
      print(ind__ + 'h({0}) = {1}*e**({2}*{0}) + {3}{4}({5}*{0})'.format(x, self.k1_f, self.k2_f, self.k1_g, FUNCTIONS[self.g].__name__, self.k2_g), end='\n')

    # print("\033[0m, Fitness: {0}\n".format(self.e))

  def update_e(self):
      f_f = FUNCTIONS[self.f]
      f_g = FUNCTIONS[self.g]

      e_ = 0
      for x in range(1, 119):
          h_x = H[x - 1]

          Va = f_f(x, self.k1_f, self.k2_f, self.cf) + f_g(x, self.k1_g, self.k2_g, self.cg)
          e = error(h_x, Va)
          e_ =+ e

      self.e = (e_/118) * 100