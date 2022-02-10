from django.shortcuts import render
from .models import *

# Create your views here.


def qidirish(request):
    if request.method == 'POST':
        soz = request.POST['q_soz']
        soz1 = Word.objects.filter(soz=soz)
        if len(soz1) > 0:
            b = Check.objects.filter(soz_id=soz1[0])
            return render(request, 'result.html', {'soz':soz1[0], 'n_soz':b})
        else:
            b = Check.objects.filter(n_soz=soz)
            if len(b) > 0:
                t_soz = Word.objects.filter(id=b[0].soz_id.id)
                b = Check.objects.filter(soz_id=t_soz[0])
                return render(request, 'result.html', {'soz': t_soz[0], 'n_soz': b})
            else:
                return render(request, 'result.html', {'soz':"Bizning bazada bumday so`z yo`q"})
    return render(request, 'result.html')