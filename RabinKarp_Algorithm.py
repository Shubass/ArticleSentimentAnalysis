# PART 2 - String Searching Algorithm
# Implementation of RABIN-KARP ALgorithm
class rabinkarp:
    d = 256  # Number of characters in input alphabet where a,b,c,... = 256

    def rabinkarp(self,T, P, d, q):  # define function for Rabin Karp Algorithm
        n = len(T)  # length of text
        m = len(P)  # length of pattern
        h = d ** (m - 1) % q
        p = 0  # hash value of pattern
        t = 0  # hash value of` text
        # assign indexes
        i = 0
        s = 0
        count = 0;

        # for loop to calculate hash value
        for i in range(m):
            p = (d * p + ord(P[i])) % q  # calculate hash value of pattern
            t = (d * t + ord(T[i])) % q  # calculate hash value of first window of text only

        # rolling hash to slide to the next window
        for s in range(n - m + 1):
            if p == t:  # check if current hash value of text window is same as pattern
                for i in range(m):  # check for characters of current window of text one by one
                    if T[i + s] != P[i]:  # if character of text and pattern is not same, break
                        break
                    else:
                        i += 1  # if character of text and pattern same, increment 1 to check next character

                if i == m:  # index is same as length of pattern
                    count += 1

            if s < (n - m):  #
                t = (d * (t - ord(T[s]) * h) + ord(T[s + m])) % q  # calculate the hash value of next text window
                # subtract with hash value of previous character and add hash value of next character

                if t < 0:  # in case the value of t is negative, make it positive
                    t = t + q

        return count
