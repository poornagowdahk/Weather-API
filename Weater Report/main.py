from flask import Flask, render_template, request
import requests, json
from datetime import datetime
app = Flask(__name__)  
@app.route('/', methods=['POST','GET'])  
def index():  
      return render_template("index.html")  




@app.route("/review", methods=['POST','GET'])
def results():
    #    return render_template("results.html")
        if request.method == "POST":
            try: 
                api_key = "6d7184976a78fe82282c295ea0a10bee"
                base_url = "http://api.openweathermap.org/data/2.5/weather?"
                city_name = request.form["content"]
                complete_url = base_url + "appid=" + api_key + "&q=" + city_name
                print(complete_url)
                response = requests.get(complete_url)

                # t = response.json()['data']['timelines'][0]['intervals'][0]['values']['temperature']
                x = response.json()
                print(x)
                reviews=[]
                if x["cod"] != 404:
                   
                    try:
                       y = x["main"]
                       current_temperature = y["temp"]
                    except:
                        print("temparature not found")
                    try:
                        Celsius = (y["temp"] - 273.15)
                    except:
                        print("celsius not found")
                    try:

                       current_pressure = y["pressure"]
                    except:
                        print("pressure not found")
                    try:
                        current_humidity = y["humidity"]
                    except:
                        print("humidity not found")
                    try:
                        date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
                    except:
                        print("date time not found")
                    try:
                        z = x["weather"]
                        weather_description = z[0]["description"]
                    except:
                        print("weather desc not found")

                    
                    mydict = {"current_temperature":current_temperature,'Celsius':Celsius,"current_pressure":current_pressure,"current_humidity":current_humidity,"date_time":date_time,"weather_description":weather_description}
                    reviews.append(mydict)
                    print(reviews)

                return render_template('results.html', reviews=reviews[0:2])
            except:
              pass
           
        else:
            print("not found")
if __name__ == '__main__':  
   app.run(debug=True)