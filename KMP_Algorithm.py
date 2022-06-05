class KMP:
    # Python program for KMP Algorithm
    def KMPSearch(self, pat, txt):
        count = 0
        M = len(pat)  # length of pattern
        N = len(txt)  # length of String
        j = 0  # index for pat[]
        i = 0  # index for txt[]

        # create an array pi[] that will hold the longest matching prefix suffix values for the pattern
        pi = [0] * M  # size of array is the length of the pattern

        # Preprocess the pattern (calculate pi[] array)
        self.computePIArray(pat, M, pi)
        # while i has not reached end of the String

        while i < N:  # —-------------------- O(n)
            # character in String matches with pattern
            if pat[j] == txt[i]:
                i += 1  # increment index of txt[]
                j += 1  # increment index of pat[]

            # all characters in pattern match in the String
            if j == M:
                count += 1
                j = pi[j - 1]  # continue searching for pattern in the rest of the String

            # mismatch after j matches
            elif i < N and pat[j] != txt[i]:
                if j > 0:
                    j = pi[j - 1]
                else:
                    i += 1  # continue searching until find a match with j[0]
        return count

    def computePIArray(self, pat, M, pi):
        k = 0  # length of the previous longest prefix suffix

        pi[0] = 0  # pi[0] is always 0
        q = 1

        # the loop calculates pi[i] for i = 1 to M-1
        while q < M:  # —-------------------- O(m)
            if pat[q] == pat[k]:
                k += 1  # increment k by 1
                pi[q] = k
                q += 1  # increment q by 1
            else:
                if k != 0:
                    k = pi[k - 1]  # value of k is the value of pi of index before k
                    # compare matches with next value
                    # if does not match, compare next until k = 0

                else:
                    pi[q] = 0  # no matches with previous pat[] pi[q]= 0
                    q += 1
