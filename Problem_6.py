'''
It's a simulation of the whole process
Adding chars in string respectively to n=numRows string lists
"direction" describe the direction of adding
    direction=1 means adding chars following the order of list[0] -> list[numRows-1]
    direction=-1 means adding chars following the order of list[numRows-1] -> list[0]
'''

'''
A Python tip:
list of list can be created by:
    list_of_list= [] * n
    for i in range(n):
        list_of_list[i]=["a list here"]
'''

class Solution:
def convert(self, s: str, numRows: int) -> str:
    
    outputstr=""
    if numRows<=1:
        outputstr=s
    else:
        output= [""] * numRows
    
        index_s=0
        direction=1
        for i in range(len(s)):
            colNo=i%numRows
            output[index_s]+=s[i]
            index_s+=direction
        
            if index_s == 0 or index_s==numRows-1:
                direction=direction*(-1)


        for j in range(numRows):
            outputstr+=output[j]
    
    return outputstr
