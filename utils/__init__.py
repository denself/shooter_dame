import sys

__author__ = 'Denis Ivanets (denself@gmail.com)'


def singleton(cls):
    def _singleton(*args, **kwargs):
        if _singleton.obj is None:
            _singleton.obj = cls(*args, **kwargs)
        return _singleton.obj
    _singleton.obj = None
    return _singleton


class ResourceManager(object):

    resource_map = {}

    def __new__(cls, *args, **kwargs):
        return cls

    @classmethod
    def resource_old(cls, old_cls):
        def _new_class(new_cls, *args, **kwargs):
            key = old_cls.get_key(*args, **kwargs)
            res = cls.resource_map.get(key)
            if res is None:
                res = super(old_cls, new_cls).__new__(new_cls, *args)
                cls.resource_map[key] = res
            return res
        old_cls.__new__ = _new_class
        return old_cls

    @classmethod
    def resource(cls, new_cls):

        assert hasattr(new_cls, 'get_key'), \
            "Resource does not have get_key method"

        def _new_class(*args, **kwargs):
            key = new_cls.get_key(*args, **kwargs)
            res = cls.resource_map.get(key)
            if res is None:
                res = new_cls(*args, **kwargs)
                cls.resource_map[key] = res
            return res
        return _new_class

    @classmethod
    def free_unused_resources(cls):
        for key, value in cls.resource_map.items():
            if sys.getrefcount(value) < 5:
                cls.resource_map.pop(key)
