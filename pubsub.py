import redis

r = redis.StrictRedis(host='p630-master.p630.cecc.ihost.com',port=31000,password='root123')
p = r.pubsub()
#channels and patters are subscribed
p.subscribe('first-channel', 'second-channel','third-channel')
p.psubscribe('*-channel', 'pattern2')
#sending some data for some channels
r.publish('first-channel', 'first data entered')
r.publish('second-channel', 'This data is only for second-channel subscribers')
r.publish('first-channel', 'first channel data')
# print list of channels
print("Channles list:" ,r.pubsub_channels())
#To check number of subscriber
print("Number of subscribers: ",r.pubsub_numsub('first-channel' , 'second-channel', 'third-channel'))

#To check number of subscription o the pattern
print("pattern subsciption", r.pubsub_numpat())

# to unsubscribe some channels
print("Unsubscibing channels", p.unsubscribe('third-channel'))
print("Unsubscribing pattern",p.punsubscribe('pattern2'))
print("Channels list after unsubscribing", r.pubsub_channels())
print("Pattern count after unsubscirbing",r.pubsub_numpat())
