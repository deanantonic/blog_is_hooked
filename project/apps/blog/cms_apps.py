from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class BlogApphook(CMSApp):
    name = _("Blog Application")   # give your application a name (required)
    urls = ["project.urls"]           # link your app to url configuration(s)
    app_name = "blog"


apphook_pool.register(BlogApphook)  # register the application