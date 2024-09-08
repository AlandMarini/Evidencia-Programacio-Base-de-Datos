import unittest
import time
from laserquirurgico import LaserQuirurgico


class TestLaserQuirurgico(unittest.TestCase):

    def setUp(self):
        self.laser = LaserQuirurgico()
    
    def test_encender_laser(self):
        self.laser.encender()
        self.assertTrue(self.laser.estado, "El láser debería estar encendido")
        self.assertIsNotNone(self.laser._LaserQuirurgico__inicio_uso, "El tiempo de inicio no debería ser None")
    
    def test_encender_laser_doble(self):
        self.laser.encender()
        inicio_uso_inicial = self.laser._LaserQuirurgico__inicio_uso
        time.sleep(0.1)  
        self.laser.encender()
        self.assertEqual(self.laser._LaserQuirurgico__inicio_uso, inicio_uso_inicial, "El tiempo de inicio debería permanecer igual si el láser ya está encendido")
    
    def test_apagar_laser(self):
        self.laser.encender()
        time.sleep(1)  
        self.laser.apagar()
        self.assertFalse(self.laser.estado, "El láser debería estar apagado")
        self.assertGreater(self.laser.tiempo_uso, 0, "El tiempo de uso debería ser mayor que 0")
    
    def test_ajustar_intensidad(self):
        self.laser.ajustar_intensidad(50)
        self.assertEqual(self.laser.intensidad, 50, "La intensidad debería ser 50")
        with self.assertRaises(ValueError):
            self.laser.ajustar_intensidad(150) 
    
    def test_intensidad_fuera_de_rango(self):
        with self.assertRaises(ValueError):
            self.laser.intensidad = 150 

    def test_string_representation(self):
        self.laser.encender()
        self.laser.ajustar_intensidad(75)
        time.sleep(1)
        self.laser.apagar()
        expected_str = f"Láser: Apagado, Intensidad: 75%, Tiempo de uso: {self.laser.tiempo_uso:.2f} segundos"
        self.assertEqual(str(self.laser), expected_str, "La representación en cadena no es correcta")
    
    def test_tiempo_uso_acumulado(self):
        self.laser.encender()
        time.sleep(1)
        self.laser.apagar()
        tiempo_uso_primero = self.laser.tiempo_uso
        self.laser.encender()
        time.sleep(1)
        self.laser.apagar()
        self.assertGreater(self.laser.tiempo_uso, tiempo_uso_primero, "El tiempo de uso debería acumularse.")

    def test_apagar_sin_encender(self):
        self.laser.apagar()
        self.assertFalse(self.laser.estado, "El láser debería seguir apagado si nunca fue encendido.")
        self.assertEqual(self.laser.tiempo_uso, 0, "El tiempo de uso debería ser 0 si el láser nunca fue encendido.")

    def test_intensidad_limite(self):
        self.laser.ajustar_intensidad(0)
        self.assertEqual(self.laser.intensidad, 0, "La intensidad debería ser 0")
        self.laser.ajustar_intensidad(100)
        self.assertEqual(self.laser.intensidad, 100, "La intensidad debería ser 100")

    def test_ajustar_intensidad_apagado(self):
        self.laser.ajustar_intensidad(30)
        self.assertEqual(self.laser.intensidad, 30, "Debería poder ajustar la intensidad mientras el láser está apagado.")

    def test_encender_apagar_rapido(self):
        self.laser.encender()
        time.sleep(0.1)
        self.laser.apagar()
        tiempo_uso_rapido = self.laser.tiempo_uso
        self.assertGreater(tiempo_uso_rapido, 0, "El tiempo de uso debería ser mayor que 0 con un encendido rápido.")

    def test_multiples_encendidos_apagados(self):
        self.laser.encender()
        time.sleep(0.5)
        self.laser.apagar()
        tiempo_uso_primero = self.laser.tiempo_uso

        self.laser.encender()
        time.sleep(0.5)
        self.laser.apagar()
        tiempo_uso_segundo = self.laser.tiempo_uso

        self.assertGreater(tiempo_uso_segundo, tiempo_uso_primero, "El tiempo de uso debería acumularse tras múltiples encendidos.")

    def test_reiniciar_tiempo_uso(self):
        self.laser.encender()
        time.sleep(0.5)
        self.laser.apagar()
        tiempo_uso_inicial = self.laser.tiempo_uso

        self.laser.encender()
        time.sleep(0.5)
        self.laser.apagar()
        tiempo_uso_total = self.laser.tiempo_uso

        self.assertGreater(tiempo_uso_total, tiempo_uso_inicial, "El tiempo de uso debería seguir acumulándose en lugar de reiniciarse.")

    def test_limite_superior_inferior_intensidad(self):
        self.laser.ajustar_intensidad(0)
        self.assertEqual(self.laser.intensidad, 0, "La intensidad debería poder ajustarse a 0.")

        self.laser.ajustar_intensidad(100)
        self.assertEqual(self.laser.intensidad, 100, "La intensidad debería poder ajustarse a 100.")


    def test_mantener_intensidad_al_apagar(self):
        self.laser.ajustar_intensidad(75)
        self.laser.encender()
        self.laser.apagar()
        self.assertEqual(self.laser.intensidad, 75, "La intensidad debería mantenerse al apagar el láser.")

    def test_string_representation_encendido(self):
        self.laser.encender()
        self.laser.ajustar_intensidad(80)
        expected_str = f"Láser: Encendido, Intensidad: 80%, Tiempo de uso: {self.laser.tiempo_uso:.2f} segundos"
        self.assertIn("Encendido", str(self.laser), "Debería indicar que el láser está encendido.")
        self.assertIn("80%", str(self.laser), "Debería mostrar la intensidad ajustada.")

if __name__ == "__main__":
    unittest.main()