import requests
import json

def locate_location_by_ip(url):
    location_from_url = requests.get(url)
    dictionary_from_json = location_from_url.json()
    city_from_url = dictionary_from_json['city']
    country_from_url = dictionary_from_json['country']
    return(city_from_url + ',' + country_from_url)

def check_weather_by_location(location,url,parameter):
    weather_from_url = requests.get(url,params=parameter)
    return (weather_from_url)


def print_to_text_file(json_weather, file_name):
    new_file_name = file_name + '.txt'
    with open(new_file_name, 'w') as new_file:
        json.dump(json_weather, new_file)
        new_file.close()


def main():
    
    url_location_by_ip = 'http://ip-api.com/json'
    url_weather_by_location = 'http://api.openweathermap.org/data/2.5/weather'

    location_list = [("Bagdad", "Iraq"),("Moscow","Russia"),("Berlin","Germany"),("Amsterdam","Netherlands"),("Jerusalem","Israel"),
                     ("Lonson","Uk"),("Paris","France"),("New York","USA"),("Tel Aviv","Israel"),("kiryat ono","Israel")]

    location = locate_location_by_ip(url_location_by_ip)
    parameters_for_weather ={'q':location, 'appid':'2c3c766e130f319e940593c1b97e1fb2'}
    weather = check_weather_by_location(location,url_weather_by_location, parameters_for_weather)


    print(weather.url)
    json_get_weather_info = requests.get(weather.url).json()
    print(weather)
    print_to_text_file(json_get_weather_info, 'new_file')
    
    
    for (city, country) in location_list:
        print(city, country)
        weather = check_weather_by_location(city +  country,url_weather_by_location, parameters_for_weather)
        temperature = json_get_weather_info['main']['temp']
        print('The weather in ' + city + ', ' + country + ' is ' + str(temperature) + ' degrees')
                
    #The weather in <city>, <country>(full country name) is XX degrees


if __name__ == '__main__':
    main()