"""Extensible memoizing collections and decorators."""

from .cache import Cache
from .decorators import cached, cachedasync, cachedmethod
from .lfu import LFUCache
from .lru import LRUCache
from .rr import RRCache
from .ttl import TTLCache

__all__ = (
    'Cache',
    'LFUCache',
    'LRUCache',
    'RRCache',
    'TTLCache',
    'cached',
    'cachedasync',
    'cachedmethod'
)

__version__ = '4.0.0'
