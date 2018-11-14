from weather import Weather, Unit
import datetime
import click

@click.command()
@click.option('--city', 'city_to_check_weather', help='Name of the city')
@click.option('--forecast', default='TODAY')
@click.option('--scale', type=click.Choice(['c', 'f']), default='c',  help='Temperature unit')



#"""
#`python cli.py --city dublin --forecast TODAY -c`

# Will print the following to screen:

#�The weather in Dublin today is Cloudy with temperatures trailing from 5-10 celsius.�
#"""
def get_scale_info(scale):
    if scale == 'c':
        unit = Unit.CELSIUS
        scale_name = 'celcius'
    elif scale == 'f':
        unit = Unit.FAHRENHEIT
        scale_name = 'fahrenheit'
        return unit, scale_name

def print_weather_by_city(cityforcasts_list, scale_name):
    print('The weather in ' + city + 'today is ' +  forecasts_list[0].text + 'with temperatures trailing from' 
          + forecasts_list[0].low + '-' + forecasts_list[0].low + ' ' + scale_name)
    pass

def main(city, forecast, scale):
    
    unit, scale_name = get_scale_info(scale)
    weather = Weather(unit)
    city_weather_info = weather.lookup_by_location(city)
    forecasts_list = city_weather_info.forecast
    print_weather_by_city(city, forecasts_list, scale)
    
    #print(city_weather_info.condition.text)





if __name__ == '__main__':
    main()