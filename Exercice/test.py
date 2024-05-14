import numpy as np
def somme_cumulative(tableau):
  somme_pair = np.cumsum(tableau[np.where(tableau % 2 == 0)])
  somme_impair = np.cumsum(tableau[np.where(tableau % 2 != 0)])
  return (somme_pair, somme_impair)
    
    
tableau = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(somme_cumulative(tableau))