import logging

from thingsboard_gateway.connectors.mqtt.json_mqtt_uplink_converter import JsonMqttUplinkConverter

def test_json_mqtt_uplink_converter():
    config = {
      "topicFilter": "hjy-dev/test/+/attr/",
      "subscriptionQos": 0,
      "converter": {
        "type": "json",
        "deviceInfo": {
          "deviceNameExpression": "${id}",
          "deviceNameExpressionSource": "message",
          "deviceProfileExpressionSource": "constant",
          "deviceProfileExpression": "Thermometer"
        },
        "attributes": [
          {
            "key": "model",
            "type": "string",
            "value": "${data.sensorModel}"
          }
        ],
        "timeseries": [
          {
            "key": "temperature",
            "type": "double",
            "value": "${data.temp}"
          },
          {
            "key": "humidity",
            "type": "string",
            "value": "${data.hum}"
          },
          {
            "key": "weekday",
            "type": "string",
            "value": "${data.weekday}"
          }
        ]
      }
    }
    converter = JsonMqttUplinkConverter(config,logging.getLogger("TEST"))
    data = {
  "cmd": 100,
  "id": "abc123",
  "data":{
    "temp": 99,
    "hum": "xxxyyy",
    "weekday": [1,2,3,4,5,6,7]
  }
}
    ans = converter.convert("hjy-dev/test/abc123/attr/", data)
    print(ans)
