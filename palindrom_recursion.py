# def recrusion_pali(list):
   



# recrusion_pali(['r','y','n','y','u'])


# def ispalindrome(word):
#     if len(word) < 2: return True
#     if word[0] != word[-1]: return False
#     return ispalindrome(word[1:-1])
# ispalindrome('rinki')

def pallindrom(word):
    if len(word)<2:
        return True
    if word[0]!=word[-1]:
        return False
    return pallindrom(word[1:-1])
  
pallindrom('mom')

    
              