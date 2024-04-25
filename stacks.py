def create_array_from_stacks(*stacks):
    result_array = []
    for stack in stacks:
        while stack:
            result_array.append(stack.pop())
    return result_array
    stack1 = [1,2,3]
    stack2 = [4,5,6] 
    stack3 = [7,8,9]

result = create_array_from_stacks(stack1, stack2, stack3)
print(result)   
