import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)  # Lee la primera fila manualmente
    data = []
    for row in reader:
      iterable = zip(header, row) # une dos array, header y row en una tupla
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data
  
if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data[0])