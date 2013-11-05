from pymongo import MongoClient

c = MongoClient()
db = c.talks

if 'test_data' not in db.collection_names():

    collection = db.test_data

    a = {
	    "link" : "https://www.youtube.com/watch?v=OSGv2VnC0go",
	    "rating" : 0,
	    "submitter" : "Mike Grimes",
	    "author" : "Raymond Hettinger"
	    }

    b = {
	    "link" : "https://www.youtube.com/watch?v=UScm9avQM1Y",
	    "rating" : 0,
	    "submitter" : "Mike Grimes",
	    "author" : "Big Think"
	    }

    collection.insert(a)
    collection.insert(b)
