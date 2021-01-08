max = 25 # Get the maximum position
list_1 = [''*(max-n-1)+'*'*(2*n+1) for n in range(max)] # For first part of arrow
list_2 = [''*int((2*max-int((2*max+1)*3/11))/2)+'*'*(int((2*max+1)*3/11)) for n in range(max//2)] # Second part

for top in list_1:
    print(top)

for tel in list_2:
    print(tel)