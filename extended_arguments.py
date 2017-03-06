def hypervolume(*lengths):
    # shows proper use of iterators
    i = iter(lengths)
    v = next(i)
    for length in i:
        v *= length
    return v

print(hypervolume(2,4))

print(hypervolume(2,4,6))

# if passed with no args the function throws a stop Iteration error
# which is not meaningful so..

def hypervolume(length, *lengths):
    v = length
    for item in lengths:
        v *= item
    return v

print(hypervolume(2,4))

print(hypervolume(2,4,6))

def tag(name, **attributes):
    result = '<' + name
    for key, value in attributes.items():
        result += ' {k}="{v}"'.format(k=key, v=str(value))
    result += '>'
    return result

print(tag('img', src="moment.jpg", alt="Sunrise", border=1))

# arguemt passed affter * args becomes keyword arguments, it must be passed
# arguments after **kwargs is not allowed


