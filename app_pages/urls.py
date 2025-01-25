from django.urls import path


from app_pages import views

app_name = "pages"

urlpatterns = [
    path('',views.PortfolioView.as_view(),name="home")
]