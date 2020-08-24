from django.urls import path
from . import views
from .views import CreateEntryView, EntryListView, EditEntryView, DeleteEntryView


urlpatterns = [
    path ('', views.about, name='home'),
    path('add_entry/', CreateEntryView.as_view(), name="add_entry"),
    path('view_book/', EntryListView.as_view(), name="view_book"),
    path('about/', views.about, name="about"),
    path ('<int:pk>', EditEntryView.as_view(), name="edit_entry"),
    path ('<int:pk>/remove', DeleteEntryView.as_view(), name="delete_entry"),

]