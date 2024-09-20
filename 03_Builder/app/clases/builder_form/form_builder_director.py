from clases.builder_form.builder import Builder

class FormBuilderDirector:

    def __init__(self, builder: Builder) -> None:
        self.builder = builder

    def contruct_login(self):
        self.builder.add_email_field().add_password_field()

    def construct_registro_de_usuario(self):
        self.builder.\
        add_email_field().\
        add_dni_field().\
        add_nombre_field().\
        add_apellido_field().\
        add_password_field().\
        add_password2_field()

    def construct_recuperar_contrasenia(self):
        self.builder.add_password_field()