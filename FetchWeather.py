__author__ = 'Johannes'
import time
import pywapi
import string

#Code of Schnaittach

# retrieve data from weather.com
def Weather():
                global WetterIcon
                global TMax
                global TMin
                global feelsLikeTemp
                #weatherDotComLocationCode = 'GMXX1602'
                weather_com_result = pywapi.get_weather_from_weather_com('GMXX1602')
                # extract current data for today
                #today = weather_com_result['forecasts'][0]['day_of_week'][0:3] + " " \
                #    + weather_com_result['forecasts'][0]['date'][4:] + " " \
                #   + weather_com_result['forecasts'][0]['date'][:3]
                TMax = weather_com_result['forecasts'][0]['high'][0:3] + u'\N{DEGREE SIGN}' + "C"
                TMin = weather_com_result['forecasts'][0]['low'][0:3] + u'\N{DEGREE SIGN}' + "C"
                #windSpeed = int(weather_com_result['current_conditions']['wind']['speed'])
                #currWind = "{:.0f}kph ".format(windSpeed) + weather_com_result['current_conditions']['wind']['text']
                #currTemp = weather_com_result['current_conditions']['temperature'] + u'\N{DEGREE SIGN}' + "C"
                feelsLikeTemp = weather_com_result['current_conditions']['feels_like'] + u'\N{DEGREE SIGN}' + "C"
                WetterIcon = weather_com_result['current_conditions']['icon']
                #currPress = weather_com_result['current_conditions']['barometer']['reading'][:-3] + "mb"
                #uv = "UV {}".format(weather_com_result['current_conditions']['uv']['text'])
                #humid = "Hum {}%".format(weather_com_result['current_conditions']['humidity'])
                #print(today)
                #print(windSpeed)
                #print(currWind)
                #print(uv)
                #print(humid)
                #print(currTemp)
                #print(feelsLikeTemp)
                #print(TMax)
                #print(TMin)
                #print(WetterIcon)

