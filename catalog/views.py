from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, RedirectView

from catalog.models import CategoryModel, ProductModel
from mysite.utils import StaffProfileRequiredMixin
from cart.forms import CartAddProductForm


class HomeView(RedirectView):
    pattern_name = 'catalog:category_list_url'


class CategoryListView(ListView):
    model = CategoryModel
    template_name = 'catalog/category_list.html'
    context_object_name = 'categories'


class CategoryUpdateView(StaffProfileRequiredMixin, UpdateView):
    model = CategoryModel
    fields = '__all__'
    slug_url_kwarg = 'category_slug'
    template_name = 'catalog/update.html'


class CategoryDeleteView(StaffProfileRequiredMixin, DeleteView):
    model = CategoryModel
    template_name = 'catalog/delete.html'
    slug_url_kwarg = 'category_slug'
    success_url = '/'


class CategoryCreateView(StaffProfileRequiredMixin, CreateView):
    model = CategoryModel
    template_name = 'catalog/create.html'
    fields = '__all__'


class ProductListView(ListView):
    model = ProductModel
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = CategoryModel.objects.get(slug=self.kwargs['category_slug'])

        if "price_range" not in context:
            context["price_range"] = [0, 50000]

        return context

    def get_queryset(self):
        return ProductModel.objects.filter(category__slug=self.kwargs['category_slug'])

    def post(self, request, *args, **kwargs):
        price_range = request.POST.get('price_range').split(";")

        self.object_list = self.get_queryset().filter(price__range=price_range)

        return render(request, self.template_name, self.get_context_data(price_range=price_range))


class ProductDetailView(DetailView):
    model = ProductModel
    slug_url_kwarg = 'product_slug'
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_product_form'] = CartAddProductForm()

        return context


class ProductUpdateView(StaffProfileRequiredMixin, UpdateView):
    model = ProductModel
    template_name = 'catalog/update.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'
    fields = '__all__'


class ProductDeleteView(StaffProfileRequiredMixin, DeleteView):
    model = ProductModel
    template_name = 'catalog/delete.html'
    slug_url_kwarg = 'product_slug'
    success_url = reverse_lazy('catalog:home_url')


class ProductCreateView(StaffProfileRequiredMixin, CreateView):
    model = ProductModel
    template_name = 'catalog/create.html'
    fields = '__all__'


class StaffCategoryListView(StaffProfileRequiredMixin, ListView):
    model = CategoryModel
    template_name = 'catalog/staff_category_list.html'
    context_object_name = 'categories'
    paginate_by = 10


class StaffProductListView(StaffProfileRequiredMixin, ListView):
    model = ProductModel
    template_name = 'catalog/staff_product_list.html'
    context_object_name = 'products'
    paginate_by = 10
