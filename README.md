# Kafka producer with flask

To build with s2i

```
s2i build --copy .  centos/python-36-centos7 ibmcase/orderproducer
```

To run

```
docker run -p 8080:8080 ibmcase/orderproducer

```