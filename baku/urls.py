from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework_nested import routers
from game.views import *
from baku.views import IndexView

router = routers.SimpleRouter()
router.register(r'problems', ProblemsViewSet)

#Nested router accounts
problem_router = routers.NestedSimpleRouter(
    router, r'problems', lookup='problems'
)
problem_router.register(r'choices', ChoiceProblemViewSet)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'baku.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/v1/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/', include(problem_router.urls)),
    url('^.*$', IndexView.as_view(), name='index'),
)
