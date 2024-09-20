from clases.builder_form.builder import Builder
from clases.builder_form.form_item import FormItem

class RegisterBuilder(Builder):
    """Construye un formulario de Registro de Usuario con los campos 
    email, dni, nombre, apellido, password, password2,
    """
    
    def __init__(self):
        self.form = []

    def add_email_field(self):
        self.form.append(FormItem("Email", "email"))
        return self
    
    def add_nombre_field(self):
        self.form.append(FormItem("Nombre", "text"))
        return self

    def add_apellido_field(self):
        self.form.append(FormItem("Apellido", "text"))
        return self

    def add_dni_field(self):
        self.form.append(FormItem("Dni", "text"))
        return self

    def add_password_field(self):
        self.form.append(FormItem("Contraseña", "password"))
        return self

    def add_password2_field(self):
        self.form.append(FormItem("Contraseña2", "password"))
        return self
    
    def build(self):
        items = [ {"label": item.label , "input_type": item.input_type} for item in self.form]
        return items 

    
