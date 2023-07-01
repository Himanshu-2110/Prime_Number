def Prime_number(n):
    if n <= 1:
        return False
    c=0
    j=1
  # This is the key Point of this fuction .
  # When we know ood number is not divaid by even number than why we use this use all number to check n%i.
    if n%2!=0:
        j=2
    for i in range(2,n//2+1,j):
        if n%i==0:
            c=1
            return False
    if c == 0:
        return True
    return False

# function call
print(Prime_number(79))
