def greet_user():
    """greeting."""
    print("Hello, how are you dear?")
    
greet_user()

def greet_user(username):
    """simple greeting"""
    print("Hello " + username + ", how are you doing today?")
greet_user("diana")  


def describe_house(size,type):
    """House description."""
    print("\nSize of this house is " + size + ".")
    print("This is a " + type + " house!" )
describe_house(str(120) + " m2", "luxury")
describe_house(str(100) + " m2" , "medium")



def describe_house(size,type):
    """Description of the house."""
    print("\nArea of the house is " + size + ".")
    print("This is a " + type + " house.")
describe_house(type="luxury",size="120 m2")
describe_house(size=("100 m2"), type="contemporary")

#default
def car_brands(brand,price="45000$"):
    print("\nI have a " + brand + ".")
    print("Its price is " + price + ".")
car_brands("Mclaren","100000$")
car_brands("Mersedes benz - S class",)

#None

def car_brands(brand,price=None):
    print("\nThis is " + brand + "!")
    if price:
        print("Its value is " + price + ".")
car_brands("BMW","10000 $")
car_brands("Bentley")

# return

def get_full_name(first,last):
    """Return formated fullname"""
    full_name = first + " " + last +  "."
    return full_name.title()

musician = get_full_name("bob","marley")
print(musician)

# returning a dictionary

def writer(first,last):
    """Writer's full name"""
    writer_fn = {"first": first , "last": last}
    return writer_fn
famous_writer = writer("Steven","King")
print(famous_writer)

# returning an optional dictionary

def writers(first,last,gender=None):
    f_writers = {
        "first":first,
        "last":last
    }
    if gender:
        f_writers["gender"] = gender
    return f_writers

famous_writer = writers("Alexander","Diuma","male")
print(famous_writer)
famous_writer = writers("Doris","lesing")
print(famous_writer)

# list in a function

def famous_footbalers(names):
    """A short list of famous footbalers
    """
    for name in names:
        greet = "Hello " + "its " + name + ", glad to see you there !"
        print(greet)

lst_of_footbalers = ["Muller","Drogba","Pogba"]
famous_footbalers(lst_of_footbalers)    

# collecting arbitrary number of arguments
def type_of_houses(type, *rooms):
    """building a house"""
    print("\nI want to build " + type + " style house.")
    print("Number of rooms:")
    for room in rooms:
        print("-" + room + "room")

type_of_houses("Contemporary","1","2","3")
type_of_houses("cottage", str(1),str(2))

# keyword arguments in function


def building_profile(first,last, **person_info):
    """Building a famous people's profiles"""
    profile = {
        "first":first,
        "last":last
    }
    for key,value in person_info.items():
        profile[key]= value
    return profile

famous_1 = building_profile(
    "kylian","mbappe",
    Field= "footbal",
    age= 20
    )
famous_2 = building_profile(
    "dwayne","jonson",
    field="movie industry"
    
)
print(famous_1)
print(famous_2)