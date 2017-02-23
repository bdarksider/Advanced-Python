class CallMe(object):
    def __call__(self):
        print("called")

a = CallMe()

print(a) # returns instance address 

a() # prints "called" 

