from django.shortcuts import render, redirect
from .models import Lead
from django.contrib import messages
from django.core.exceptions import ValidationError

# Create your views here.
def index(request):
    return render(request, 'index.html')

def registerLead(request):
    if request.method == 'POST':
        # Obtén los datos del formulario o crea un objeto MiModelo
        names = request.POST.get('Names')
        email = request.POST.get('Email')
        dni = request.POST.get('DNI')
        phone = request.POST.get('Phone')
        lead = Lead(Names=names, Email=email, DNI=dni, Phone=phone)
        
        try:
            # Valida los campos utilizando full_clean()
            lead.full_clean()
        except ValidationError as e:
            # Captura los mensajes de error y pásalos al contexto de la plantilla
            errores = e.message_dict
            messages.error(request, errores)
            return redirect('/#divMessage')
        else:
            # Si no hay errores de validación, guarda el objeto en la base de datos
            #lead.save()
            messages.success(request, 'Nuestros Asesores se comunicaran con usted!')
    return redirect('/#divMessage')




    # lead = Lead(Names = request.POST['Names'], Email = request.POST['Email'], DNI = request.POST['DNI'], Phone = request.POST['Phone'])
    # lead.save()

    # Names = request.POST['Names']
    # Email = request.POST['Email']
    # DNI = request.POST['DNI']
    # Phone = request.POST['Phone']

    # lead = Lead.objects.create(Names=Names, Email=Email, DNI=DNI, Phone=Phone)
    # messages.success(request, 'Nuestros Asesores se comunicaran con usted!')
    # return redirect('/#divMessage')