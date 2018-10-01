# Geocoder that parses structured address components using the Google Geocoding API

**Output**
<img src="https://cl.ly/b581a495a983/Image%2525202018-10-01%252520at%25252010.54.26%252520AM.png">

## How does it work?

Copy your raw address data into input.csv. Every address on a new line. Leave the first line with 'address'.
The program will output the results as a clean CSV file you can use in your projects.
Uncomment line 13 in get_address.py if you want to see the requested output in your terminal

Clone the repo and run the script in command prompt or terminal as:

```bash
python main.py
```

Once complete, you will have a CSV file called result.csv with the formatted address data.

### Google Maps Geocoding API

Google Maps Geocoding API is a service that provides geocoding and reverse geocoding for an address.

Each Google Maps Web Service request requires an API key that is freely available with a Google Account at Google Developers Console. The type of API key you need is a Server key.

## How to get an API Key

- Visit the Google Maps Platform Page <a href="https://cloud.google.com/maps-platform">Here</a>
- Create a new project or select one of your existing ones.
- Enable the Geocoding API.
- Create a new Server Key.
- Add your key to main.py

**Important: Do not ever share your API Key! Keep them secure.**
