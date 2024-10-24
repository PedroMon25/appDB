import requests

class GetRecord:

    __url = "https://66db3d98f47a05d55be77b70.mockapi.io/api/v1/estudiante"

    def getLastRecord(self):
        try:
            response = requests.get(self.__url)
            response.raise_for_status()  # Verifica si hubo un error en la solicitud
            data = response.json()

            # Obtiene el último registro
            if data:
                ultimo_registro = data[-1]
                print(f"Tipo de último registro: {type(ultimo_registro)}")
                print(f"Contenido de último registro: {ultimo_registro}")
                self.mostrar_datos(ultimo_registro)
            else:
                print("No se encontraron registros.")
        except Exception as e:
            print(f"Error: {e}")  # Mostrar error en consola

    def mostrar_datos(self, registro):
        # Si es un diccionario, lo mostramos
        if isinstance(registro, dict):
            print("Último Registro:")
            for clave, valor in registro.items():
                print(f"{clave}: {valor}")
        else:
            print("Error: El registro no es un diccionario válido.")

# Uso del código:
record = GetRecord()
record.getLastRecord()
