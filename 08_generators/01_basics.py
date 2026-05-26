def serve_chai():
    yield "Cup 1 : Masala Chai"
    yield "Cup 2 : Ginger Chai"
    yield "Cup 3 : Cardamom Chai"

stall = serve_chai()
print(next(stall))

for cup in stall:
    print(r"The cup is : ", cup)


def get_chai_list():
    return ["Cup 1", "Cup 2", "Cup 3"]


def get_chai_generator():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

print(get_chai_list())
print(get_chai_generator())

chai_gen = get_chai_generator()
print(next(chai_gen))
print(next(chai_gen))
print(next(chai_gen))
