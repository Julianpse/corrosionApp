from datetime import datetime
from datetime import timedelta
from math import floor

def days_between(d1,d2):
    return abs((d2-d1).days)/365.25


def yrs_til_tmin(readings,dates,tmin):
    d = dict()
    thickness_readings = readings
    reading_date = [datetime.strptime(x, '%Y-%m-%d') for x in dates]
    tmin = tmin
    delta_readings = thickness_readings[-1]-thickness_readings[-2]
    delta_dates = days_between(reading_date[-2],reading_date[-1])
    slope = round(delta_readings/delta_dates,6)
    y_int = thickness_readings[-2]
    yrs2tmin = round((tmin-y_int)/slope,2)
    extra_years = floor(yrs2tmin+3)
    predict_y = slope*extra_years+y_int
    d['predict_y']=[y_int,predict_y]
    d['predict_x']=[dates[-2],(reading_date[-1]+timedelta(days=extra_years*365)).strftime('%Y-%m-%d')]
    d['slope']=slope
    d['y_int']=y_int
    d['yrs2tmin']=yrs2tmin
    return d



thickness_readings = [0.009,0.0085,0.0082, 0.0081,0.0071]
reading_dates = ["2014-02-27","2015-03-17","2016-02-10","2017-05-13","2018-08-13"]
tmin = 0.004
howManyYrs = yrs_til_tmin(thickness_readings,reading_dates,tmin)

print(howManyYrs)



# print(delta_readings)
# print(delta_dates)
# print(slope)
# print(yrs_til)