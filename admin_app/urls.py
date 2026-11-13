from django.urls import path
from admin_app import views


urlpatterns = [
    path('dashboard/', views.admin_dashboard, name="dashboard"),

    path('add_categories/', views.add_categories, name="add_categories"),
    path('view_categories/', views.view_categories, name="view_categories"),
    path('save_category/', views.save_category, name="save_category"),
    path('edit_categories/<int:cat_id>/', views.edit_categories, name="edit_categories"),
    path('update_category/<int:cat_id>/', views.update_category, name="update_category"),
    path('delete_category/<int:cat_id>/', views.delete_category, name="delete_category"),

    path('add_products/', views.add_products, name="add_products"),
    path('save_product/', views.save_product, name="save_product"),
    path('view_products/', views.view_products, name="view_products"),
    path('product_edit/<int:pro_id>/', views.product_edit, name="product_edit"),
    path('UpdateProduct/<int:pro_id>/', views.UpdateProduct, name="UpdateProduct"),
    path('delete_product/<int:pro_id>/', views.delete_product, name="delete_product"),

    path('admin_loginpage/', views.admin_loginpage, name="admin_loginpage"),
    path('admin_login/', views.admin_login, name="admin_login"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),


]