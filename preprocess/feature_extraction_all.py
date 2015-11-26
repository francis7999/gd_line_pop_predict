from preprocess.ultimate_feature_extraction import *
import os
parent_path = os.path.dirname(os.getcwd())
data_path = os.path.join(parent_path, 'train_data')
weather_workday = os.path.join(data_path, 'workday_weather.txt')
weather_restday = os.path.join(data_path, 'restday_weather.txt')
weather_holiday = os.path.join(data_path, 'holiday_weather.txt')
line6_stat = os.path.join(data_path, 'line6_stat.txt')
line11_stat = os.path.join(data_path, 'line11_stat.txt')
featureMat_workday_line6 = os.path.join(data_path, 'featureMat_workday_line6.txt')
featureMat_workday_line11 = os.path.join(data_path, 'featureMat_workday_line11.txt')
featureMat_restday_line6 = os.path.join(data_path, 'featureMat_restday_line6.txt')
featureMat_restday_line11 = os.path.join(data_path, 'featureMat_restday_line11.txt')
featureMat_holiday_line6 = os.path.join(data_path, 'featureMat_holiday_line6.txt')
featureMat_holiday_line11 = os.path.join(data_path, 'featureMat_holiday_line11.txt')
ultimate_feature_extraction(weather_workday, line6_stat, featureMat_workday_line6)
ultimate_feature_extraction(weather_workday, line11_stat, featureMat_workday_line11)
ultimate_feature_extraction(weather_restday, line6_stat, featureMat_restday_line6)
ultimate_feature_extraction(weather_restday, line11_stat, featureMat_restday_line11)
ultimate_feature_extraction(weather_holiday, line6_stat, featureMat_holiday_line6)
ultimate_feature_extraction(weather_holiday, line11_stat, featureMat_holiday_line11)