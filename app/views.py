from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, DetailView, CreateView, ListView, View
from app.models import Menu, Order, Employee, Check, Menu_Item

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"

class ProfileView(DetailView):
    model = get_user_model()
    context_object_name = 'user_object'
    template_name = 'accounts/profile.html'

    def get_object(self):
        return self.request.user

class MenuView(ListView):
    model = Menu
    template = "menu_view.html"

class LoginView(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                return HttpResponseRedirect('/form')
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)

        return render(request, "index.html")

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)

class CreateOrderView(CreateView):
    model = Order
    fields = ["id","server_id","total_bill","is_cashed","table_number","is_server","is_completed","memo_notes"]
    success_url = "/"

class OrderListView(ListView):
    model = Order
    template = "order_view.html"
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(OrderListView, self).get_context_data(**kwargs)
        list_order = Order.objects.all()
        paginator = Paginator(list_order, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            list_order = paginator.page(page)
        except PageNotAnInteger:
            list_order = paginator.page(1)
        except EmptyPage:
            list_order = paginator.page(paginator.num_pages)

        context['list_order'] = list_order
        return context

class OrderDetailView(DetailView):
    model = Order
    template = "order_detail.html"

class KitchenOrderView(ListView):
    model = Check
    template = "kitchen_order_view.html"

class MenuItemView(ListView):
    model = Menu_Item
    template = "menu_item_view.html"
