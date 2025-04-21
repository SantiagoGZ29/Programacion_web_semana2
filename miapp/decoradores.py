from functools import wraps
from django.shortcuts import redirect
from django.urls import reverse
from .models import Usuario

def usuario_logueado_requerido(vista_func):
    @wraps(vista_func)
    def _wrapped_view(request, *args, **kwargs):
        if 'usuario_id' not in request.session:
            # Redirige al login y le pasa la URL actual como 'next'
            login_url = reverse('login_usuario')
            return redirect(f"{login_url}?next={request.path}")
        return vista_func(request, *args, **kwargs)
    return _wrapped_view

def admin_requerido(vista_func):
    @wraps(vista_func)
    def _wrapped_view(request, *args, **kwargs):
        usuario_id = request.session.get('usuario_id')

        if not usuario_id:
            login_url = reverse('login_usuario')
            return redirect(f"{login_url}?next={request.path}")

        try:
            usuario = Usuario.objects.get(id=usuario_id)
            if usuario.rol.rol_usuario != 'administrador':
                return redirect('inicio')  # Asegúrate de tener esta vista o URL
        except Usuario.DoesNotExist:
            login_url = reverse('login_usuario')
            return redirect(f"{login_url}?next={request.path}")

        return vista_func(request, *args, **kwargs)
    return _wrapped_view