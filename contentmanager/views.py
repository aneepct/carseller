from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from .models import City
from frontend.models import CarBrand, CarModel, CarYear


cities_array = [
    {
        "id":306,
        "lat":50.7618,
        "lng":6.154446,
        "name":"Aachen",
        "street":"Neuenhofstra\u00dfe 191",
        "zipcode":"52078",
        "city":"Aachen",
        "area":"null",
        "partner":"null"
    },
    {
        "id":201,
        "lat":51.456291,
        "lng":7.952553,
        "name":"Arnsberg",
        "street":"Im Ohl 4",
        "zipcode":"59757",
        "city":"Arnsberg",
        "area":"null",
        "partner":"null"
    },
    {
        "id":235,
        "lat":49.981494,
        "lng":9.15111,
        "name":"Aschaffenburg",
        "street":"Auhofstra\u00dfe 2a",
        "zipcode":"63741",
        "city":"Aschaffenburg",
        "area":"null",
        "partner":"null"
    },
    {
        "id":47,
        "lat":48.319119,
        "lng":10.862039,
        "name":"Augsburg-S\u00fcd",
        "street":"B\u00fcrgermeister-Schlosser-Str. 1",
        "zipcode":"86199",
        "city":"Augsburg",
        "area":"null",
        "partner":"null"
    },
    {
        "id":295,
        "lat":52.217045,
        "lng":8.831016,
        "name":"Minden",
        "street":"Adam-Opel-Stra\u00dfe 8",
        "zipcode":"32547",
        "city":"Bad Oeynhausen",
        "area":"Minden",
        "partner":"null"
    },
    {
        "id":216,
        "lat":51.180856,
        "lng":14.415399,
        "name":"Bautzen",
        "street":"Schliebenstra\u00dfe 18",
        "zipcode":"02625",
        "city":"Bautzen",
        "area":"null",
        "partner":"null"
    },
    {
        "id":219,
        "lat":49.95561,
        "lng":11.55448,
        "name":"Bayreuth",
        "street":"Am Bauhof 17",
        "zipcode":"95445",
        "city":"Bayreuth",
        "area":"null",
        "partner":"null"
    },
    {
        "id":211,
        "lat":52.526573,
        "lng":13.308781,
        "name":"Berlin-Charlottenburg",
        "street":"Ilsenburger Stra\u00dfe 29-31",
        "zipcode":"10589",
        "city":"Berlin",
        "area":"Berlin",
        "partner":{
            "id":2,
            "name":"T\u00dcV",
            "logoPath":"https:\/\/content.wirkaufendeinauto.de\/static\/car_images\/tuef-fsp-logo.jpg",
            "country":"DE",
            "status":1
        }
    },
    {
        "id":308,
        "lat":52.453577,
        "lng":13.59184,
        "name":"Berlin-K\u00f6penick",
        "street":"Salvador-Allende-Stra\u00dfe 117",
        "zipcode":"12555",
        "city":"Berlin",
        "area":"null",
        "partner":"null"
    },
    {
        "id":226,
        "lat":52.524273,
        "lng":13.499974,
        "name":"Berlin-Lichtenberg",
        "street":"Siegfriedstra\u00dfe 60",
        "zipcode":"10365",
        "city":"Berlin",
        "area":"Berlin",
        "partner":"null"
    },
    {
        "id":1,
        "lat":52.573843,
        "lng":13.444824,
        "name":"Berlin-Pankow",
        "street":"Blankenburger Stra\u00dfe 23",
        "zipcode":"13089",
        "city":"Berlin",
        "area":"Berlin",
        "partner":"null"
    },
    {
        "id":274,
        "lat":52.550267,
        "lng":13.247406,
        "name":"Berlin-Siemensstadt",
        "street":"Gartenfelder Stra\u00dfe 28",
        "zipcode":"13599",
        "city":"Berlin",
        "area":"null",
        "partner":"null"
    },
    {
        "id":321,
        "lat":52.457168,
        "lng":13.420174,
        "name":"Berlin-Tempelhof",
        "street":"Bergholzstra\u00dfe 4",
        "zipcode":"12099",
        "city":"Berlin",
        "area":"null",
        "partner":"null"
    },
    {
        "id":52,
        "lat":52.485014,
        "lng":13.456136,
        "name":"Berlin-Treptow",
        "street":"Heidelberger Stra\u00dfe 61",
        "zipcode":"12435",
        "city":"Berlin",
        "area":"null",
        "partner":"null"
    },
    {
        "id":330,
        "lat":52.010783,
        "lng":8.572833,
        "name":"Bielefeld",
        "street":"Stralsunder Stra\u00dfe 62",
        "zipcode":"33605",
        "city":"Bielefeld",
        "area":"null",
        "partner":"null"
    },
    {
        "id":220,
        "lat":49.918269,
        "lng":10.809434,
        "name":"Bamberg",
        "street":"B\u00fcrgermeister-Wachter-Stra\u00dfe 2",
        "zipcode":"96120",
        "city":"Bischberg",
        "area":"Bamberg",
        "partner":"null"
    },
    {
        "id":251,
        "lat":51.46789,
        "lng":7.132578,
        "name":"Bochum-Wattenscheid",
        "street":"Berliner Stra\u00dfe 79",
        "zipcode":"44867",
        "city":"Bochum",
        "area":"null",
        "partner":"null"
    },
    {
        "id":57,
        "lat":50.742841,
        "lng":7.055092,
        "name":"Bonn-Nord",
        "street":"Hohe Str. 65",
        "zipcode":"53119",
        "city":"Bonn",
        "area":"null",
        "partner":"null"
    },
    {
        "id":76,
        "lat":52.311261,
        "lng":10.505417,
        "name":"Braunschweig",
        "street":"Benzstr. 1",
        "zipcode":"38112",
        "city":"Braunschweig",
        "area":"null",
        "partner":"null"
    },
    {
        "id":279,
        "lat":53.024873,
        "lng":8.866111,
        "name":"Bremen",
        "street":"Arster Hemm 56",
        "zipcode":"28279",
        "city":"Bremen",
        "area":"null",
        "partner":"null"
    },
    {
        "id":67,
        "lat":53.567378,
        "lng":8.595584,
        "name":"Bremerhaven",
        "street":"Stresemannstra\u00dfe 279",
        "zipcode":"27580",
        "city":"Bremerhaven",
        "area":"null",
        "partner":"null"
    },
    {
        "id":238,
        "lat":50.843797,
        "lng":6.903884,
        "name":"K\u00f6ln-Br\u00fchl",
        "street":"Gleueler Weg 5",
        "zipcode":"50321",
        "city":"Br\u00fchl",
        "area":"K\u00f6ln",
        "partner":"null"
    },
    {
        "id":240,
        "lat":50.845681,
        "lng":12.918902,
        "name":"Chemnitz",
        "street":"Nordstra\u00dfe 41",
        "zipcode":"09113",
        "city":"Chemnitz",
        "area":"null",
        "partner":"null"
    },
    {
        "id":69,
        "lat":51.761008,
        "lng":14.359483,
        "name":"Cottbus",
        "street":"An der Pastoa 13",
        "zipcode":"03042",
        "city":"Cottbus",
        "area":"null",
        "partner":"null"
    },
    {
        "id":267,
        "lat":49.888761,
        "lng":8.653039,
        "name":"Darmstadt",
        "street":"Frankfurter Stra\u00dfe 97",
        "zipcode":"64293",
        "city":"Darmstadt",
        "area":"null",
        "partner":"null"
    },
    {
        "id":45,
        "lat":48.83457,
        "lng":12.945615,
        "name":"Deggendorf",
        "street":"Mettener Str. 15",
        "zipcode":"94469",
        "city":"Deggendorf",
        "area":"null",
        "partner":"null"
    },
    {
        "id":319,
        "lat":51.8497,
        "lng":12.240269,
        "name":"Dessau-Ro\u00dflau",
        "street":"Albrechtstra\u00dfe 89",
        "zipcode":"06844",
        "city":"Dessau-Ro\u00dflau",
        "area":"null",
        "partner":"null"
    },
    {
        "id":242,
        "lat":47.961228,
        "lng":8.512967,
        "name":"Donaueschingen",
        "street":"Carl-Benz-Stra\u00dfe 2B",
        "zipcode":"78166",
        "city":"Donaueschingen",
        "area":"null",
        "partner":"null"
    },
    {
        "id":286,
        "lat":51.673806,
        "lng":6.995149,
        "name":"Dorsten",
        "street":"Halterner Str. 195",
        "zipcode":"46284",
        "city":"Dorsten",
        "area":"null",
        "partner":"null"
    },
    {
        "id":325,
        "lat":51.540083,
        "lng":7.550234,
        "name":"Dortmund-Brackel",
        "street":"He\u00dflingsweg 71",
        "zipcode":"44309",
        "city":"Dortmund",
        "area":"null",
        "partner":"null"
    },
    {
        "id":296,
        "lat":51.507434,
        "lng":7.391602,
        "name":"Dortmund-Dorstfeld",
        "street":"Planetenfeldstra\u00dfe 118",
        "zipcode":"44379",
        "city":"Dortmund",
        "area":"null",
        "partner":"null"
    },
    {
        "id":7,
        "lat":51.034169,
        "lng":13.712011,
        "name":"Dresden-Plauen",
        "street":"Bamberger Strasse 8",
        "zipcode":"01187",
        "city":"Dresden",
        "area":"null",
        "partner":"null"
    },
    {
        "id":332,
        "lat":51.476393,
        "lng":6.79001,
        "name":"Duisburg",
        "street":"Neum\u00fchler Stra\u00dfe 24",
        "zipcode":"47138",
        "city":"Duisburg",
        "area":"null",
        "partner":"null"
    },
    {
        "id":297,
        "lat":50.808441,
        "lng":6.484299,
        "name":"D\u00fcren",
        "street":"Lagerstra\u00dfe 3",
        "zipcode":"52351",
        "city":"D\u00fcren",
        "area":"null",
        "partner":"null"
    },
    {
        "id":257,
        "lat":51.283138,
        "lng":6.741087,
        "name":"D\u00fcsseldorf-Lohausen",
        "street":"Niederrheinstra\u00dfe 211",
        "zipcode":"40474",
        "city":"D\u00fcsseldorf",
        "area":"D\u00fcsseldorf",
        "partner":"null"
    },
    {
        "id":221,
        "lat":50.480724,
        "lng":9.734464,
        "name":"Fulda",
        "street":"B\u00fcrgermeister-Ebert-Stra\u00dfe 36",
        "zipcode":"36124",
        "city":"Eichenzell",
        "area":"Fulda",
        "partner":"null"
    },
    {
        "id":25,
        "lat":50.996158,
        "lng":11.040838,
        "name":"Erfurt-Johannesvorstadt",
        "street":"Dieselstra\u00dfe 2",
        "zipcode":"99086",
        "city":"Erfurt",
        "area":"null",
        "partner":"null"
    },
    {
        "id":42,
        "lat":51.437434,
        "lng":7.094983,
        "name":"Essen-Steele",
        "street":"Kleine Ruhrau 20",
        "zipcode":"45279",
        "city":"Essen",
        "area":"null",
        "partner":"null"
    },
    {
        "id":63,
        "lat":54.761222,
        "lng":9.411997,
        "name":"Flensburg",
        "street":"Graf-Zeppelin-Str. 1",
        "zipcode":"24941",
        "city":"Flensburg",
        "area":"null",
        "partner":"null"
    },
    {
        "id":54,
        "lat":50.123719,
        "lng":8.588918,
        "name":"Frankfurt",
        "street":"Westerbachstra\u00dfe 122",
        "zipcode":"65936",
        "city":"Frankfurt",
        "area":"Frankfurt",
        "partner":"null"
    },
    {
        "id":246,
        "lat":48.029944,
        "lng":7.862722,
        "name":"Freiburg",
        "street":"Gundelfinger Str. 25",
        "zipcode":"79108",
        "city":"Freiburg im Breisgau",
        "area":"null",
        "partner":"null"
    },
    {
        "id":239,
        "lat":47.676612,
        "lng":9.47645,
        "name":"Friedrichshafen",
        "street":"Albert-Maier-Stra\u00dfe 10",
        "zipcode":"88045",
        "city":"Friedrichshafen",
        "area":"null",
        "partner":"null"
    },
    {
        "id":320,
        "lat":49.485474,
        "lng":11.004481,
        "name":"F\u00fcrth",
        "street":"Hans-Vogel-Stra\u00dfe 125",
        "zipcode":"90765",
        "city":"F\u00fcrth",
        "area":"null",
        "partner":"null"
    },
    {
        "id":259,
        "lat":51.545722,
        "lng":7.074694,
        "name":"Gelsenkirchen",
        "street":"Benzstra\u00dfe 1",
        "zipcode":"45891",
        "city":"Gelsenkirchen",
        "area":"null",
        "partner":"null"
    },
    {
        "id":204,
        "lat":50.860846,
        "lng":12.091492,
        "name":"Gera",
        "street":"Plauensche Stra\u00dfe 184",
        "zipcode":"07551",
        "city":"Gera",
        "area":"null",
        "partner":"null"
    },
    {
        "id":169,
        "lat":50.584421,
        "lng":8.644148,
        "name":"Gie\u00dfen",
        "street":"Friedrich-List-Stra\u00dfe 27-29",
        "zipcode":"35398",
        "city":"Gie\u00dfen",
        "area":"null",
        "partner":"null"
    },
    {
        "id":272,
        "lat":54.07698,
        "lng":13.388763,
        "name":"Greifswald",
        "street":"Am Gorzberg 24-28",
        "zipcode":"17489",
        "city":"Greifswald",
        "area":"null",
        "partner":"null"
    },
    {
        "id":217,
        "lat":48.695426,
        "lng":9.679016,
        "name":"G\u00f6ppingen",
        "street":"Heilbronner Stra\u00dfe 3",
        "zipcode":"73037",
        "city":"G\u00f6ppingen",
        "area":"null",
        "partner":"null"
    },
    {
        "id":49,
        "lat":51.527662,
        "lng":9.89109,
        "name":"G\u00f6ttingen-West",
        "street":"Siekweg 19a",
        "zipcode":"37081",
        "city":"G\u00f6ttingen",
        "area":"null",
        "partner":"null"
    },
    {
        "id":215,
        "lat":51.522246,
        "lng":11.955356,
        "name":"Halle (Saale)",
        "street":"An der Saalebahn 2",
        "zipcode":"06118",
        "city":"Halle",
        "area":"null",
        "partner":"null"
    },
    {
        "id":3,
        "lat":53.597902,
        "lng":9.9774990999999,
        "name":"Hamburg-Eppendorf",
        "street":"Osterfeldstrasse 8",
        "zipcode":"22529",
        "city":"Hamburg",
        "area":"Hamburg",
        "partner":"null"
    },
    {
        "id":218,
        "lat":53.457693,
        "lng":10.006383,
        "name":"Hamburg-Harburg",
        "street":"Gro\u00dfmoorring 8",
        "zipcode":"21079",
        "city":"Hamburg",
        "area":"Hamburg",
        "partner":"null"
    },
    {
        "id":229,
        "lat":53.670201,
        "lng":10.069437,
        "name":"Hamburg-Poppenb\u00fcttel",
        "street":"Poppenb\u00fctteler Bogen 13",
        "zipcode":"22399",
        "city":"Hamburg",
        "area":"Hamburg",
        "partner":"null"
    },
    {
        "id":83,
        "lat":50.144385,
        "lng":8.923037,
        "name":"Hanau",
        "street":"Martin-Luther-King-Stra\u00dfe 4",
        "zipcode":"63452",
        "city":"Hanau",
        "area":"null",
        "partner":"null"
    },
    {
        "id":10,
        "lat":52.416241,
        "lng":9.742572,
        "name":"Hannover-Vahrenheide",
        "street":"Alter Flughafen 6",
        "zipcode":"30179",
        "city":"Hannover",
        "area":"Hannover",
        "partner":"null"
    },
    {
        "id":275,
        "lat":49.403969,
        "lng":8.638051,
        "name":"Heidelberg",
        "street":"Kurpfalzring 116 - 118",
        "zipcode":"69123",
        "city":"Heidelberg",
        "area":"null",
        "partner":"null"
    },
    {
        "id":68,
        "lat":48.716285,
        "lng":10.157836,
        "name":"Heidenheim an der Brenz",
        "street":"Aufhausener Str. 35",
        "zipcode":"89520",
        "city":"Heidenheim an der Brenz",
        "area":"null",
        "partner":"null"
    },
    {
        "id":50,
        "lat":49.122236,
        "lng":9.203477,
        "name":"Heilbronn",
        "street":"Kreuz\u00e4ckerstr 35",
        "zipcode":"74081",
        "city":"Heilbronn",
        "area":"null",
        "partner":"null"
    },
    {
        "id":200,
        "lat":48.601503,
        "lng":8.86934,
        "name":"Herrenberg",
        "street":"Daimlerstra\u00dfe 6",
        "zipcode":"71083",
        "city":"Herrenberg",
        "area":"null",
        "partner":"null"
    },
    {
        "id":307,
        "lat":52.169286,
        "lng":9.917339,
        "name":"Hildesheim",
        "street":"Marggrafstra\u00dfe 23",
        "zipcode":"31137",
        "city":"Hildesheim",
        "area":"null",
        "partner":"null"
    },
    {
        "id":77,
        "lat":50.291573,
        "lng":11.925601,
        "name":"Hof",
        "street":"Schneebergstra\u00dfe 8",
        "zipcode":"95032",
        "city":"Hof",
        "area":"null",
        "partner":"null"
    },
    {
        "id":318,
        "lat":48.783459,
        "lng":11.473863,
        "name":"Ingolstadt",
        "street":"Marie-Curie-Stra\u00dfe 14",
        "zipcode":"85055",
        "city":"Ingolstadt",
        "area":"null",
        "partner":"null"
    },
    {
        "id":322,
        "lat":51.214049,
        "lng":6.631589,
        "name":"Neuss-Kaarst",
        "street":"Daimlerstra\u00dfe 12",
        "zipcode":"41564",
        "city":"Kaarst",
        "area":"null",
        "partner":"null"
    },
    {
        "id":168,
        "lat":49.4419638,
        "lng":7.7256659,
        "name":"Kaiserslautern",
        "street":"Merkurstra\u00dfe 23",
        "zipcode":"67663",
        "city":"Kaiserslautern",
        "area":"null",
        "partner":"null"
    },
    {
        "id":237,
        "lat":51.567527,
        "lng":7.675927,
        "name":"Kamen",
        "street":"Unnaer Stra\u00dfe 97",
        "zipcode":"59174",
        "city":"Kamen",
        "area":"null",
        "partner":"null"
    },
    {
        "id":87,
        "lat":48.995727,
        "lng":8.448403,
        "name":"Karlsruhe",
        "street":"Ottostra\u00dfe 1d",
        "zipcode":"76227",
        "city":"Karlsruhe",
        "area":"null",
        "partner":"null"
    },
    {
        "id":16,
        "lat":51.307208,
        "lng":9.522554,
        "name":"Kassel-Bettenhausen",
        "street":"Leipziger Stra\u00dfe 96",
        "zipcode":"34123",
        "city":"Kassel",
        "area":"null",
        "partner":"null"
    },
    {
        "id":64,
        "lat":47.705924,
        "lng":10.325908,
        "name":"Kempten",
        "street":"Friedrich-Ebert-Stra\u00dfe 5",
        "zipcode":"87437",
        "city":"Kempten (Allg\u00e4u)",
        "area":"null",
        "partner":"null"
    },
    {
        "id":66,
        "lat":54.297268,
        "lng":10.168165,
        "name":"Kiel",
        "street":"Preetzer Str. 304",
        "zipcode":"24147",
        "city":"Kiel",
        "area":"null",
        "partner":"null"
    },
    {
        "id":273,
        "lat":51.354133,
        "lng":6.623201,
        "name":"Krefeld",
        "street":"Emil-Sch\u00e4fer-Stra\u00dfe 71",
        "zipcode":"47800",
        "city":"Krefeld",
        "area":"null",
        "partner":"null"
    },
    {
        "id":294,
        "lat":48.499856,
        "lng":12.160335,
        "name":"Landshut",
        "street":"Ziegelfeldstra\u00dfe 6",
        "zipcode":"84036",
        "city":"Kumhausen",
        "area":"Landshut",
        "partner":"null"
    },
    {
        "id":181,
        "lat":51.001336,
        "lng":7.035033,
        "name":"K\u00f6ln-D\u00fcnnwald",
        "street":"R\u00f6nsahlerstr. 3-17",
        "zipcode":"51069",
        "city":"K\u00f6ln",
        "area":"K\u00f6ln",
        "partner":"null"
    },
    {
        "id":2,
        "lat":50.99086,
        "lng":6.909956,
        "name":"K\u00f6ln-Longerich",
        "street":"Hugo-Junkers-Stra\u00dfe 12d",
        "zipcode":"50739",
        "city":"K\u00f6ln",
        "area":"K\u00f6ln",
        "partner":"null"
    },
    {
        "id":74,
        "lat":50.880396,
        "lng":7.069797,
        "name":"K\u00f6ln-Porz",
        "street":"Kaiserstra\u00dfe 103",
        "zipcode":"51145",
        "city":"K\u00f6ln",
        "area":"K\u00f6ln",
        "partner":"null"
    },
    {
        "id":72,
        "lat":52.294737,
        "lng":9.830095,
        "name":"Hannover-Laatzen",
        "street":"L\u00fcbecker Str. 5",
        "zipcode":"30880",
        "city":"Laatzen",
        "area":"Hannover",
        "partner":"null"
    },
    {
        "id":234,
        "lat":51.123633,
        "lng":6.95713,
        "name":"D\u00fcsseldorf-Langenfeld",
        "street":"Industriestra\u00dfe 61",
        "zipcode":"40764",
        "city":"Langenfeld (Rheinland)",
        "area":"D\u00fcsseldorf",
        "partner":"null"
    },
    {
        "id":4,
        "lat":51.3422372,
        "lng":12.4373399,
        "name":"Leipzig-Paunsdorf",
        "street":"Geithainer Strasse 15",
        "zipcode":"04328",
        "city":"Leipzig",
        "area":"null",
        "partner":"null"
    },
    {
        "id":233,
        "lat":48.921576,
        "lng":9.146669,
        "name":"Ludwigsburg",
        "street":"Maybachstrasse 5",
        "zipcode":"71634",
        "city":"Ludwigsburg",
        "area":"null",
        "partner":"null"
    },
    {
        "id":284,
        "lat":49.497119,
        "lng":8.37466,
        "name":"Ludwigshafen am Rhein",
        "street":"Notwendestra\u00dfe 34",
        "zipcode":"67071",
        "city":"Ludwigshafen am Rhein",
        "area":"null",
        "partner":"null"
    },
    {
        "id":39,
        "lat":53.849388,
        "lng":10.677732,
        "name":"L\u00fcbeck-S\u00fcd",
        "street":"Bei der Gasanstalt 2-4",
        "zipcode":"23560",
        "city":"L\u00fcbeck",
        "area":"null",
        "partner":"null"
    },
    {
        "id":27,
        "lat":52.082961,
        "lng":11.582807,
        "name":"Magdeburg-Ottersleben",
        "street":"Werner-von-Siemens-Ring 17b",
        "zipcode":"39116",
        "city":"Magdeburg",
        "area":"null",
        "partner":"null"
    },
    {
        "id":41,
        "lat":49.9579,
        "lng":8.26253,
        "name":"Mainz-Hechtsheim",
        "street":"Robert-Koch-Str. 28",
        "zipcode":"55129",
        "city":"Mainz",
        "area":"null",
        "partner":"null"
    },
    {
        "id":285,
        "lat":50.013988,
        "lng":8.287976,
        "name":"Wiesbaden",
        "street":"Ludwig-Wolker-Stra\u00dfe 14",
        "zipcode":"55252",
        "city":"Mainz-Kastel (Wiesbaden)",
        "area":"Wiesbaden",
        "partner":"null"
    },
    {
        "id":19,
        "lat":49.459143,
        "lng":8.506599,
        "name":"Mannheim-Neckarau",
        "street":"Siegmund-Schuckert-Str. 24",
        "zipcode":"68199",
        "city":"Mannheim",
        "area":"null",
        "partner":"null"
    },
    {
        "id":43,
        "lat":51.219683,
        "lng":6.478864,
        "name":"M\u00f6nchengladbach-Ost",
        "street":"Krefelder Stra\u00dfe 510",
        "zipcode":"41066",
        "city":"M\u00f6nchengladbach",
        "area":"null",
        "partner":"null"
    },
    {
        "id":59,
        "lat":51.40973,
        "lng":6.869305,
        "name":"M\u00fclheim an der Ruhr",
        "street":"D\u00fcsseldorfer Str. 166",
        "zipcode":"45481",
        "city":"M\u00fclheim an der Ruhr",
        "area":"null",
        "partner":"null"
    },
    {
        "id":223,
        "lat":50.393697,
        "lng":7.510327,
        "name":"M\u00fclheim-K\u00e4rlich",
        "street":"In der P\u00fctzgewann 14",
        "zipcode":"56218",
        "city":"M\u00fclheim\u00ad-K\u00e4rlich",
        "area":"M\u00fclheim-K\u00e4rlich",
        "partner":"null"
    },
    {
        "id":53,
        "lat":48.137517,
        "lng":11.629718,
        "name":"M\u00fcnchen-Bogenhausen",
        "street":"Zamdorfer Str. 22",
        "zipcode":"81677",
        "city":"M\u00fcnchen",
        "area":"M\u00fcnchen",
        "partner":"null"
    },
    {
        "id":5,
        "lat":48.140508,
        "lng":11.52358,
        "name":"M\u00fcnchen-Laim",
        "street":"Landsberger Stra\u00dfe 183",
        "zipcode":"80687",
        "city":"M\u00fcnchen",
        "area":"M\u00fcnchen",
        "partner":"null"
    },
    {
        "id":36,
        "lat":51.911686,
        "lng":7.685149,
        "name":"M\u00fcnster-Hiltrup",
        "street":"Zum Kaiserbusch 7",
        "zipcode":"48165",
        "city":"M\u00fcnster",
        "area":"null",
        "partner":"null"
    },
    {
        "id":92,
        "lat":53.567413,
        "lng":13.269959,
        "name":"Neubrandenburg",
        "street":"Pasewalker Str. 5",
        "zipcode":"17034",
        "city":"Neubrandenburg",
        "area":"null",
        "partner":"null"
    },
    {
        "id":245,
        "lat":48.313843,
        "lng":11.653577,
        "name":"M\u00fcnchen-Neufahrn",
        "street":"Ludwig-Erhard-Stra\u00dfe 2",
        "zipcode":"85375",
        "city":"Neufahrn",
        "area":"M\u00fcnchen",
        "partner":"null"
    },
    {
        "id":61,
        "lat":49.476769,
        "lng":11.121245,
        "name":"N\u00fcrnberg-Ost",
        "street":"Schafhofstra\u00dfe 39",
        "zipcode":"90411",
        "city":"N\u00fcrnberg",
        "area":"null",
        "partner":"null"
    },
    {
        "id":8,
        "lat":49.428414,
        "lng":11.032553,
        "name":"N\u00fcrnberg-Schweinau",
        "street":"Dieselstr. 24",
        "zipcode":"90441",
        "city":"N\u00fcrnberg",
        "area":"null",
        "partner":"null"
    },
    {
        "id":336,
        "lat":51.484622,
        "lng":6.87496,
        "name":"Oberhausen",
        "street":"Im Lipperfeld 10",
        "zipcode":"46047",
        "city":"Oberhausen",
        "area":"null",
        "partner":"null"
    },
    {
        "id":243,
        "lat":50.084953,
        "lng":8.745565,
        "name":"Offenbach",
        "street":"Sprendlinger Landstra\u00dfe 173 a",
        "zipcode":"63069",
        "city":"Offenbach am Main",
        "area":"null",
        "partner":"null"
    },
    {
        "id":270,
        "lat":53.179528,
        "lng":8.202581,
        "name":"Oldenburg",
        "street":"Meeschweg 9",
        "zipcode":"26127",
        "city":"Oldenburg",
        "area":"null",
        "partner":"null"
    },
    {
        "id":51,
        "lat":52.26116,
        "lng":8.072082,
        "name":"Osnabr\u00fcck-Fledder",
        "street":"Hannoversche Stra\u00dfe 52 b",
        "zipcode":"49084",
        "city":"Osnabr\u00fcck",
        "area":"null",
        "partner":"null"
    },
    {
        "id":104,
        "lat":51.697558,
        "lng":8.731084,
        "name":"Paderborn",
        "street":"Frankfurter Weg 68",
        "zipcode":"33106",
        "city":"Paderborn",
        "area":"null",
        "partner":"null"
    },
    {
        "id":244,
        "lat":48.904474,
        "lng":8.658231,
        "name":"Pforzheim",
        "street":"Mannheimer Str. 19",
        "zipcode":"75179",
        "city":"Pforzheim",
        "area":"null",
        "partner":"null"
    },
    {
        "id":281,
        "lat":49.215511,
        "lng":7.595076,
        "name":"Pirmasens",
        "street":"Zweibr\u00fccker Str. 173",
        "zipcode":"66954",
        "city":"Pirmasens",
        "area":"null",
        "partner":"null"
    },
    {
        "id":179,
        "lat":52.383472,
        "lng":13.106896,
        "name":"Potsdam",
        "street":"Gartenstra\u00dfe 22",
        "zipcode":"14482",
        "city":"Potsdam",
        "area":"null",
        "partner":"null"
    },
    {
        "id":60,
        "lat":49.015145,
        "lng":12.121049,
        "name":"Regensburg",
        "street":"Straubinger Stra\u00dfe 9",
        "zipcode":"93055",
        "city":"Regensburg",
        "area":"null",
        "partner":"null"
    },
    {
        "id":258,
        "lat":53.655449,
        "lng":9.819074,
        "name":"Hamburg-Rellingen",
        "street":"Hauptstra\u00dfe 138-144",
        "zipcode":"25462",
        "city":"Rellingen",
        "area":"Hamburg",
        "partner":"null"
    },
    {
        "id":269,
        "lat":50.625257,
        "lng":7.22368,
        "name":"Bad Honnef",
        "street":"Rolandsecker Weg 39",
        "zipcode":"53619",
        "city":"Rheinbreitbach (Bad Honnef)",
        "area":"Bad Honnef",
        "partner":"null"
    },
    {
        "id":323,
        "lat":47.848205,
        "lng":12.115973,
        "name":"Rosenheim",
        "street":"Klepperstra\u00dfe 18E",
        "zipcode":"83026",
        "city":"Rosenheim",
        "area":"null",
        "partner":"null"
    },
    {
        "id":263,
        "lat":54.095778,
        "lng":12.098561,
        "name":"Rostock",
        "street":"Werftstra\u00dfe 20",
        "zipcode":"18057",
        "city":"Rostock",
        "area":"null",
        "partner":"null"
    },
    {
        "id":241,
        "lat":49.224351,
        "lng":7.040595,
        "name":"Saarbr\u00fccken",
        "street":"Am Halberg 13",
        "zipcode":"66121",
        "city":"Saarbr\u00fccken",
        "area":"null",
        "partner":"null"
    },
    {
        "id":315,
        "lat":49.310724,
        "lng":6.73202,
        "name":"Saarlouis",
        "street":"Fasanenallee 18-22",
        "zipcode":"66740",
        "city":"Saarlouis",
        "area":"null",
        "partner":"null"
    },
    {
        "id":291,
        "lat":49.18439,
        "lng":10.064644,
        "name":"Crailsheim",
        "street":"R\u00f6tstra\u00dfe 5",
        "zipcode":"74589",
        "city":"Satteldorf",
        "area":"Crailsheim",
        "partner":"null"
    },
    {
        "id":232,
        "lat":50.035793,
        "lng":10.232042,
        "name":"Schweinfurt",
        "street":"Carl-Zei\u00df-Stra\u00dfe 29",
        "zipcode":"97424",
        "city":"Schweinfurt",
        "area":"null",
        "partner":"null"
    },
    {
        "id":316,
        "lat":53.648268,
        "lng":11.352527,
        "name":"Schwerin",
        "street":"Ratzeburger Stra\u00dfe 2",
        "zipcode":"19057",
        "city":"Schwerin",
        "area":"null",
        "partner":"null"
    },
    {
        "id":58,
        "lat":50.905974,
        "lng":8.013897,
        "name":"Siegen",
        "street":"Weidenauer Str.20",
        "zipcode":"57078",
        "city":"Siegen",
        "area":"null",
        "partner":"null"
    },
    {
        "id":79,
        "lat":48.77031,
        "lng":8.168537,
        "name":"Baden-Baden",
        "street":"In den Lissen 20",
        "zipcode":"76547",
        "city":"Sinzheim",
        "area":"Baden-Baden",
        "partner":"null"
    },
    {
        "id":15,
        "lat":48.772981,
        "lng":9.132189,
        "name":"Stuttgart-Botnang",
        "street":"Lindpaintnerstr. 5-7",
        "zipcode":"70195",
        "city":"Stuttgart",
        "area":"null",
        "partner":"null"
    },
    {
        "id":62,
        "lat":48.825445,
        "lng":9.098393,
        "name":"Stuttgart-Weilimdorf",
        "street":"Motorstra\u00dfe 38",
        "zipcode":"70499",
        "city":"Stuttgart",
        "area":"null",
        "partner":"null"
    },
    {
        "id":264,
        "lat":50.589212,
        "lng":10.714161,
        "name":"Suhl",
        "street":"Pf\u00fctschbergstra\u00dfe 5",
        "zipcode":"98527",
        "city":"Suhl",
        "area":"null",
        "partner":"null"
    },
    {
        "id":222,
        "lat":49.731439,
        "lng":6.609749,
        "name":"Trier",
        "street":"Diedenhofener Str. 1g",
        "zipcode":"54294",
        "city":"Trier",
        "area":"null",
        "partner":"null"
    },
    {
        "id":75,
        "lat":48.326981,
        "lng":10.047994,
        "name":"Ulm-Senden",
        "street":"Funkweg 12a",
        "zipcode":"89250",
        "city":"Ulm-Senden",
        "area":"Ulm-Senden",
        "partner":"null"
    },
    {
        "id":91,
        "lat":49.671444,
        "lng":12.157639,
        "name":"Weiden",
        "street":"Hochstra\u00dfe 9",
        "zipcode":"92637",
        "city":"Weiden",
        "area":"null",
        "partner":"null"
    },
    {
        "id":205,
        "lat":53.514726,
        "lng":8.093044,
        "name":"Wilhelmshaven",
        "street":"Banter Weg 13",
        "zipcode":"26389",
        "city":"Wilhelmshaven",
        "area":"null",
        "partner":"null"
    },
    {
        "id":310,
        "lat":52.429217,
        "lng":10.801562,
        "name":"Wolfsburg",
        "street":"Maybachweg 4",
        "zipcode":"38446",
        "city":"Wolfsburg",
        "area":"null",
        "partner":"null"
    },
    {
        "id":202,
        "lat":49.618471,
        "lng":8.349736,
        "name":"Worms",
        "street":"Horchheimerstr. 47a",
        "zipcode":"67547",
        "city":"Worms",
        "area":"null",
        "partner":"null"
    },
    {
        "id":46,
        "lat":51.249533,
        "lng":7.131018,
        "name":"Wuppertal-Elberfeld",
        "street":"Simonsstra\u00dfe 22",
        "zipcode":"42117",
        "city":"Wuppertal",
        "area":"null",
        "partner":"null"
    },
    {
        "id":231,
        "lat":49.758336,
        "lng":9.970521,
        "name":"W\u00fcrzburg",
        "street":"Winterh\u00e4user Stra\u00dfe 79",
        "zipcode":"97084",
        "city":"W\u00fcrzburg",
        "area":"null",
        "partner":"null"
    },
    {
        "id":261,
        "lat":50.706305,
        "lng":12.482808,
        "name":"Zwickau",
        "street":"B\u00fcrgerschachtstra\u00dfe 3C",
        "zipcode":"08056",
        "city":"Zwickau",
        "area":"null",
        "partner":"null"
    }
]

car_brands = {
		"abarth": {
	        "500": {
		        "2008": "2008",
		        "2009": "2009",
		        "2010": "2010",
		        "2011": "2011",
		        "2012": "2012",
		        "2013": "2013",
		        "2014": "2014",
		        "2015": "2015",
		        "2016": "2016",
		        "2017": "2017",
		        "2018": "2018"
		    },
	        "124 Spider": {
		        "2016": "2016",
		        "2017": "2017",
		        "2018": "2018"
		    },
	        "Grande Punto": {
		        "2008": "2008",
		        "2009": "2009",
		        "2010": "2010",
		        "2011": "2011"
		    },
	        "Punto": {
		        "2002": "2002",
		        "2003": "2003",
		        "2010": "2010",
		        "2011": "2011",
		        "2012": "2012",
		        "2013": "2013",
		        "2014": "2014",
		        "2015": "2015"
		    },
	        "Ritmo": {
		        "1983": "1983",
		        "1984": "1984",
		        "1985": "1985",
		        "1986": "1986"
		    },
	        "Stilo": {
		        "2001": "2001",
		        "2002": "2002",
		        "2003": "2003",
		        "2004": "2004",
		        "2005": "2005",
		        "2006": "2006"
		    }
	    },
    	"Alfa Romeo": {
	        "4C": {
		        "2013": "2013",
		        "2014": "2014",
		        "2015": "2015",
		        "2016": "2016",
		        "2017": "2017",
		        "2018": "2018"
		    },
	        "4C Spider": {
		        "2015": "2015",
		        "2016": "2016",
		        "2017": "2017",
		        "2018": "2018"
		    },
	        "8C Competizione": {
		        "2007": "2007",
		        "2008": "2008",
		        "2009": "2009",
		        "2010": "2010"
		    },
	        "Alfa 6": {
		        "1979": "1979",
		        "1980": "1980",
		        "1981": "1981",
		        "1982": "1982",
		        "1983": "1983",
		        "1984": "1984",
		        "1985": "1985",
		        "1986": "1986"
		    },
	        "Alfa 33": {
		        "1983": "1983",
		        "1984": "1984",
		        "1985": "1985",
		        "1986": "1986",
		        "1987": "1987",
		        "1988": "1988",
		        "1989": "1989",
		        "1990": "1990",
		        "1991": "1991",
		        "1992": "1992",
		        "1993": "1993",
		        "1994": "1994",
		        "1995": "1995"
		    },
	        "Alfa 75": {
		        "1985": "1985",
		        "1986": "1986",
		        "1987": "1987",
		        "1988": "1988",
		        "1989": "1989",
		        "1990": "1990",
		        "1991": "1991",
		        "1992": "1992"
		    },
	        "Alfa 90": {
		        "1986": "1986",
		        "1987": "1987"
		    },
	        "Alfa 145": {
		        "1994": "1994",
		        "1995": "1995",
		        "1996": "1996",
		        "1997": "1997",
		        "1998": "1998",
		        "1999": "1999",
		        "2000": "2000",
		        "2001": "2001"
		    },
	        "Alfa 146": {
		        "1995": "1995",
		        "1996": "1996",
		        "1997": "1997",
		        "1998": "1998",
		        "1999": "1999",
		        "2000": "2000",
		        "2001": "2001"
		    },
	        "Alfa 147": {
		        "2000": "2000",
		        "2001": "2001",
		        "2002": "2002",
		        "2003": "2003",
		        "2004": "2004",
		        "2005": "2005",
		        "2006": "2006",
		        "2007": "2007",
		        "2008": "2008",
		        "2009": "2009",
		        "2010": "2010",
		        "2011": "2011"
		    },
	        "Alfa 155": {
		        "1992": "1992",
		        "1993": "1993",
		        "1994": "1994",
		        "1995": "1995",
		        "1996": "1996",
		        "1997": "1997",
		        "1998": "1998"
		    },
	        "Alfa 156": {
		        "1997": "1997",
		        "1998": "1998",
		        "1999": "1999",
		        "2000": "2000",
		        "2001": "2001",
		        "2002": "2002",
		        "2003": "2003",
		        "2004": "2004",
		        "2005": "2005",
		        "2006": "2006",
		        "2007": "2007",
		        "2008": "2008",
		        "2009": "2009",
		        "2010": "2010",
		        "2011": "2011"
		    },
	        "Alfa 159": {
		        "2005": "2005",
		        "2006": "2006",
		        "2007": "2007",
		        "2008": "2008",
		        "2009": "2009",
		        "2010": "2010",
		        "2011": "2011",
		        "2012": "2012",
		        "2013": "2013"
		    },
	        "Alfa 164": {
		        "1988": "1988",
		        "1989": "1989",
		        "1990": "1990",
		        "1991": "1991",
		        "1992": "1992",
		        "1993": "1993",
		        "1994": "1994",
		        "1995": "1995",
		        "1996": "1996",
		        "1997": "1997",
		        "1998": "1998"
		    },
	        "Alfa 166": {
		        "1998": "1998",
		        "1999": "1999",
		        "2000": "2000",
		        "2001": "2001",
		        "2002": "2002",
		        "2003": "2003",
		        "2004": "2004",
		        "2005": "2005",
		        "2006": "2006",
		        "2007": "2007"
		    },
	        "Alfa Brera": {
		        "2005": "2005",
		        "2006": "2006",
		        "2007": "2007",
		        "2008": "2008",
		        "2009": "2009",
		        "2010": "2010",
		        "2011": "2011"
		    },
	        "Alfa GT": {
		        "2004": "2004",
		        "2005": "2005",
		        "2006": "2006",
		        "2007": "2007",
		        "2008": "2008",
		        "2009": "2009",
		        "2010": "2010"
		    },
	        "Alfa GTV": {
		        "1995": "1995",
		        "1996": "1996",
		        "1997": "1997",
		        "1998": "1998",
		        "1999": "1999",
		        "2000": "2000",
		        "2001": "2001",
		        "2002": "2002",
		        "2003": "2003",
		        "2004": "2004",
		        "2005": "2005",
		        "2006": "2006"
		    },
	        "Alfa Spider": {
		        "1979": "1979",
		        "1980": "1980",
		        "1981": "1981",
		        "1982": "1982",
		        "1983": "1983",
		        "1986": "1986",
		        "1987": "1987",
		        "1988": "1988",
		        "1989": "1989",
		        "1990": "1990",
		        "1991": "1991",
		        "1992": "1992",
		        "1993": "1993",
		        "1995": "1995",
		        "1996": "1996",
		        "1997": "1997",
		        "1998": "1998",
		        "1999": "1999",
		        "2000": "2000",
		        "2001": "2001",
		        "2002": "2002",
		        "2003": "2003",
		        "2004": "2004",
		        "2005": "2005",
		        "2006": "2006",
		        "2007": "2007",
		        "2008": "2008",
		        "2009": "2009",
		        "2010": "2010",
		        "2011": "2011"
		    },
	        "Alfasud": {
		        "1981": "1981",
		        "1982": "1982",
		        "1983": "1983",
		        "1984": "1984",
		        "1985": "1985",
		        "1986": "1986"
		    },
	        "Alfetta Serie III/GTV": {
		        "1981": "1981",
		        "1982": "1982",
		        "1983": "1983",
		        "1984": "1984",
		        "1985": "1985",
		        "1986": "1986"
		    },
	        "Giulia": {
		        "2016": "2016",
		        "2017": "2017",
		        "2018": "2018"
		    },
	        "Giulietta": {
		        "1979": "1979",
		        "1980": "1980",
		        "1981": "1981",
		        "1982": "1982",
		        "1983": "1983",
		        "1984": "1984",
		        "1985": "1985",
		        "2010": "2010",
		        "2011": "2011",
		        "2012": "2012",
		        "2013": "2013",
		        "2014": "2014",
		        "2015": "2015",
		        "2016": "2016",
		        "2017": "2017",
		        "2018": "2018"
		    },
	        "MiTo": {
		        "2008": "2008",
		        "2009": "2009",
		        "2010": "2010",
		        "2011": "2011",
		        "2012": "2012",
		        "2013": "2013",
		        "2014": "2014",
		        "2015": "2015",
		        "2016": "2016",
		        "2017": "2017",
		        "2018": "2018"
		    },
	        "Stelvio": {
		        "2017": "2017",
		        "2018": "2018"
		    }
	    }
    }


def index(request):

    for city in cities_array:
        try:
            City.objects.get(name=city["name"])
        except City.DoesNotExist:
            City.objects.create(
                name = city["name"],
                street = city["street"],
                city = city["city"],
                zipcode = city["zipcode"],
                area = city["area"],
                partner = city["partner"],
                lat = city["lat"],
                lng = city["lng"]
            )
    

    return HttpResponse("Cities are created successfully.!")


def upload_car_data(request):

    for car_brand in car_brands:
        try:
            car_brand_obj = CarBrand.objects.get(name=car_brand)
        except CarBrand.DoesNotExist:
            CarBrand.objects.create(
                name=car_brand,
                alias=car_brand
            )
            car_brand_obj = CarBrand.objects.get(name=car_brand)

        for cm_key in car_brands[car_brand]:
            try:
                car_model = CarModel.objects.get(name=cm_key)
            except CarModel.DoesNotExist:
                CarModel.objects.create(
                    car_brand = car_brand_obj,
                    name=cm_key,
                    alias=cm_key
                )
                car_model = CarModel.objects.get(name=cm_key)

            for cy_key in car_brands[car_brand][cm_key]:
                try:
                    CarYear.objects.get(name=cy_key)
                except CarYear.DoesNotExist:
                    CarYear.objects.create(
                        car_model=car_model,
                        name=cy_key,
                        alias=cy_key
                    )

    return HttpResponse("Cars are created successfully.!")
