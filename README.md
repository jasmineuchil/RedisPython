### RedisPython

The Python interface to the Redis key-value store. Redis is a popular key-value data store known for its speed and flexibility. In this, I described some of the more commonly discussed Redis features with python to get our hands on the essence of Redis. Here we are using Redis as a Publisher/Subscriber platform. In this pattern, publishers can issue messages to any number of subscribers on a channel.

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
[root@p1322-bastion RedisPython]# oc get svc
NAME    TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
redis   NodePort   172.30.23.193   <none>        6379:31000/TCP   47m
[root@p1322-bastion RedisPython]# oc get po
NAME                     READY   STATUS    RESTARTS   AGE
redis-7bc5d7d8bb-v72tg   1/1     Running   0          41m
```

To validate login to container :
```
[root@p1322-bastion cecuser]# oc rsh redis-7bc5d7d8bb-v72tg
$ redis-cli -h p1322-master.p1322.cecc.ihost.com -p 31000 -a "root123"
Warning: Using a password with '-a' or '-u' option on the command line interface may not be safe.
p1322-master.p1322.cecc.ihost.com:31000> ping
PONG
p1322-master.p1322.cecc.ihost.com:31000>
$ exit

```

## Using Redis with Python

To start using Redis, first we need to install Python environment in OCP. Either you can use your system-wide Python installation or you can build new python app.

To install redis in your Openshift system, make sure you have installed python3 (along with PIP) Or you can even build python app using oc new-app and validate if pod is created successfully by using oc get pod command.

To install redis-py
` pip install redis `

After installing redis-py, establish a connection to Redis using redis-py by importing redis and mentioning hostname, port and password. In pubsub.py script change hostname, port and password accordingly.

### Publish / Subscribe

Pub/Sub(Publish-Subscribe) pattern is a pattern in which there are three main components, sender, receiver & a broker. The communication is processed by the broker, it helps the sender or publisher to publish information and deliver that information to the receiver or subscriber.

redis-py includes a PubSub object that subscribes to channels and listens for new messages. After creating a PubSub object, channels and patterns can be subscribed to.

After having redis-server, python 3 and Python Redis client installed on your system successfully and run pubsub.py script. The goal of this script is to create a pub/sub pattern that helps users to subscribe to publisher channels and get notified whenever there are updates.

```
[root@p1322-bastion RedisPython]# python3 pubsub.py
Channels list: [b'third-channel', b'second-channel', b'first-channel']
Number of subscribers:  [(b'first-channel', 1), (b'second-channel', 1), (b'third-channel', 1)]
pattern subscription 2
Unsubscribing channels :1 None
Unsubscribing pattern :1 None
Channels list after unsubscribing [b'second-channel', b'first-channel']
Pattern count after unsubscribing 1
```

Any publisher can publish through the channel and, the subscriber will receive all the new messages that are published on that particular channel. Redis handles the communication between publisher and subscriber without any hassle.

In pubsub.py script we had published data only on first and second channel. In first-channel we had published two datas and it is only available for the users who subscribed for first-channel. In second channel we had published only one data and it is available only for second-channel subscribers. We didn’t publish any data in third-channel, so third-channel subscribers will not receive any data.
```
r.publish('first-channel', 'first data entered')
r.publish('second-channel', 'This data is only for second-channel subscribers')
r.publish('first-channel', 'first channel data')
```

To validate let’s login to all three channels by subscribing all three channels and check the data published:
First-channel:
```
p1322-master.p1322.cecc.ihost.com:31000> SUBSCRIBE first-channel
Reading messages... (press Ctrl-C to quit)
1) "subscribe"
2) "first-channel"
3) (integer) 1
1) "message"
2) "first-channel"
3) "first data entered"
1) "message"
2) "first-channel"
3) "first channel data"
```

Second-channel :
```
p1322-master.p1322.cecc.ihost.com:31000> SUBSCRIBE second-channel
Reading messages... (press Ctrl-C to quit)
1) "subscribe"
2) "second-channel"
3) (integer) 1
1) "message"
2) "second-channel"
3) "This data is only for second-channel subscribers"
```

Third-channel:
```
p1322-master.p1322.cecc.ihost.com:31000> SUBSCRIBE third-channel
Reading messages... (press Ctrl-C to quit)
1) "subscribe"
2) "third-channel"
3) (integer) 1
```
