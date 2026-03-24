class Fibonacci:
    """Class for calculating Fibonacci sequence"""
    def term(self, N):
        a = 0
        b = 1
        for i in range(2, N + 1):
            c = a + b
            a = b
            b = c
        return a

    def fibo(self, N, M):
        a = 0
        b = 1
        result = []
        for j in range(N):
            if a % M == 0:
                result.append(a)
            c = a + b
            a = b
            b = c
        return result   
            
fibon = Fibonacci()
print(fibon.fibo(100,7))