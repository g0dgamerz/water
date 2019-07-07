from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import CreateView,ListView,View
from .models import Infos,Water
from .forms import Info,Incre
from django.http.response import HttpResponse, Http404, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model


User= get_user_model()

# Create your views here.
def home(request):
	return render(request, 'drink/home.html')

def saveinfo(request):
    if request.method == 'POST':
        form= Info(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.user = request.user
            new_topic.save()
            return HttpResponse('ok man you data have been processed')
    else:
        form=Info()
        args={'form':form}
        return render(request,'info.html',args)

# class CreateMyModelView(CreateView):
#     model=Infos
#     form_class=Info
#     template_name='info.html'

#     def get(self,request):
#         form=Info
#         info=Infos.objects.all()
#         print(Infos.user)
#         print('fghjk')
#         print(Infos.weight)
#         return render(request,self.template_name,{'form':form})

#     def post(self, request, *args, **kwargs):
#         form = Info(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('ok man you data have been processed')

def incre(request):
    if request.method == 'POST':
        form = Incre(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.accountholder = request.user
            new.save()
            glass=Water.objects.all()
            # for glas in glass:
            #     glas.noofglass += 1
            #     glas.save()
            return redirect('/history')
    else:
        form=Incre()
        args={'form':form}
        return render(request,'addwater.html',args)

def list1(request):
    user=request.user
    water=Water.objects.filter(accountholder=user)
    objectlist = Infos.objects.all()


    context={
    'water':water,
    'objectl':objectlist,  
    }
    
    return render(request,'list.html',context)


# class Indexview(ListView):
    
#     template_name="list.html"

#     def get_queryset(self):
#         user = self.request.user
#         return Water.objects.filter(accountholder=user)
    

#     def get_context_data(self, **kwargs):          
#         context = super().get_context_data(**kwargs)                     
#         new_context_entry = 7
#         user=self.request.user
#         water = Water.objects.filter(accountholder=user).order_by('Water__date').values('accountholder','noofglass')
#         print('startdebug')
#         # for wa in water:
#         # print(water.noofglass)
            
#         print('stopdebug')
#         context["new_context_entry"] = new_context_entry
#         return context


class HomeView(View):
    def get(self,request, *args, **kwargs):
        return render(request,'charts.html')

  
def get_data(request, *args, **kwargs):
    data={
        'sales':100,
        'customer':10,
    }
    return JsonResponse(data)


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        data={
        'sales':100,
        'customer':10,
        "users": User.objects.all().count()
        }
        return Response(data)