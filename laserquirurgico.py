import time

class LaserQuirurgico:
    def __init__(self):
        self.estado = False
        self.intensidad = 0
        self.tiempo_uso = 0.0
        self.inicio_uso = None

    def encender(self):
        if not self.estado:
            self.estado = True
            self.inicio_uso = time.time()

    def apagar(self):
        if self.estado:
            tiempo_actual = time.time() - self.inicio_uso
            self.tiempo_uso += tiempo_actual
            self.estado = False
            self.inicio_uso = None
    
    def ajustar_intensidad(self, nueva_intensidad):
        if 0 <= nueva_intensidad <= 100:
            self.intensidad = nueva_intensidad
        else:
            raise ValueError("Intensidad fuera del rango seguro (0-100)")
        
    def __str__(self):
        estado_laser = "Encendido" if self.estado else "Apagado"
        return (f"Láser: {estado_laser}, "
                f"Intensidad: {self.intensidad}%, "
                f"Tiempo de uso: {self.tiempo_uso:.2f} segundos")    
    

