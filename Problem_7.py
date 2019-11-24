'''
Using x//10 and x%10 to reverse
To make it easier to understand, I classified the x to positive, 0 and negative
Pay attention on overflow
'''

'''
A Python tip:
list of list can be created by:
    list_of_list= [] * n
    for i in range(n):
        list_of_list[i]=["a list here"]
'''

class Solution:
def reverse(self, x: int) -> int:
    num=x
    output=0
    if num>0:
        while num%10!=0 or num//10!=0:
            output=10*(output)+num%10
            num=num//10
        
    elif num==0:
        output=0
    else:
        num_tmp=0-num
        while num_tmp%10!=0 or num_tmp//10!=0:
            output=10*(output)+num_tmp%10
            num_tmp=num_tmp//10
        
        output*=(-1)
        
    #dealing with overflow
    if output>=2**31-1 or output<=-2**31:
        output=0
    
    
    return output

