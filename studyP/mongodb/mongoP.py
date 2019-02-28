import pymongo
from bson.objectid import ObjectId

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.mytest;
collection = db["mycollection"]   #指定集合
student = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

student1 = {
    'id': '20170103',
    'name': 'Jordan',
    'age': 30,
    'gender': 'male'
}

student2 = {
    'id': '20170202',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}

# 插入多条数据
# result = collection.insert_many([student1, student2])
# print(result)
# print(result.inserted_ids)

# result = collection.find_one({'name': 'Mike'})
# print(type(result))
# print (result)

#根据id查询   导入objectId方法
# result = collection.find_one({'_id': ObjectId('5c45b3d83520b056985f94f1')})
# print(result)

# results = collection.find({'communityArea':{'$regex':'^西湖'} })   #({'name': {'$regex': '^M.*'}})
# count = collection.find({'communityArea':{'$regex':'^西湖'} }).count()
num = 0
for i in collection.find().limit(1):
        aa = ''
        for a in i.keys():
            aa = aa + a + ','
        print(aa[4:-1])
# print(len(results))
# for result in results:
#     num += 1
#     print(result)
print(num)
