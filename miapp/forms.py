from django import forms
from .models import Usuario,Juego

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'usuario', 'correo', 'password', 'fecha_nacimiento', 'direccion', 'rol', 'genero', 'region']
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'usuario', 'correo', 'fecha_nacimiento', 'direccion', 'genero']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'usuario': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'value': 'yyyy-mm-dd'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-select'}),
        }

class CambiarContrasenaForm(forms.Form):
    contrasena_actual = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Contraseña actual"
    )
    nueva_contrasena = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Nueva contraseña"
    )
    confirmar_contrasena = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Confirmar nueva contraseña"
    )

class JuegoForm(forms.ModelForm):
    class Meta:
        model = Juego
        fields = ['nombre', 'categoria', 'precio', 'descripcion', 'imagen']  # Añadir imagen
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }