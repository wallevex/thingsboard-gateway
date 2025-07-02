from thingsboard_gateway.tb_utility.tb_utility import TBUtility

def test_get_value():
    body = {
  "cmd": 100,
  "id": "abc123",
  "data":{
    "temp": 99,
    "hum": "xxxyyy",
    "weekday": [1,2,3,4,5,6,7]
  }
}
    x = TBUtility()
    temp = x.get_value('${data.temp}', body, 'double')
    hum = x.get_value('${data.hum}', body, 'string')
    weekday = x.get_value('${data.weekday}', body, 'string')
    print(type(temp))
    print(hum)
    print(type(weekday))
    print(weekday[0])
