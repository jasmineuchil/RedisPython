### RedisPython

## Using Redis with Python

Redis-py requires a running Redis server

## Steps to deploy the Redis Application on OpenShift Container Platform

Git clone this repository to your server -
```
cd $HOME/
git clone https://github.com/jasmineuchil/RedisPython.git
cd RedisPython
```

Create a new project
```
oc new-project ibm -description="IBM" --display-name="ibm"
oc project ibm
```

Deploy Service and Deployment config files via

```
oc create -f redis-service.yaml
oc create -f redis-deployment.yaml

```

To check the status of pods
```
[root@p1316-bastion redis]# oc get svc
NAME    TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
redis   NodePort   172.30.68.207   <none>        6379:31000/TCP   5s
[root@p1316-bastion redis]# oc get po
NAME                           READY   STATUS    RESTARTS   AGE
redis-7bc5d7d8bb-wq4zd         1/1     Running   0          55s
```

To validate login to container :
```
[root@p1316-bastion redis]# oc rsh redis-7bc5d7d8bb-wq4zd
$ redis-cli -h p1316-master.p1316.cecc.ihost.com -p 31000
p1316-master.p1316.cecc.ihost.com:31000> ping
PONG
```

## Using Redis with Python

To start using Redis, first we need to install Python environment in OCP. Either you can use your system-wide Python installation or you can build new python app.

To install redis in your Openshift system, make sure you have installed python3 (along with PIP) Or you can even build python app using oc new-app and validate if pod is created successfully by using oc get pod command.

To install redis-py
` pip install redis `

After installing redis-py, establish a connection to Redis using redis-py
```
import redis

r = redis.StrictRedis(
    host='hostname',
    port=port,
    password='password')
```

### Publish / Subscribe

Pub/Sub aka Publish-Subscribe pattern is a pattern in which there are three main components, sender, receiver & a broker. The communication is processed by the broker, it helps the sender or publisher to publish information and deliver that information to the receiver or subscriber.

redis-py includes a PubSub object that subscribes to channels and listens for new messages. After creating a PubSub object, channels and patterns can be subscribed to.

After having redis-server, python 3 and Python Redis client installed on your system successfully and run pubsub.py script. The goal of this script is to create a pub/sub pattern that helps users to subscribe to publisher channels and get notified whenever there are updates.

Any publisher can publish through the channel and, the subscriber will receive all the new messages that are published on that particular channel. Redis handles the communication between publisher and subscriber without any hassle.
