from django.views.generic import ListView, DetailView
from .models import *
from django.shortcuts import render, HttpResponse
from cart.cart import Cart
from django.contrib.auth import logout, login
from django.shortcuts import redirect
from django.views.generic import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from .utils import *
from django.urls import *
from .forms import RegisterUserForm
from cart.forms import CartAddProductForm
# from .context_process import balance


# class RegUser(DataMixin, CreateView):
#     form_class = RegisterUserForm
#     template_name = 'Products/register.html'
#     success_url = reverse_lazy('products:login')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         gt = self.context_object_return(title='Реєстрація')
#         return dict(list(context.items()) + list(gt.items()))

#     def form_valid(self, form):
#         print(self.object)
#         return super().form_valid(form)
    
def register(request):
    if request.method == 'POST':
        user_form = RegisterUserForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password1'])
            # Save the User object
            new_user.save()
            user = UserDetail.objects.create(user_old=new_user)
            user.save()
            login(request, new_user)
            return redirect('products:home')
    else:
        user_form = RegisterUserForm()
    return render(request, 'Products/register.html', {'form': user_form})

class LoginUs(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'Products/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        gt = self.context_object_return(title='Увійти')
        return dict(list(context.items()) + list(gt.items()))
    
    def get_success_url(self) -> str:
        return reverse_lazy('products:home')


def logout_user(request):
    logout(request)
    return redirect('products:login')


class ProductsList(ListView, DataMixin):
    model = Product
    context_object_name = 'products'
    template_name = 'Products/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        gt_ret = self.context_object_return(req=self.request, title='Головне меню')
        return dict(list(context.items()) + list(gt_ret.items()))

    def get_queryset(self):
        return Product.objects.filter(is_publish=True)

class CategoryList(ListView, DataMixin):
    model = Product
    context_object_name = 'products'
    template_name = 'Products/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        gt_ret = self.context_object_return(req=self.request, title=Category.objects.get(cat_slug=self.kwargs['cat_slug']).name)
        return dict(list(context.items()) + list(gt_ret.items()))

    def get_queryset(self):
        return Product.objects.filter(cat__cat_slug=self.kwargs['cat_slug'], is_publish=True)

class ProductDetail(DetailView, DataMixin):
    model = Product
    slug_url_kwarg = "product_slug"
    context_object_name = "product"
    template_name = 'Products/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = Product.objects.get(slug=self.kwargs['product_slug'])
        gt_ret = self.context_object_return(req=self.request, title=obj.name)
        context['form'] = CartAddProductForm()
        return dict(list(context.items()) + list(gt_ret.items()))
    
def get_accounts(request):
    return render(request, 'Products/accounts.html', {'title': 'Акаунти'})
