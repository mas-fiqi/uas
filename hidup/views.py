from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def hom(request):
  template = loader.get_template('hom.html')
  return HttpResponse(template.render())
def comen(request):
  template = loader.get_template('comen.html')
  return HttpResponse(template.render())

def work(request):
  template = loader.get_template('work.html')
  return HttpResponse(template.render())
def contact(request):
  template = loader.get_template('contact.html')
  return HttpResponse(template.render())



# from django.shortcuts import render
# from django.http import HttpResponseForbidden
# from .forms import BeritaForm  

# def index1(request):
#     if request.method == 'POST':
#         form = BeritaForm(request.POST)
#         if form.is_valid():
          
#         else:
#             return HttpResponseForbidden("CSRF verification failed")
#     else:
#         form = BeritaForm()

#     return render(request, 'my_template.html', {'form': form})

# from django.shortcuts import render
# from .forms import ContohForm

# def contoh_view(request):
#     if request.method == 'POST':
#         form = ContohForm(request.POST)
#         if form.is_valid():
#             # Lakukan sesuatu dengan data formulir yang valid
#             # Contoh: simpan ke database, kirim email, dll.
#     else:
#         form = ContohForm()

#     return render(request, 'contoh_template.html', {'form': form})
