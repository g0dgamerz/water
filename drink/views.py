from django.shortcuts import render
from django.views.generic import CreateView
from .models import Infos
from .forms import Info

# Create your views here.
def home(request):
	return render(request, 'drink/home.html')

class CreateMyModelView(CreateView):
    model=Infos
    form_class=Info
    template_name='info.html'

    def get(self,request):
        form=Info
        info=Infos.objects.all()
        print(Infos.user)
        print('fghjk')
        print(Infos.weight)
        return render(request,self.template_name,{'form':form})
 