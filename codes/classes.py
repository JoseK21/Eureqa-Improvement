class Individual:
  def __init__(self, x = None, r = None, e = None, f_f = None, f_g = None, k1_f = None, k2_f = None, k1_g = None, k2_g = None):
    self.x = x          # x value
    self.r = r          # Result h(x)
    self.e = e          # Error %
    self.f_f = f_f      # Function f(x)
    self.f_g = f_g      # Function g(x)
    self.k1_f = k1_f    # Constant k1 of f(x)
    self.k2_f = k2_f    # Constant k2 of f(x)
    self.k1_g = k1_g    # Constant k1 of g(x)
    self.k2_g = k2_g    # Constant k2 of g(x)

  def _update(self, x, r, e, f_f, f_g, k1_f, k2_f, k1_g, k2_g):
    self.x = x      
    self.r = r      
    self.e = e      
    self.f_f = f_f  
    self.f_g = f_g  
    self.k1_f = k1_f
    self.k2_f = k2_f
    self.k1_g = k1_g
    self.k2_g = k2_g

  def printInfo(self):
    if(self.f_f.__name__ in ["sin", "cos"] and self.f_g.__name__ in ["sin", "cos"]):
        print('h({0}) = {1}{2}({3}*{0}) + {4}{5}({6}*{0})'.format(self.x, self.k1_f, self.f_f.__name__, self.k2_f, self.k1_g, self.f_g.__name__, self.k2_g))
    elif(self.f_f.__name__ == "cos" and self.f_g.__name__ == "sin"):
        print('.................')

    print("|-> {1}".format(self.x, self.r,))