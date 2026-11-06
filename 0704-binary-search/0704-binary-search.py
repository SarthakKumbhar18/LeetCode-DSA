class Solution:
    def search(self, l: List[int], t: int) -> int:

        s = 0
        e = len(l) - 1

        while(s <= e):

            m = int(s + (e - s)/2)

            if(l[m] == t):
                return m

            elif(l[m] < t):
                s = m + 1

            else:
                e = m - 1

        return -1
        