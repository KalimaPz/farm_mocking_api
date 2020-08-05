from flask import Flask , jsonify

app = Flask(__name__)
# data

water = {
  "main": {
    "EC": 3.22,
    "level": 50,
    "pH": 6.5
  },
  "subLeft": {
    "EC": 1.22,
    "level": 50,
    "pH": 5.5
  },
  "subRight": {
    "EC": 3.41,
    "level": 50,
    "pH": 7.5
  }
}

env = {
  "in": {
    "humd": 65.22,
    "temp": 26.23
  },
  "out": {
    "humd": 42.25,
    "temp": 32.23
  }
} 
info = {
  "farmID": "FARM0007PK",
  "farmName": "SERVESOOK FARM",
  "owner": "BOB MARLEY",
  "staff": [
    "STEVEN",
    "FRANKY"
  ]
}

imageList = [
    'https://th-live-01.slatic.net/p/bbc847afac4930608b2f2e9b06ae1519.jpg',
    'https://s3.amazonaws.com/finegardening.s3.tauntoncloud.com/app/uploads/vg-migration/2018/11/28004024/sage.JPG',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcScYqBgmWO9Jgsv7WbImqc5mqLQFYM_l8XDew&usqp=CAU',
    'https://images.homedepot-static.com/productImages/11b2e243-983f-4750-ae86-d8ca8f62edcf/svn/gurney-s-vegetable-herb-seeds-14592-64_1000.jpg',
    'https://www.prairieviewfarmmarket.com/wp-content/uploads/2016/03/taragon.jpg',
]
# routes 

@app.route('/',methods=['GET'])
def index():
    return jsonify({msg : 'Hello World!'})

@app.route('/api/topic/env')
def getEnvData() :
    return jsonify(env)
@app.route('/api/topic/water',methods=['GET'])
def getWaterData() : 
    return jsonify(water)
@app.route('/api/topic/info',methods=['GET'])
def getInfoData():
    return jsonify(info)

@app.route('/api/topic/getImage', methods=['GET'])
def getImage() : 
    return jsonify(imageList)
# if __name__ == '__main__':
#   app.run(host='0.0.0.0', port=8000, debug=True)
 