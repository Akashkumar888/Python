# In C++, the default access modifier for members of a class is private
# in python by default public

# public modifier

# class ABC:
#     def __init__(self):
#        self.public_attribute=None
#     def public_function():
#         pass


# obj1=ABC()
# obj1.public_attribute()
# print(obj1.public_attribute())
# obj1.public_function()

# public modifier

# class ABC:
#     def __init__(self):
#        self.__private_attribute=30
#     def __private_function():
#         pass

# obj1=ABC()
# print(obj1.__private_attribute)

# protected modifier

class ABC:
    def __init__(self):
       self._protected_attribute=30
    def _protected_function():
        pass

