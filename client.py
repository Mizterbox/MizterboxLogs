import requests, numpy as np, time
from time import gmtime, strftime, localtime

sprinklerid = np.random.randint(100,size=100)
address = np.random.randint(1000,size=100)
status = np.random.randint(1000,size=100)

actualsprinkids = [1,2,3,4,5]
status = ['Running Active', 'Restarting','Connecting to Wifi', 'Connecting to Internet']

while True:
    res = requests.post('http://localhost:5000/sprinklerlogs/', json={
    "id":int(np.random.choice(sprinklerid,size=1)[0])%len(actualsprinkids),
    "status":np.random.choice(status,size=1)[0],
    })

    if res.ok:
        print (res.json())
    time.sleep(2)
