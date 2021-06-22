from constants import *
from functions import error


class Individual:
  def __init__(self, f = None, g = None, cf = None, cg = None, k1_f = None, k2_f = None, k1_g = None, k2_g = None, e = None, rank = None):
    self.f = f          # Function f(x)
    self.g = g          # Function g(x)
    self.cf = cf        # Constant 1 function
    self.cg = cg        # Constant 2 function
    self.k1_f = k1_f    # Constant k1 of f(x)
    self.k2_f = k2_f    # Constant k2 of f(x)
    self.k1_g = k1_g    # Constant k1 of g(x)
    self.k2_g = k2_g    # Constant k2 of g(x)
    self.e = e          # Error %
    self.rank = rank    # Rank %

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
  
  def printInfo(self, x, ind__, setRank = True):
    e_string = ''
    if(setRank):
      self.rank = ind__
    # >>>>>>>> sin || cos
    if(FUNCTIONS[self.f].__name__ in ["sin", "cos"] and FUNCTIONS[self.g].__name__ in ["sin", "cos"]):
      e_string = 'h({0}) = {1}{2}({3}*{0}) + {4}{5}({6}*{0})'.format(x, self.k1_f, FUNCTIONS[self.f].__name__, self.k2_f, self.k1_g, FUNCTIONS[self.g].__name__, self.k2_g)
      print(ind__ + e_string, end='\n')
  
    elif(FUNCTIONS[self.f].__name__ in ["sin", "cos"] and FUNCTIONS[self.g].__name__ == "constant"):
      e_string = 'h({0}) = {1}{2}({3}*{0}) + {4}'.format(x, self.k1_f, FUNCTIONS[self.f].__name__, self.k2_f, self.cg)
      print(ind__ + e_string, end='\n')

    elif(FUNCTIONS[self.f].__name__ in ["sin", "cos"] and FUNCTIONS[self.g].__name__ == "poli4"):
      e_string = 'h({0}) = {1}{2}({3}*{0}) + 5*({0}**4) + 4*({0}**3) + 3*({0}**2) + 2*{0} + 1'.format(x, self.k1_f, FUNCTIONS[self.f].__name__, self.k2_f)
      print(ind__ + e_string, end='\n')

    elif(FUNCTIONS[self.f].__name__ in ["sin", "cos"] and FUNCTIONS[self.g].__name__ == "expo"):
      e_string = 'h({0}) = {1}{2}({3}*{0}) + {4}*e**({5}*{0})'.format(x, self.k1_f, FUNCTIONS[self.f].__name__, self.k2_f, self.k1_g, self.k2_g)
      print(ind__ + e_string, end='\n')

    # >>>>>>>> constant
    elif(FUNCTIONS[self.f].__name__ == "constant" and FUNCTIONS[self.g].__name__ == "constant"):
      e_string = 'h({0}) = {1} + {2}'.format(x, self.cf, self.cg)
      print(ind__ + e_string, end='\n')

    elif(FUNCTIONS[self.f].__name__ == "constant" and FUNCTIONS[self.g].__name__ == "poli4"):
      e_string = 'h({0}) = {1} + 5*({0}**4) + 4*({0}**3) + 3*({0}**2) + 2*{0} + 1'.format(x, self.cf)
      print(ind__ + e_string, end='\n')
  
    elif(FUNCTIONS[self.f].__name__ == "constant" and FUNCTIONS[self.g].__name__ == "expo"):
      e_string = 'h({0}) = {1} + {2}*e**({3}*{0})'.format(x, self.cf, self.k1_g, self.k2_g)
      print(ind__ + e_string, end='\n')
    
    elif(FUNCTIONS[self.f].__name__ == "constant" and FUNCTIONS[self.g].__name__ in ["sin", "cos"]):
      e_string = 'h({0}) = {1} + {2}{3}({4}*{0})'.format(x, self.cf, self.k1_g, FUNCTIONS[self.g].__name__, self.k2_g)
      print(ind__ + e_string, end='\n')

    # >>>>>>>> poli4
    elif(FUNCTIONS[self.f].__name__ == "poli4" and FUNCTIONS[self.g].__name__ == "constant"):
      e_string = 'h({0}) = 5*({0}**4) + 4*({0}**3) + 3*({0}**2) + 2*{0} + 1 + {1}'.format(x, self.cg)
      print(ind__ + e_string, end='\n')

    elif(FUNCTIONS[self.f].__name__ == "poli4" and FUNCTIONS[self.g].__name__ == "poli4"):
      e_string = 'h({0}) = 5*({0}**4) + 4*({0}**3) + 3*({0}**2) + 2*{0} + 1 + 5*({0}**4) + 4*({0}**3) + 3*({0}**2) + 2*{0} + 1'.format(x)
      print(ind__ + e_string, end='\n')
  
    elif(FUNCTIONS[self.f].__name__ == "poli4" and FUNCTIONS[self.g].__name__ == "expo"):
      e_string = 'h({0}) = 5*({0}**4) + 4*({0}**3) + 3*({0}**2) + 2*{0} + 1 + {1}*e**({2}*{0}) '.format(x, self.k1_g, self.k2_g)
      print(ind__ + e_string, end='\n')
    
    elif(FUNCTIONS[self.f].__name__ == "poli4" and FUNCTIONS[self.g].__name__ in ["sin", "cos"]):
      e_string = 'h({0}) = 5*({0}**4) + 4*({0}**3) + 3*({0}**2) + 2*{0} + 1 + {1}{2}({3}*{0})'.format(x, self.k1_g, FUNCTIONS[self.g].__name__, self.k2_g)
      print(ind__ + e_string, end='\n')
  
    # >>>>>>>> expo
    elif(FUNCTIONS[self.f].__name__ == "expo" and FUNCTIONS[self.g].__name__ == "constant"):
      e_string = 'h({0}) = {1}*e**({2}*{0}) + {3}'.format(x, self.k1_f, self.k2_f, self.cg)
      print(ind__ + e_string, end='\n')

    elif(FUNCTIONS[self.f].__name__ == "expo" and FUNCTIONS[self.g].__name__ == "poli4"):
      e_string = 'h({0}) = {1}*e**({2}*{0}) + 5*({0}**4) + 4*({0}**3) + 3*({0}**2) + 2*{0} + 1'.format(x, self.k1_f, self.k2_f)
      print(ind__ + e_string, end='\n')
  
    elif(FUNCTIONS[self.f].__name__ == "expo" and FUNCTIONS[self.g].__name__ == "expo"):
      e_string = 'h({0}) = {1}*e**({2}*{0}) + {3}*e**({4}*{0})'.format(x, self.k1_f, self.k2_f, self.k1_g, self.k2_g)
      print(ind__ + e_string, end='\n')
    
    elif(FUNCTIONS[self.f].__name__ == "expo" and FUNCTIONS[self.g].__name__ in ["sin", "cos"]):
      e_string = 'h({0}) = {1}*e**({2}*{0}) + {3}{4}({5}*{0})'.format(x, self.k1_f, self.k2_f, self.k1_g, FUNCTIONS[self.g].__name__, self.k2_g)
      print(ind__ + e_string, end='\n')

    else:
      print('\n\n\n\n\n\n-------------------------------ERROR-------------------------------\n\n')

    return e_string[7: len(e_string)]

  def update_e(self):
      f_f = FUNCTIONS[self.f]
      f_g = FUNCTIONS[self.g]

      e_ = 0
      for x in range(1, 119):
          Vreal = H[x - 1]

          Vaprox = f_f(x, self.k1_f, self.k2_f, self.cf) + f_g(x, self.k1_g, self.k2_g, self.cg)

          e = error(Vreal, Vaprox)
          e_ =+ e

      self.e = (e_/118) * 100