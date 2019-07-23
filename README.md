# Kafka producer with flask

This is a simple example of using kafka producer in python within a flask application to expose a POST operation for creating order and publish "order created" events. The events are sent to the kafka topic `orders` created in IBM Event Stream service on IBM Cloud.

This sample is used to validate an Event Stream deployment, with this code running in an Openshift cluster.

To deploy the code to an openshift cluster do the following:

1. Login to the cluster. 

    ```
    oc login -u apikey -p <apikey> --server=https://...
    ```

1. Create a project if not done already:

    ```
    oc  new-project order-producer-python --description="A kafka producer with python"
    ```

1. Create an app from the source code, and use source to image build process to deploy the app:

    ```
    oc new-app python:latest~https://github.com/jbcodeforce/order-producer-python -name order-producer-python
    ```

    Then to track the deployment progress:
    ```
    oc logs -f bc/order-producer-python
    ```
    The dependencies are loaded, the build is scheduled and executed, the image is uploaded to the registry, and started.


1. Set environment variables

    For Broker URLs
    ```
    oc set env dc/order-producer-python KAFKA_BROKERS=kafka03-prod02.messagehub.services.us-south.blu....
    ```

    For apikey:
    ```
    oc set env dc/order-producer-python KAFKA_APIKEY=""
    ```


## Build and run locally

To build with s2i CLI:

```
s2i build --copy .  centos/python-36-centos7 ibmcase/orderproducer
```

To run locally

```
docker run -p 8080:8080 ibmcase/orderproducer
```
