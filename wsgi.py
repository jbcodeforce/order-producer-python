from flask import Flask
import os

try:
    KAFKA_BROKERS = os.environ['KAFKA_BROKERS']
except KeyError:
    # KAFKA_BROKERS = "kafka03-prod02.messagehub.services.us-south.bluemix.net:9093,kafka01-prod02.messagehub.services.us-south.bluemix.net:9093,kafka02-prod02.messagehub.services.us-south.bluemix.net:9093,kafka05-prod02.messagehub.services.us-south.bluemix.net:9093,kafka04-prod02.messagehub.services.us-south.bluemix.net:9093"
    KAFKA_BROKERS = "localhost:9092"

application = Flask(__name__)

def createOrder(id):
    print('Create order')
    data = {"orderID": id, 
        "productID": "FreshFoodItg", 
        "customerID": "Customer000",
        "quantity": 180, 
        "pickupAddress": {"street": "main","city": "Oakland","country":"USA","state":"CA","zipcode": "95000"},
        "destinationAddress": {"street": "bstreet","city": "Beijing","country":"China","state":"NE","zipcode": "09000"},
        "pickupDate": "2019-05-25",
        "expectedDeliveryDate": "2019-06-25"}
    containerEvent = {"orderID": id,"timestamp": int(time.time()),"type":"OrderCreated","payload": data}
    return containerEvent


@application.route("/")
def hello():
    print(KAFKA_BROKERS)
    return "Jbcodeforce on Openshift Hello to you! v01"

@application.route("/order")
def getOrder():
    return createOrder("10")

if __name__ == "__main__":
    application.run()
    