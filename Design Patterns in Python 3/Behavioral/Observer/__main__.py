from kpis import KPIs
from forecast import Forecast
from currentkpis import CurrentKPIs

kpis = KPIs()
currentKPIs = CurrentKPIs(kpis)
forecast = Forecast(kpis)

kpis.set_kpis(25,10,5)
kpis.set_kpis(55,10,15)

print('Detach Forecast')
kpis.detach(forecast)
kpis.set_kpis(100,100,100)
