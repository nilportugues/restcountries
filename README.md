REST Countries
=======

**Que es, que tiene**
- countries-input.json es la base de datos real.. todo gira alrededor de este archivo.
- Este servicio java carga el JSON y lo parsea a cada peticion :\

**Actualización de datos**
- countries-input.json es la madre de todo. Si este archivo no existe o está vacio, no se crawlea nada.
   - Usa python3 para bajar info y montar la BBDD
   - debes correr python3 updater.py para actualizar la info




(Convertir a SpringBoot) API Endpoints
=======

Below are described the REST endpoints available that you can use to search for countries

All
---------------

``` html
https://restcountries.eu/rest/v2/all
```

Name
---------------

Search by country name. It can be the native name or partial name

``` javascript
https://restcountries.eu/rest/v2/name/{name}
```

``` html
https://restcountries.eu/rest/v2/name/eesti
```

``` html
https://restcountries.eu/rest/v2/name/united
```

Full Name
---------------

Search by country full name

``` javascript
https://restcountries.eu/rest/v2/name/{name}?fullText=true
```

``` html
https://restcountries.eu/rest/v2/name/aruba?fullText=true
```

Code
---------------

Search by ISO 3166-1 2-letter or 3-letter country code

``` javascript
https://restcountries.eu/rest/v2/alpha/{code}
```

``` html
https://restcountries.eu/rest/v2/alpha/co
```

``` html
https://restcountries.eu/rest/v2/alpha/col
```

List of codes
---------------

Search by list of ISO 3166-1 2-letter or 3-letter country codes

``` javascript
https://restcountries.eu/rest/v2/alpha?codes={code};{code};{code}
```

``` html
https://restcountries.eu/rest/v2/alpha?codes=col;no;ee
```

Currency
---------------

Search by ISO 4217 currency code

``` javascript
https://restcountries.eu/rest/v2/currency/{currency}
```
``` html
https://restcountries.eu/rest/v2/currency/cop
```

Language
---------------

Search by ISO 639-1 language code

``` javascript
https://restcountries.eu/rest/v2/lang/{et}
```
``` html
https://restcountries.eu/rest/v2/lang/es
```

Capital city
---------------

Search by capital city

``` javascript
https://restcountries.eu/rest/v2/capital/{capital}
```
``` html
https://restcountries.eu/rest/v2/capital/tallinn
```

Calling code
---------------

Search by calling code

``` javascript
https://restcountries.eu/rest/v2/callingcode/{callingcode}
```
``` html
https://restcountries.eu/rest/v2/callingcode/372
```

Region
---------------

Search by region: Africa, Americas, Asia, Europe, Oceania

``` javascript
https://restcountries.eu/rest/v2/region/{region}
```
``` html
https://restcountries.eu/rest/v2/region/europe
```

Response Example
---------------

``` html
https://restcountries.eu/rest/v2/alpha/col
```

``` json
[{
	"name": "Colombia",
	"topLevelDomain": [".co"],
	"alpha2Code": "CO",
	"alpha3Code": "COL",
	"callingCodes": ["57"],
	"capital": "Bogotá",
	"altSpellings": ["CO", "Republic of Colombia", "República de Colombia"],
	"region": "Americas",
	"population": 48759958,
	"latlng": [4.0, -72.0],
	"demonym": "Colombian",
	"area": 1141748.0,
	"gini": 55.9,
	"timezones": ["UTC-05:00"],
	"borders": ["BRA", "ECU", "PAN", "PER", "VEN"],
	"nativeName": "Colombia",
	"numericCode": "170",
	"currencies": [{
		"code": "COP",
		"name": "Colombian peso",
		"symbol": "$"
	}],
	"languages": [{
		"iso639_1": "es",
		"iso639_2": "spa",
		"name": "Spanish",
		"nativeName": "Español"
	}],
	"translations": {
		"de": "Kolumbien",
		"es": "Colombia",
		"fr": "Colombie",
		"ja": "コロンビア",
		"it": "Colombia",
		"br": "Colômbia",
		"pt": "Colômbia"
	},
	"flag": "https://restcountries.eu/data/col.svg"
}
```

Filter Response
=======

You can filter the output of your request to include only the specified fields.

``` javascript
https://restcountries.eu/rest/v2/{service}?fields={field};{field};{field}
```
``` html
https://restcountries.eu/rest/v2/all?fields=name;capital;currencies
```

Sources
=======
* [@mledoze]
* [List of countries]
* [Languages]
* [Currencies]
* [Area]

Similar projects
=======
* [Countries of the word]
* [REST Countries Node.js]
* [REST Countries Ruby]
* [REST Countries Go]
* [REST Countries Python]
* [world-currencies]

License
=======
[Mozilla Public License] MPL

[dist]: https://github.com/fayder/restcountries/
[Twitter]: https://twitter.com/restcountries
[mailing list]: http://eepurl.com/cC-h2v
[donate]: https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=V5AJAEMKE6A3E
[@mledoze]: https://github.com/mledoze/countries
[List of countries]: https://en.wikipedia.org/wiki/ISO_3166-1#Current_codes
[Languages]: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
[Currencies]: https://en.wikipedia.org/wiki/List_of_circulating_currencies
[Area]: https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_area
[Population]: https://en.wikipedia.org/wiki/List_of_countries_by_population
[Gini coefficient]: http://en.wikipedia.org/wiki/List_of_countries_by_income_equality
[Mozilla Public License]: http://www.mozilla.org/MPL/
[world-currencies]: https://github.com/wiredmax/world-currencies
[REST Countries Node.js]: https://github.com/aredo/restcountries
[REST Countries Ruby]: https://github.com/davidesantangelo/restcountry
[REST Countries Go]: https://github.com/alediaferia/gocountries
[REST Countries Python]: https://github.com/SteinRobert/python-restcountries
[Countries of the world]: http://countries.petethompson.net
