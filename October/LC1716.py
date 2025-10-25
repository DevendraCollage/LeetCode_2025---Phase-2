class Solution:
    def totalMoney(self, n: int) -> int:
        k = n // 7
        F = 28
        L = 28 + (k-1) * 7
        arithmetic_sum = k * (F + L) // 2

        monday = k + 1
        final_week = 0

        for day in range(n % 7):
            final_week += monday + day
            
        return final_week + arithmetic_sum    