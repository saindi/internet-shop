from django.urls import path
from catalog import views


app_name = 'catalog'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home_url'),

    path('category/', views.CategoryListView.as_view(), name='category_list_url'),
    path('category/create/', views.CategoryCreateView.as_view(), name="category_create_url"),
    path('category/<slug:category_slug>/update/', views.CategoryUpdateView.as_view(), name="category_update_url"),
    path('category/<slug:category_slug>/delete/', views.CategoryDeleteView.as_view(), name="category_delete_url"),

    path('product/create/', views.ProductCreateView.as_view(), name="product_create_url"),
    path('category/<slug:category_slug>/', views.ProductListView.as_view(), name="product_list_url"),
    path('product/<slug:product_slug>/', views.ProductDetailView.as_view(), name="product_detail_url"),
    path('product/<slug:product_slug>/update/', views.ProductUpdateView.as_view(), name="product_update_url"),
    path('product/<slug:product_slug>/delete/', views.ProductDeleteView.as_view(), name="product_delete_url"),


    path('staff/category/', views.StaffCategoryListView.as_view(), name="staff_category_list_url"),
    path('staff/product/', views.StaffProductListView.as_view(), name="staff_product_delete_url"),
]
