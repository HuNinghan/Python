#----------------------args----------------------------------
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(3, 5, 6, 12, 55, 4))
# collect all inputs into a tuple



#----------------------kwargs----------------------------------
def calculate(n, **kwargs):
    n += kwargs["add"]
    n*= kwargs["multiple"]
    print(n)


calculate(2, add=3, multiple=5)
# collect all inputs into a dictionary


#-----------------------use args and kwargs to create a class---------------------------------
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        # if key does not exist, the get() function will just return null instead of an error


my_car = Car(make="Nissan", model="GT-3")
print(my_car.model)