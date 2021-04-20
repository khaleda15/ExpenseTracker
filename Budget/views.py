from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from .models import Asset,Cost
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .forms import LoginForm,SignUpForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy


class Home(LoginRequiredMixin,View):
    login_url = '/login/'
    
    def get(self,request):
        context = {}
        costobj = Cost.objects.filter(user=request.user).order_by('asset')
        assetobj = Asset.objects.filter(user=request.user).order_by('purpose')
        context['costs'] = costobj
        context['assets'] = assetobj


        asub = {}
        for costs in costobj:
            sub = costs.amount
            print('All Asset Data')
            print(costs.asset.id,end=' ')
            print(costs.asset.purpose,end=' ')
            print(costs.asset.totalamount,end=' ')
            print(costs.asset.date)
            print('All Cost Data')
            print(costs.id,end=' ')
            print(costs.description,end=' ')
            print(costs.amount)
            print('===================')
            
            if costs.asset.id in asub.keys():     
                asub[costs.asset.id] = asub[costs.asset.id]-costs.amount
            else:
                asub[costs.asset.id] = costs.asset.totalamount
                asub[costs.asset.id] = asub[costs.asset.id]-costs.amount
            print('Now avialable',asub[costs.asset.id])


        print('After Substration:',asub)

        context['ailables'] = asub


        # here i create all assets unique dictonary
        purposes = {}
        for assetobjs in assetobj:
            purposes[assetobjs.purpose] = assetobjs.totalamount

        print("My assetobj:",purposes)
        context['purposes'] = purposes



        return render(request,'index.html',context)


class AddCost(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    model = Cost
    fields = ['asset','description','amount']
    template_name = 'addcost.html'
    success_url = '/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_queryset(self):
        return [(Cost.objects.filter(user = self.request.user)),(Asset.objects.filter(user = self.request.user))]


class UpdateCost(LoginRequiredMixin,UpdateView):
    model = Cost
    fields = ['asset','description','amount']
    template_name = 'updatecost.html'
    success_url = '/'
    login_url = '/login/'
    def get_queryset(self):
        return Cost.objects.filter(user = self.request.user)

class DeleteCost(LoginRequiredMixin,DeleteView):
    model = Cost
    context_object_name = 'cost'
    template_name = 'deletecost.html'
    success_url = '/'

class AddAsset(LoginRequiredMixin,CreateView):
    model = Asset
    fields = ['purpose','totalamount']
    template_name = 'addasset.html'
    success_url = '/'
    login_url = '/login/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class DeleteAsset(LoginRequiredMixin,DeleteView):
    model = Asset
    context_object_name = 'asset'    
    template_name = 'deleteasset.html'
    success_url = '/'
    login_url = '/login/'


class Userlogin(View):
    def get(self,request):
        if not request.user.is_authenticated:
            form = LoginForm()
            return render(request,'login.html',{'form':form})
        else:
            return redirect('/')
    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/?next=%s' % request.path)
            else:
                return redirect(('login'))
        return render(request,'login.html',{'form':form})


@login_required(login_url='login')
def userlogout(request):
    logout(request)
    return redirect('login')


class UserSignUp(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
