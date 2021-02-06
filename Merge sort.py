def mergeSort(A):
    if len(A) > 1:
        r = len(A)//2
        L = A[:r]
        M = A[r:]
        mergeSort(L)
        mergeSort(M)
        i = j = k = 0
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                A[k] = L[i]
                i = i+1
            else:
                A[k] = M[j]
                j = j+1
            k = k+1
        while i < len(L):
            A[k] = L[i]
            i = i+1
            k = k+1
        while j < len(M):
            A[k] = M[j]
            j = j+1
            k = k+1
A = []
x =int(input("Enter number of array needed: "))
for n in range(x):
    print("Enter the element :")
    ele =int(input())
    A.append(ele)
mergeSort(A)
print("Sorted array is: ")
for i in range(len(A)):
    print(A[i],"")