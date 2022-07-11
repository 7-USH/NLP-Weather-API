# NLP Weather API

Get weather details of any place with NLTK
## Deployed Link

```
https://my-api09.herokuapp.com/api?query=$sentence
```

> The variable sentence must contain the name of City,Country or any location, aslong as the sentence contains name of any location the api works.

## Example of API call

```
https://my-api09.herokuapp.com/api?query=what is the weather in mumbai?
```
## Example of API response

```
{
   "base":"stations",
   "clouds":{
      "all":100
   },
   "cod":200,
   "coord":{
      "lat":19.0144,
      "lon":72.8479
   },
   "dt":1657531990,
   "id":1275339,
   "main":{
      "feels_like":308.76,
      "humidity":84,
      "pressure":1004,
      "temp":302.14,
      "temp_max":302.14,
      "temp_min":301.09
   },
   "name":"Mumbai",
   "rain":{
      "1h":2.73
   },
   "sys":{
      "country":"IN",
      "id":9052,
      "sunrise":1657499867,
      "sunset":1657547395,
      "type":1
   },
   "timezone":19800,
   "visibility":2500,
   "weather":[
      {
         "description":"haze",
         "icon":"50d",
         "id":721,
         "main":"Haze"
      },
      {
         "description":"moderate rain",
         "icon":"10d",
         "id":501,
         "main":"Rain"
      }
   ],
   "wind":{
      "deg":260,
      "speed":7.72
   }
}
```
