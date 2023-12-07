#Function to find the first non-repeating character in a string.
def nonrepeatingCharacter(s):
        hmp = {}
        for i in s:
                if i in hmp:
                        hmp[i] += 1
                else:
                        hmp[i] = 1
        for i in s:
                if hmp[i] == 1:
                        return i
                
        return "$"
nonrepeatingCharacter(s='shjhdcissi')