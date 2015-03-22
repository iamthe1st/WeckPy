__author__ = 'Simone'
import FetchWeather
import time
import uhr

FetchWeather.Weather()
print(FetchWeather.WetterIcon)
print(FetchWeather.feelsLikeTemp)
print(FetchWeather.TMax)
print(FetchWeather.TMin)


#refresh Display
lt = time.localtime()
brightness = 50
WakeTime = time.strftime("  %H:%M ", lt)
uhr.DisplayWatch(brightness, FetchWeather.Tmin, FetchWeather.Tmax, FetchWeather.Tfeel, WakeTime, FetchWeather.WetterIcon)
print('fertig')