import time

class LaserQuirurgico:
    def __init__(self):
        self.__estado = False
        self.__intensidad = 0
        self.__tiempo_uso = 0.0
        self.__inicio_uso = None

    @property
    def estado(self):
        return self.__estado
    
    @estado.setter
    def estado(self, valor):
        if not isinstance(valor, bool):
            raise ValueError("Estado debe ser booleano")
        self.__estado = valor
    
    @property
    def intensidad(self):
        return self.__intensidad

    @intensidad.setter
    def intensidad(self, valor):
        if not(0 <= valor <= 100):
            raise ValueError("Intensidad fuera del rango seguro (0-100)")
        self.__intensidad = valor

    @property
    def tiempo_uso(self):
        return self.__tiempo_uso  

    def encender(self):
        if not self.__estado:
            self.__estado = True
            self.__inicio_uso = time.time()

    def apagar(self):
        if self.__estado:
            tiempo_actual = time.time() - self.__inicio_uso
            self.__tiempo_uso += tiempo_actual
            self.__estado = False
            self.__inicio_uso = None
    
    def ajustar_intensidad(self, nueva_intensidad):
        self.intensidad = nueva_intensidad
        
    def __str__(self):
        estado_laser = "Encendido" if self.__estado else "Apagado"
        return (f"Láser: {estado_laser}, "
                f"Intensidad: {self.__intensidad}%, "
                f"Tiempo de uso: {self.__tiempo_uso:.2f} segundos")    


