### RedisPython

The Python interface to the Redis key-value store.
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

After installing redis-py, establish a connection to Redis using redis-py
```
import redis

r = redis.StrictRedis(
    host='hostname',
    port=port,
    password='password')
```

### Publish / Subscribe

Pub/Sub(Publish-Subscribe) pattern is a pattern in which there are three main components, sender, receiver & a broker. The communication is processed by the broker, it helps the sender or publisher to publish information and deliver that information to the receiver or subscriber.

redis-py includes a PubSub object that subscribes to channels and listens for new messages. After creating a PubSub object, channels and patterns can be subscribed to.

After having redis-server, python 3 and Python Redis client installed on your system successfully and run pubsub.py script. The goal of this script is to create a pub/sub pattern that helps users to subscribe to publisher channels and get notified whenever there are updates.

```
[root@p1322-bastion RedisPython]# python3 pubsub.py
Channles list: [b'third-channel', b'second-channel', b'first-channel']
Number of subscribers:  [(b'first-channel', 1), (b'second-channel', 1), (b'third-channel', 1)]
pattern subsciption 2
Unsubscibing channels :1 None
Unsubscribing pattern :1 None
Channels list after unsubscribing [b'second-channel', b'first-channel']
Pattern count after unsubscirbing 1
```

Any publisher can publish through the channel and, the subscriber will receive all the new messages that are published on that particular channel. Redis handles the communication between publisher and subscriber without any hassle.
