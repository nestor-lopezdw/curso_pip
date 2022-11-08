import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda item: item['Continent'] == 'South America', data))
  
  countries = utils.get_country(data)
  porcentaje = utils.get_world_population_percentage(data)
  pais = utils.get_country(data)

  if len(porcentaje) > 0:
    charts.generate_pie_chart(pais, porcentaje)

  country = input('Type Country => ')
  print(country)
 
  result = utils.population_by_country(data, country)
  if len(result) > 0:
    country = result[0]
    print(country)
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)
 
  
if __name__ == '__main__':
  run()