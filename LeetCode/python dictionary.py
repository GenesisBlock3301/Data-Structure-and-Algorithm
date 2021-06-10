greeting = "Hello {}"
default_name = "World"
name = "Sifat"

def get(name,**kwargs):
    print(kwargs,name)
    name = kwargs.pop("name", default_name)
    return greeting.format(name)

print(get(name))


#
# class SuperVillainView(GreetView):
#     greeting = "We are the future {}.Not them."
#     default_name = "My friend"
