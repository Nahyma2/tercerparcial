def simulacion_sensor_temperatura(lecturas):
  fuera_rango = 0

  for _ in range(lecturas):
      temperatura_raw = float(input("Ingresa una la ectura de temperatura en Celsius: "))
      if not (10 <= temperatura_raw <= 40):
          fuera_rango += 1
          print("Advertencia: Temperatura fuera del rango esperado!", end=" ")

  porcentaje_error = (fuera_rango / lecturas) * 100
  print("\nResumen:")
  print("Total de lecturas:", lecturas, end=" ")
  print("Lecturas fuera del rango esperado de 10 a 40 grados Celsius:", fuera_rango, end=" ")
  print("Porcentaje de error:", porcentaje_error, "%")

lecturas = int(input("Ingresa el número de lecturas de temperatura: "))
simulacion_sensor_temperatura(lecturas)
      
