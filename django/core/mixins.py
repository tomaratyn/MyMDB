from django.core.cache import caches
from django.views.decorators.cache import (
    cache_page)
from django.views.decorators.vary import \
    vary_on_cookie


class CachePageVaryOnCookieMixin:
    """
    Mixin caching a single page.

    Subclasses can provide these attributes:

    `cache_name` - name of cache to use.
    `timeout` - cache timeout for this
    page. When not provided, the default
    cache timeout is used.
    """
    cache_name = 'default'

    @classmethod
    def get_timeout(cls):
        if hasattr(cls, 'timeout'):
            return cls.timeout
        cache = caches[cls.cache_name]
        return cache.default_timeout

    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super().as_view(
            *args, **kwargs)
        view = vary_on_cookie(view)
        view = cache_page(
            timeout=cls.get_timeout(),
            cache=cls.cache_name,
        )(view)
        return view
