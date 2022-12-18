# Python solution for Longest Palindromic Substring (Manacher's Algorithm)

def manacher(s):
    n = len(s)

    # intersperse '#' characters in the original string
    s = aug(s, n)

    # the length of the augmented string
    length = 2*n + 1

    # p is the array that stores the expansion lengths 
    # of the palindromes centered at each index
    p = [0] * length

    # the center of the longest palindromic substring until now
    c = 0 

    # the right boundary of the longest palindromic substring until now
    r = 0

    # maximum length of the longest palindrome (final returned value) 
    maxLen = 0

    for i in range(length):
        # get mirror index (wrt center c) of i 
        mirror = 2*c - i

        # if the mirror of i is expanding beyond the left boundary 
        # of current longest palindrome at center c, then
        # take r - i as p[i]
        # else take p[mirror] as p[i]
        if i < r:
            p[i] = min(p[mirror], r - i)

        # expand at i
        a = i + p[i] + 1 
        b = i - p[i] - 1
        while a < length and b >= 0 and s[a] == s[b]:
            p[i] += 1 # increase p[i] and enlarge the range (a,b)
            a += 1
            b -= 1
        

        # check if the expanded palindrome at i is expanding beyond
        # the right boundary of current longest palindrome at center c
        # if it is, the new center is i
        if i + p[i] > r:
            c = i # update center
            r = i + p[i] # update r

            if p[i] > maxLen:
                maxLen = p[i] # update maxLen

    return maxLen


def aug(s, n):
    '''
    returns the string s augmented with '#'
    s = abcd --->  #a#b#c#d#
    n is the length of s
    '''
    t = []
    for i in range(n):
        t.append('#')
        t.append(s[i])
    t.append('#')
    return t



print(manacher('ycbc'))


