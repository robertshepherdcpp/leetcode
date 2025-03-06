class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        if n == 0:
            return True
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                return True
            else:
                return False
        for i in range(len(flowerbed)):
            if flowerbed[i] != 1:
                if i != 0 and i != len(flowerbed)-1:
                    if flowerbed[i-1] != 1 and flowerbed[i+1] != 1:
                        flowerbed[i] = 1
                        n-=1
                else:
                    if i == 0:
                        if flowerbed[i+1] != 1:
                            flowerbed[i] = 1
                            n-=1
                    elif i == len(flowerbed)-1:
                        if flowerbed[i-1] != 1:
                            flowerbed[i] = 1
                            n-=1
        return n <= 0
