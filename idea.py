
number = input() #input the length of the numbers
s = input() #all the numbers without one
ugjet = -1
for i in range(3):
    j =  i + 1
    step_size = i + 1
    while j < len(s):
        prev = int(s[j - step_size: j])
        new_step = len(str(int(prev) + 1))
        current = int(s[j: j + new_step]) 
        if current - prev != 1:
            if ugjet != -1 or current - prev != 2:
                ugjet = -1
                break
            ugjet = current - 1
        step_size = new_step
        j += step_size
    if ugjet != -1: break


print(ugjet)




