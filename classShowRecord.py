

class ShowRecord:

    __textoRegistro = None


    def mostrar_datos(self, registro):
        self.__textoRegistro = registro



        resultado_label.config(text=self.__textoRegistro)
