"""healthmap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from user import views as userView
from forums import views as forumView
from filemanager import views as fileView
from .casehistory import views as caseView
from .medicalofficer import views as moView
from .patients import views as staffView
from .referral import views as referView

router = routers.DefaultRouter()
router.register(r'users', userView.UserViewSet)
router.register(r'groups', userView.GroupViewSet)
router.register(r'forum', forumView.ForumViewSet)
router.register(r'files', fileView.FilesViewSet)
router.register(r'case', caseView.CaseHistoryViewSet)
router.register(r'mo', moView.MOViewSet)
router.register(r'staff', staffView.StaffPersonViewSet)
router.register(r'refer', referView.ReferralViewSet)

# Settings for Interactive API documentation
API_TITLE = 'Health Map API'
API_DESCRIPTION = 'A web API to monitor and manage Health Related Data'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)), # noqa E501
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))  # noqa E501
]
