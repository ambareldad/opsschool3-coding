from weather import Weather, Unit
import datetime
import click


def get_scale_info(scale):
    if scale == 'c':
        unit = Unit.CELSIUS
        scale_name = 'celcius'
    elif scale == 'f':
        unit = Unit.FAHRENHEIT
        scale_name = 'fahrenheit'
    return unit, scale_name


def forecast_length(forecast):
    split_forecast = forecast.split("+")
    if len(split_forecast) == 1:
        forecast_len = 0
    else:
        forecast_len = int(split_forecast[1])
    return forecast_len


def print_weather_by_city(city, forcasts_list, scale_name, forecast_len = 0):
    print('The weather in {0} today is {1} with temperatures trailing from {2} - {3} {4}'
          .format(city, forcasts_list[0].text, forcasts_list[0].low, forcasts_list[0].high, scale_name))

    if forecast_len > 0:
        print('Forecast for the next {0} days:'.format(forecast_len))
        for i in range(1,forecast_len + 1):
            print('{0} {1} with temperatures trailing from {2} - {3} {4}'
                  .format(forcasts_list[i].date, forcasts_list[i].text, forcasts_list[i].low, forcasts_list[i].high, scale_name))


@click.command()
@click.option('--city', help='Name of the city')
@click.option('--forecast', default='TODAY', help='TODAY or TODAY+n for future forecast, where n = [1-9]',show_default=True)
@click.option('--scale', type=click.Choice(['c', 'f']), default='c', help='Temperature unit')

def main(city, forecast, scale):
    unit, scale_name = get_scale_info(scale)
    weather = Weather(unit)
    city_weather_info = weather.lookup_by_location(city)
    forecasts_list = city_weather_info.forecast
    forecast_len = forecast_length(forecast)
    print_weather_by_city(city, forecasts_list, scale_name, forecast_len)

if __name__ == '__main__':
    main()