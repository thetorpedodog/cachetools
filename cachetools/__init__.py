"""Extensible memoizing collections and decorators."""

from .cache import Cache
from .decorators import cached, cachedmethod
from .lfu import LFUCache
from .lru import LRUCache
from .rr import RRCache
from .tlru import TLRUCache
from .ttl import TTLCache

__all__ = (
    'Cache',
    'LFUCache',
    'LRUCache',
    'RRCache',
    'TLRUCache',
    'TTLCache',
    'cached',
    'cachedmethod'
)

__version__ = '4.0.0'
