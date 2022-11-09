def conversor_temperatura(temperatura):
  t = temperatura
  f = (9* c + 160)/5
  return 'A temperatura {}°C equivale a {}°Fahrenheit'.format(t, f)

c = float(input('Digite a temperatura em Celsius para sua conversão: '))
conversor_temperatura(c)