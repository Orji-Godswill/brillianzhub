from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

from django.views.generic.base import RedirectView

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    path('', views.index_view, name="home"),
    path('accounts/', include("accounts.passwords.urls")),
    path('accounts/', RedirectView.as_view(url='/account')),
    path('account/', include("accounts.urls", namespace="account")),
    path('settings/', RedirectView.as_view(url='/account')),
    path('admin/', admin.site.urls),

    # path('investment-packages/', include("package.urls")),
    path('financial-calculator/', include("analyser.urls")),
    path('blog-investments/', include("blog.urls")),
    path('investment-packages/', include('package.urls')),
    path('referrals/', include('referral.urls')),
    path('order/', include('order.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('dividend/', include('dividend.urls')),
    path('courses/', include("course.urls")),


    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('contact/', views.contact_view, name="contact"),
    path('about/', views.about_view, name="about"),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
