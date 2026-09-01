class Solution:
    def reverseBits(self, n: int) -> int:
        bits = []

        for _ in range(32):
            bits.append(n%2)
            n=n//2
        for bit in bits:
            n= 2*n+ bit
        return n