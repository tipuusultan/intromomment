from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',    include('account.urls' ,    namespace="account") ),
    path('',    include('admin_section.urls',  namespace="admin_section" )),
    path('',    include('client.urls' ,     namespace="client") ),
    path('',    include('home.urls' ,       namespace="home") ),
    path('',    include('influencer.urls' , namespace="influencer") ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)