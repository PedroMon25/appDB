import requests

class GetRecord:

    __url = "https://66db3d98f47a05d55be77b70.mockapi.io/api/v1/estudiante"

    def getLastRecord(self):
        try:

            response = requests.get(self.__url)
            response.raise_for_status() # Verifica si hubo un error en la solicitud
            data = response.json()

        # Obtiene el último registro
            if data:
                ultimo_registro = data[-1]
                mostrar_datos(ultimo_registro)
            else:
                resultado_label.config(text="No se encontraron registros.")
        except Exception as e:
            resultado_label.config(text=f"Error: {e}")
