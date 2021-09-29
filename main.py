'''
Returneaza true daca n este prim si false daca nu.
'''


def is_prime(n):
  if n <= 1:
    return False
  if n==2:
    return True
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
  n = int(input("Da lungimea listei: "))
  p = 1
  for i in range(n):
    nr = int(input("Da al "+str(i+1)+"-lea numar "))
    lst.append(nr)
  i = 0
  while i < len(lst):
    p = p * lst[i]
    i = i + 1

  return p

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
  nr=int(input("Ce problema vrei rezolvata?(1=Prime,2=CMMDC scadere,3=CMMDC impartire,4:Produs din lista): "))

  if nr==1:
    print("Problema de numere prime.")
    n=int(input("Da numarul: "))
    print(is_prime(n))

  if nr==2:
    print("CMMDC prin metoda scaderii.")
    a=int(input("Da primul numar: "))
    b=int(input("Da al doilea numar: "))
    print(get_cmmdc_v1(a,b))

  if nr==3:
    print("CMMDC prin metoda impartirii.")
    a=int(input("Da primul numar: "))
    b = int(input("Da al doilea numar: "))
    print(get_cmmdc_v2(a, b))

  if nr==4:
    print("Produsul a n numere: ")
    thislist =[]
    print(get_product(thislist))


if __name__ == '__main__':
  main()
