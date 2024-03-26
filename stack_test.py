from stack_another import stack

s=stack()

print(s.isempty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isempty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())
