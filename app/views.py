from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render,redirect
from django.db import connection
from django.contrib import messages


# Create your views here.
def listar_alumno(request):
    # abrir conexion a la BD
    cursor=connection.cursor()
    cursor.execute('call sp_obtener_alumnos()')
    alumnos=cursor.fetchall()    
    
    return render(request,'app/index.html',{'alumnos':alumnos})

def insertar_alumno(request):
    if request.method == 'POST':
        # Obtener datos del formulario
        nombre_apellido = request.POST.get('nombre_apellido')
        nombre_curso = request.POST.get('nombre_curso')
        nota_curso = request.POST.get('nota_curso')
        # estado = request.POST.get('estado')  # El estado se pone automático       

        # Llamar al procedimiento almacenado para insertar alumno
        cursor=connection.cursor()
        cursor.execute('call sp_crear_alumno(%s, %s, %s)', [nombre_apellido, nombre_curso, nota_curso])
        
        messages.success(request, 'Alumno insertado exitosamente.')

        return redirect('listar_alumno')

    return render(request,'app/add.html')

def editar_alumno(request, id_alumno):
    if request.method == 'POST':
        # Obtener datos del formulario
        nombre_apellido = request.POST.get('nombre_apellido')
        nombre_curso = request.POST.get('nombre_curso')
        nota_curso = request.POST.get('nota_curso')
        # estado = request.POST.get('estado')  # El estado se pone automático 

        cursor = connection.cursor()
        cursor.execute('call sp_actualizar_alumno(%s, %s, %s, %s)', [id_alumno, nombre_apellido, nombre_curso, nota_curso])

        messages.success(request, 'Alumno actualizado exitosamente.')

        return redirect('listar_alumno')  # Redirigir al usuario a la página de inicio    

    else:
        cursor = connection.cursor()
        cursor.execute('call sp_obtener_alumno_por_id(%s)', [id_alumno])
        alumno = cursor.fetchone()        

        return render(request, 'app/edit.html', {'alumno': alumno})



def eliminar_alumno(request, id_alumno):
    # Llamar al procedimiento almacenado para eliminar alumno
    cursor=connection.cursor()
    cursor.execute('call sp_eliminar_alumno(%s)',(id_alumno,))
    cursor=connection.cursor()
    cursor.execute('call sp_obtener_alumnos()')
    alumnos = cursor.fetchall()

    return render(request,'app/index.html',{'alumnos': alumnos}) 