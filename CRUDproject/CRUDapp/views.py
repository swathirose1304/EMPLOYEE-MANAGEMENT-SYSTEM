from django.shortcuts import render, redirect
from CRUDapp.models import EmpModel
from django.contrib import messages
from CRUDapp.forms import Empforms

def showemp(request):
    showall = EmpModel.objects.all()
    return render(request, 'index.html', {'data':showall})

def insertEmp(request):
    if request.method == 'POST':
        if request.POST.get('empname') and request.POST.get('email') and request.POST.get('domain') and request.POST.get('salary') and request.POST.get('gender'):
            save_record = EmpModel()
            save_record.empname = request.POST.get('empname')
            save_record.email = request.POST.get('email')
            save_record.domain = request.POST.get('domain')
            save_record.salary = request.POST.get('salary')
            save_record.gender = request.POST.get('gender')
            save_record.save()

            messages.success(request, 'Employee ' +save_record.empname+ ' is saved successfully!')

            return redirect('insertEmp')
        
        else:
            messages.error(request, 'Please fill in all the required fields.')
            return redirect('insertEmp')
    
    return render(request, 'insert.html')

def editEmp(request,id):
    editEmpObj = EmpModel.objects.get(id=id)
    return render(request, 'edit.html', {'EmpModel':editEmpObj})

def updateEmp(request,id):
    updateEmpObj = EmpModel.objects.get(id=id)
    form = Empforms(request.POST, instance=updateEmpObj)
    if form.is_valid():
        form.save()
        messages.success(request, 'Details updated successfully!')
        return render(request, 'edit.html', {'EmpModel':updateEmpObj})
    
def delEmp(request,id):
    delEmpObj = EmpModel.objects.get(id=id)
    delEmpObj.delete()
    showdata = EmpModel.objects.all()
    return render(request, 'index.html', {'data':showdata})

