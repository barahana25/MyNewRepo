a = [5, 12, 28, 29, 40, 41, 53, 54, 68, 69, 79, 80, 83, 89, 90, 100]
x = input('Input a number: ')
left = 0
right = len(a) - 1

while left <= right:
    middle = (left + right) // 2
  
    if a[middle] == int(x):
        print('리스트 a[{:2}]에 {:3}가 있습니다.'.format(middle, x))
        break   
    elif a[middle] < int(x):
        left = middle + 1    
    else:
        right = middle - 1

if left > right:
    print('리스트에 {:3}가 없습니다.'.format(x))
