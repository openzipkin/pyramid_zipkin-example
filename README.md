# Basic example showing distributed tracing across python apps
This is an example app where two pyramid (python) services collaborate on an http request. Notably, timing of these requests are recorded into [Zipkin](http://zipkin.io/), a distributed tracing system. This allows you to see the how long the whole operation took, as well how much time was spent in each service.

Here's an example of what it looks like
<img width="972" alt="zipkin screen shot" src="https://cloud.githubusercontent.com/assets/64215/19347100/bf76a270-9179-11e6-80bb-bd6ccfe7f7f4.png">

This example was ported from similar examples, such as [Spring Boot](https://github.com/openzipkin/sleuth-webmvc-example).

# Implementation Overview

Web requests are served by [Pyramid](http://www.pylonsproject.org/) routes, and tracing is automatically performed for you by [pyramid_zipkin](https://github.com/Yelp/pyramid_zipkin).

This example has two services: frontend and backend. They both report trace data to zipkin. To setup the demo, you need to start frontend.py, backend.py and Zipkin.

## Setup

Before you start anything, you'll need to download the libraries used in this demo:
```bash
# get the latest version of pyramid_zipkin
$ pip install pyramid_zipkin -U
# install the example
$ python setup.py install
```

You'll also want to download zipkin.
```bash
$ wget -O zipkin.jar 'https://search.maven.org/remote_content?g=io.zipkin.java&a=zipkin-server&v=LATEST&c=exec'
```

## Starting the Services
In a separate tab or window, start each of [frontend.py](./frontend.py) and [backend.py](./backend.py):
```bash
$ python frontend.py
$ python backend.py
```

Next, run [Zipkin](http://zipkin.io/), which stores and queries traces reported by and above services.

```bash
$ java -jar zipkin.jar
```

## Running the example

Once the services are started, open http://localhost:8081/
* This will call the backend (http://localhost:9000/api) and show the result, which defaults to a formatted date.

Now, you can view traces that went through the frontend via http://localhost:9411/?serviceName=frontend
* This is a locally run zipkin service which keeps traces in memory
