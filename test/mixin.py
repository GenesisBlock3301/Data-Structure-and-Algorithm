"""
a mixin is not intened to be used by itself . It always call or used by other class.
"""

class MetaMixin(object):
    def get_meta_title(self) -> str:
        return str(self.get_object())

class Foo(MetaMixin):
    def get_object(self):
        return "Nur AMin Sifat"

c = Foo()
print(c.get_meta_title())
