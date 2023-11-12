def detectar_alexa(texto):
  palabras = texto.split()
  conteo = palabras.count('alexa'.lower())

  if conteo > 1:
    return "Porfavor solo di alexa una vez  dentro de tu texto"
  elif conteo == 1:
        return "Exclenete, dijiste mi nombre!"
  else:
    return "Alexa no fue detactada dentro del texto que acabas de escribir, Porfavor vuelve a escribir un texto que si diga Alexa"
    

entrada = input("Ingresa tu texto aquí ")
resultado = detectar_alexa(entrada.lower())
print(resultado)
