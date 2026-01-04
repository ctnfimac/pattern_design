from abc import ABC, abstractmethod

class ReportValueError(ValueError):
    def __init__(self, message, *args):
        super(ReportValueError, self).__init__(message, *args)

# Interfaz de reportes
class Report(ABC):

    @abstractmethod
    def generate(self):
        pass

# Clases concretas de reportes
class SalesReport(Report):

    def generate(self) -> None:
        print("Generando reporte de ventas")
        

class InventoryReport(Report):

    def generate(self) -> None:
        print("Generando reporte de inventario")


class FinanceReport(Report):

    def generate(self) -> None:
        print("Generando reporte de las Finanzas de la empresa") 


# Clase base de ResportFactory
class ReportFactory(ABC):
    @abstractmethod
    def _create_report(self) -> Report:
        pass

    def generate_report(self) -> None:
        report = self._create_report()
        report.generate()
        

# Clases concretas fabricas de reportes
class SalesReportFactory(ReportFactory):
    def _create_report(self) -> Report:
        return SalesReport()


class InventoryReportFactory(ReportFactory):
    def _create_report(self) -> Report:
        return InventoryReport()


class FinanceReportFactory(ReportFactory):
    def _create_report(self) -> Report:
        return FinanceReport()
    

if __name__ == "__main__":
    report_factory: ReportFactory

    report_selected = "finance"
    # report_selected = "no_existe"

    if(report_selected == "sales"):
        report_factory = SalesReportFactory()
    
    elif(report_selected == "inventory"):
        report_factory = InventoryReportFactory()

    elif(report_selected == "finance"):  
        report_factory = FinanceReportFactory()

    else:
        raise ReportValueError("tipo de reporte inexistente")
    
    report_factory.generate_report()