'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  if n <= 1:
    return False
  if n % 2 == 0:
    return False
  div = 3
  while div * div <= n:
    if n % div == 0:
      return False
    div = div + 2

  return True
  
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  # codul vostru aici
  
  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  while x != y:
    if x < y:
      y = y - x
    else:
      x = x - y
  return x

  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  if x < y:
    aux = x
    x = y
    y = aux

  r = 1
  while r != 0:
    r = x % y
    y = r
    x = y

  return y
  
  
def main():
  # interfata de tip consola aici

if __name__ == '__main__':
  main()
