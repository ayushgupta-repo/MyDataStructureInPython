
a = [1,2,1,2,2]

left_marker = 0
right_marker = len(a)-1

result = []

while left_marker != right_marker:
    if a[left_marker] == a[right_marker]:
        if a[left_marker] in result:
            continue
        else:
            result.append(a.pop(left_marker))
            left_marker = 0
            right_marker = len(a)-1
    else:
        right_marker -= 1

print(result)