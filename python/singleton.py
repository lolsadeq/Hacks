#!/usr/bin/env python
# -*- coding: utf-8 -*-

#old style classes
class OnlyOneOld:
    class __OnlyOneOld:
        def __init__(self, arg):
            self.val = arg

        def __str__(self):
            return `self` + self.val

    instance = None

    def __init__(self, arg):
        if not OnlyOneOld.instance:
            OnlyOneOld.instance = OnlyOneOld.__OnlyOneOld(arg)
        else:
            OnlyOneOld.instance.val = arg

    def __getattr__(self, name):
        return getattr(self.instance, name)

# new style classes
class OnlyOneNew(object):
    class __OnlyOneNew:
        def __init__(self):
            self.val = None
        def __str__(self):
            return `self` + self.val

    instance = None

    def __new__(cls): # class method
        if not OnlyOneNew.instance:
            OnlyOneNew.instance = OnlyOneNew.__OnlyOneNew()

        return OnlyOneNew.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)

# borg style singleton
class Borg:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class SingleBorg(Borg):
    def __init__(self, arg):
        Borg.__init__(self)
        self.val = arg

    def __str__(self):
        return self.val

# decorator style singleton
class SingletonDecorator:
    def __init__(self, klass):
        self.klass = klass
        self.instance = None

    def __call__(self, *args, **kwds):
        if self.instance == None:
            self.instance = self.klass(*args, **kwds)

        return self.instance

class Foo:
    pass


# meta class style singleton
class SingletonMetaclass(type):
    def __init__(cls, name, bases, dect):
        super(SingletonMetaclass, cls).__init__(name, bases, dict)
        original_new = cls.__new__

        def my_new(cls, *args, **kwds):
            if cls.instance == None:
                cls.instance = original_new(cls, *args, **kwds)
            return cls.instance

        cls.instance = None
        cls.__new__ = staticmethod(my_new)

class Bar(object):
    __metaclass__ = SingletonMetaclass
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return `self` + self.val



def oldStyleClasses():
    x = OnlyOneOld('sausage')
    print x
    y = OnlyOneOld('eggs')
    print y
    z = OnlyOneOld('spam')
    print z
    print x
    print y
    print `x`
    print `y`
    print `z`


def newStyleClasses():
    x = OnlyOneNew()
    x.val = 'sausage'
    print x
    y = OnlyOneNew()
    y.val = 'eggs'
    print y
    z = OnlyOneNew()
    z.val = 'spam'
    print z
    print x
    print y


def borgClasses():
    x = SingleBorg('sausage')
    print x
    y = SingleBorg('eggs')
    print y
    z = SingleBorg('spam')
    print z
    print x
    print y
    print `x`
    print `y`
    print `z`


def decoratorClasses():
    foo = SingletonDecorator(Foo)
    x = foo()
    y = foo()
    z = foo()
    x.val = 'sausage'
    y.val = 'eggs'
    z.val = 'spam'
    print x.val
    print y.val
    print z.val
    print x is y is z


def metaclassClasses():
    x = Bar('sausage')
    y = Bar('eggs')
    z = Bar('spam')
    print x
    print y
    print z
    print x is y is z

def main():
    print 'OLD'
    oldStyleClasses()
    print

    print 'NEW'
    newStyleClasses()
    print

    print 'BORG'
    borgClasses()
    print

    print 'DECORATORS'
    decoratorClasses()
    print

    print 'METACLASS'
    metaclassClasses()
    print



if __name__ == '__main__':
    main()
