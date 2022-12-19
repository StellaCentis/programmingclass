def is_prime(n):
    for i in range(2, n//2 +1):
        if n%1 == 0:
            return False
    
    return True

n = 7

print(n, 'is prime?', is_prime(n))

if __name__ == '__main__': #if the file is called, run this. otherwise, not
    for i in range(20):
        print(i,' is prime?', is_prime(i))
#se no ogni volta me lo stampa anche nel file "project"