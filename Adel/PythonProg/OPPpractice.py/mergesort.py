def divide(arr, l, r):
    if l < r:
        
        m1 = l + (r - l) // 3
        m2 = l + 2 * (r - l) // 3

        # Recursively divide the three parts
        divide(arr, l, m1)
        divide(arr, m1 + 1, m2)
        divide(arr, m2 + 1, r)

        # Merge the three parts
        merge(arr, l, m1, m2, r)


def merge(arr, l, m1, m2, r):
    # Lengths of the three segments
    n1 = m1 - l + 1
    n2 = m2 - m1
    n3 = r - m2

    # Temporary arrays for the three parts
    L = arr[l:m1 + 1]
    M = arr[m1 + 1:m2 + 1]
    R = arr[m2 + 1:r + 1]

    # Indices for the three arrays
    i, j, k = 0, 0, 0
    index = l

    # Merge elements from the three parts
    while i < n1 and j < n2 and k < n3:
        if L[i] <= M[j] and L[i] <= R[k]:
            arr[index] = L[i]
            i += 1
        elif M[j] <= L[i] and M[j] <= R[k]:
            arr[index] = M[j]
            j += 1
        else:
            arr[index] = R[k]
            k += 1
        index += 1

    # Merge remaining elements from L and M
    while i < n1 and j < n2:
        if L[i] <= M[j]:
            arr[index] = L[i]
            i += 1
        else:
            arr[index] = M[j]
            j += 1
        index += 1

    # Merge remaining elements from M and R
    while j < n2 and k < n3:
        if M[j] <= R[k]:
            arr[index] = M[j]
            j += 1
        else:
            arr[index] = R[k]
            k += 1
        index += 1

    # Merge remaining elements from L and R
    while i < n1 and k < n3:
        if L[i] <= R[k]:
            arr[index] = L[i]
            i += 1
        else:
            arr[index] = R[k]
            k += 1
        index += 1

    # Copy remaining elements of L, M, and R if any
    while i < n1:
        arr[index] = L[i]
        i += 1
        index += 1

    while j < n2:
        arr[index] = M[j]
        j += 1
        index += 1

    while k < n3:
        arr[index] = R[k]
        k += 1
        index += 1


# Input and execution
print("Enter the number of elements: ")
n = int(input())
arr = []

print("Enter the elements: ")
for i in range(n):
    x = int(input(f"Enter element {i + 1}: "))
    arr.append(x)

# Call the divide function to sort the array
divide(arr, 0, n - 1)

print("Sorted array is: ")
print(arr)
