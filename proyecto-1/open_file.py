import csv
with open("C:\\Users\\rogarciad\\automation-adoption-training\\prueba1.csv", encoding='latin1') as fichero_csv:
          lector = csv.reader(fichero_csv)
          next(lector, None)
          importe_total = 0
          for linea in lector:
              importe_str = linea[2]
              importe = float(importe_str)
              importe_total = importe_total + importe
          print(importe_total)
          print("Hola mundo!")