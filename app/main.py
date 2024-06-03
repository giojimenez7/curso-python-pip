import utils
import read_csv
import charts
import pandas as pd

def run():
  '''
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda item: item['Continent'] == 'South America', data))

  countries = [x['Country/Territory'] for x in data]
  percentages = [x['World Population Percentage'] for x in data]
  charts.generate_pie_chart(countries, percentages)
  '''

  df = pd.read_csv('data.csv')
  df = df[df['Continent'] == 'Africa']

  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values
  charts.generate_pie_chart(countries, percentages)

  country = input('Type Country => ')
  print(country)
  
  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)

if __name__ == '__main__':
  run()