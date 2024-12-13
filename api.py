from flask import Flask
from flask_restful import Resource, Api, reqparse

#instantiate
app = Flask(__name__)
api = Api(app)

#Create a Dictionary
COUNTRIES = {
    "1": {"country": "Ghana", "capital": "Accra"},
    "2": {"country": "Nigeria", "capital": "Abuja"},
    "3": {"country": "Kenya", "capital": "Nairobi"},
    "4": {"country": "South Africa", "capital": "Pretoria"},
    "5": {"country": "Egypt", "capital": "Cairo"},
    "6": {"country": "Morocco", "capital": "Rabat"},
    "7": {"country": "Ethiopia", "capital": "Addis Ababa"},
    "8": {"country": "Uganda", "capital": "Kampala"},
    "9": {"country": "Tanzania", "capital": "Dodoma"},
    "10": {"country": "Senegal", "capital": "Dakar"},
    "11": {"country": "Zimbabwe", "capital": "Harare"},
    "12": {"country": "Cameroon", "capital": "Yaoundé"},
    "13": {"country": "Ivory Coast", "capital": "Yamoussoukro"},
    "14": {"country": "Zambia", "capital": "Lusaka"},
    "15": {"country": "Gabon", "capital": "Libreville"},
    "16": {"country": "Mali", "capital": "Bamako"},
    "17": {"country": "Ghana", "capital": "Accra"},
    "18": {"country": "Benin", "capital": "Porto-Novo"},
    "19": {"country": "Botswana", "capital": "Gaborone"},
    "20": {"country": "Namibia", "capital": "Windhoek"},
    "21": {"country": "Mozambique", "capital": "Maputo"},
    "22": {"country": "Angola", "capital": "Luanda"},
    "23": {"country": "Rwanda", "capital": "Kigali"},
    "24": {"country": "Sudan", "capital": "Khartoum"},
    "25": {"country": "Chad", "capital": "N'Djamena"},
    "26": {"country": "Liberia", "capital": "Monrovia"},
    "27": {"country": "Sierra Leone", "capital": "Freetown"},
    "28": {"country": "Madagascar", "capital": "Antananarivo"},
    "29": {"country": "Malawi", "capital": "Lilongwe"},
    "30": {"country": "Togo", "capital": "Lomé"}
}

#define request parser
parser = reqparse.RequestParser()
parser.add_argument("name", required=False, type=str, location='json', help='Name of Country')
parser.add_argument("capital", required=False, type=str, location='json', help='The capital city')

#Create a resource class
class CountriesList(Resource):
    def get(self):
        return COUNTRIES
    
    def post(self):
        args = parser.parse_args()
        country_id = int(max(COUNTRIES.keys())) + 1

        country_id = str(country_id)
        COUNTRIES[country_id] = {
            "name":args["name"],
            "capital":args["capital"]
        }
        return COUNTRIES[country_id], 201

#add resource class to the API and reference the endpoint on which it will be available
api.add_resource(CountriesList, '/countries')


#new class for CRUD operations
class CountryEdit(Resource):
    def get(self, country_id):
        if country_id not in COUNTRIES:
            return 'Not Found', 404
        else:
            return COUNTRIES[country_id], 200

    def put(self, country_id):
        args = parser.parse_args()
        print(f"Parsed arguments: {args}")
        if country_id not in COUNTRIES:
            return 'Not Found', 404
        else:
            country = COUNTRIES[country_id]
            country["country"] = args.get("name", country["country"])
            country["capital"] = args.get("capital", country["capital"])
            return country, 200
    
    def delete(self, country_id):
        if country_id not in COUNTRIES:
            return 'Not Found', 404
        else:
            del COUNTRIES[country_id]
            return '', 204

#reference the endpoint on which the CountryEdit class will be available
api.add_resource(CountryEdit, '/countries/<country_id>')