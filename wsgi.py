from flask import Flask, request
import os, time, jsonify
from KcProducer import KafkaProducer 

try:
    KAFKA_BROKERS = os.environ['KAFKA_BROKERS']
except KeyError:
    KAFKA_BROKERS = "localhost:9092"

try:
    KAFKA_APIKEY = os.environ['KAFKA_APIKEY']
except KeyError:
    print("The KAFKA_APIKEY environment variable not set... assume local deployment")

try:
    KAFKA_ENV = os.environ['KAFKA_ENV']
except KeyError:
    KAFKA_ENV='LOCAL'

application = Flask(__name__)

orders = []

def createOrder(oid):
    print('Create order')
    data = {"orderID": oid, 
        "productID": "FreshFoodItg", 
        "customerID": "Customer000",
        "quantity": 180, 
        "pickupAddress": {"street": "main","city": "Oakland","country":"USA","state":"CA","zipcode": "95000"},
        "destinationAddress": {"street": "bstreet","city": "Beijing","country":"China","state":"NE","zipcode": "09000"},
        "pickupDate": "2019-05-25",
        "expectedDeliveryDate": "2019-06-25"}
    containerEvent = {"orderID": oid,"timestamp": int(time.time()),"type":"OrderCreated","payload": data}
    return containerEvent



@application.route("/")
def hello():
    print(KAFKA_BROKERS)
    return "Jbcodeforce on Openshift Hello to you! v01"

@application.route("/order", methods = ['GET'])
def getOrder():
    order= createOrder("10")
    return jsonify(order)
    
@application.route("/order", methods = ['POST'])
def createOrder():
    if not request.json or not 'orderID' in request.json:
        abort(400)
    print(request.json)
    order = request.json
    d = datetime.datetime(2019, 4, 13,10,0,14)
    evt = {"orderID": orderID,"timestamp": int(datetime.datetime.timestamp(d)),"type":"OrderCreated","payload": order}
    kp = KafkaProducer(KAFKA_ENV,KAFKA_BROKERS,KAFKA_APIKEY)
    kp.prepareProducer("OrderProducerPython")
    kp.publishEvent('orders',evt,"orderID")
    return jsonify(evt)

if __name__ == "__main__":
    application.run(debug=True)
    
