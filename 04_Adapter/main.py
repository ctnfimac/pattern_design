
#   ! Patrón Adapter
#    Permite que objetos con interfaces incompatibles trabajen juntos, también es muy
#    util para utilizar librerías de terceros en nuestra aplicación sin depender
#    directamente de ellas.
 
#    Es útil cuando se quiere reutilizar una clase que no tiene la interfaz que
#    necesitamos o cuando queremos crear una capa de abstracción para una librería
#    de terceros.
 
#   https://refactoring.guru/es/design-patterns/adapter
from abc import ABC, abstractmethod

# 1. Interfaz PaymentProcessor
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(amount: int):
        pass


# 2. Clases de Servicios de Pago Externos
# Estas clases simulan los servicios externos de PayPal, Stripe y MercadoPago
class PayPalService:
    def send_payment(self, amount: int):
        print(f'Procesando pago de $${amount} con PayPal')


class StripeService:
    def make_charge(self, amount: int):
        print(f'Procesando pago de $${amount} con Stripe')
  

class MercadoPagoService:
    def pay(self, amount: int):
        print(f'Procesando pago de $${amount} con MercadoPago')


# 3. Clases Adaptadoras

# Adaptador para PayPal
class PayPalAdapter(PaymentProcessor):

    def __init__(self):
        self._paypal_service = PayPalService()
    
    # Implemento la interfaz PaymentProcessor
    def process_payment(self, amount: int):
        self._paypal_service.send_payment(amount)


# Adaptador para Stripe
class StripeAdapter(PaymentProcessor):

    def __init__(self):
        self._stripe_service = StripeService()

    # Implemento la interfaz PaymentProcessor
    def process_payment(self, amount: int):
        self._stripe_service.make_charge(amount)


# Adaptador para MercadoPago
class MercadoPagoAdapter(PaymentProcessor):

    def __init__(self):
        self._mercado_pago_service = MercadoPagoService()


    #Implemento la interfaz PaymentProcessor
    def process_payment(self, amount: int):
        self._mercado_pago_service.pay(amount)


# 4. Código Cliente para probar el Adapter
def main():
    PAYMENT_AMOUNT = 100

    # Agrego los adaptadores para los servicios de pago
    paypalProcessor: PaymentProcessor = PayPalAdapter()
    stripeProcessor: PaymentProcessor = StripeAdapter()
    mercadoPagoProcessor: PaymentProcessor = MercadoPagoAdapter()

    # Procesar pagos con los diferentes servicios
    # Los 3 procesadores de pago trabajan exactamente igual después de adaptaros
    print('Usando PayPal:')
    paypalProcessor.process_payment(PAYMENT_AMOUNT)

    print('\nUsando Stripe:')
    stripeProcessor.process_payment(PAYMENT_AMOUNT)

    print('\nUsando MercadoPago:')
    mercadoPagoProcessor.process_payment(PAYMENT_AMOUNT)


if __name__ == "__main__":
    main()