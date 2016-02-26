from __future__ import unicode_literals
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sites.models import Site
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.sitemaps.views import sitemap
from django.utils.translation import ugettext_lazy as _

from cms.sitemaps import CMSSitemap
from solid_i18n.urls import solid_i18n_patterns as i18n_patterns

urlpatterns = [
    url(r'^$', 'blog.views.index'),	
    #url(r'^blog/view/(?P<slug>[^\.]+).html', 'blog.views.view_post', name='view_blog_post'),
    #url(r'^blog/category/(?P<slug>[^\.]+).html', 'blog.views.view_category', name='view_blog_category'),
]
