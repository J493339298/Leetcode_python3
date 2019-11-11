#Using two pointer sliding though each list
#Median always occurs around (len(nums1)+len(nums2))/2
#Need to discuss different situations according to whether length sum is odd or even
#Need to consider the problem of "out of range", which may happen when one of lists reach the end.

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sum_len=len(nums1)+len(nums2)
        if sum_len%2 ==0:
            med_idx=sum_len/2+1
        else:
            med_idx=sum_len//2+1
            
        i1=i2=0
        l=[]
        n1=n2=0
        for i in range(0,int(med_idx)):
            if i1<len(nums1) and i2<len(nums2):
                if nums1[i1]<=nums2[i2]:
                    l.append(nums1[i1])
                    i1=i1+1
                else:
                    l.append(nums2[i2])
                    i2=i2+1
            elif i1==len(nums1) and i2<len(nums2):
                l.append(nums2[i2])
                i2=i2+1
            elif i1<len(nums1) and i2==len(nums2):
                l.append(nums1[i1])
                i1=i1+1
            
        med=0
        if sum_len%2 ==0:
            med=(l[len(l)-2]+l[len(l)-1])/2
        else:
            med=l[len(l)-1]
        return med

