from clases.builder_form.builder import Builder
from clases.builder_form.form_item import FormItem

class LoginBuilder(Builder):
    """Construye un formulario de login con los campos email y password"""
    
    def __init__(self):
        self.form = []

    def add_email_field(self):
        self.form.append(FormItem("Email", "email"))
        return self
    
    def add_password_field(self):
        self.form.append(FormItem("Contraseña", "password"))
        return self
    
    def build(self):
        items = [ {"label": item.label , "input_type": item.input_type} for item in self.form]
        return items 

    """campos no utilizados"""
    def add_apellido_field(self):
        pass

    def add_password2_field(self):
        pass

    def add_nombre_field(self):
        pass

    def add_dni_field(self):
        pass