talks.io
========

A user-based programming/tech talks aggregator written in Python, using Flask and MongoDB.

Requirements

    pip install pymongo
    pip install flask

Before running, make sure you have a mongodb instance running:

    mongod &

To preload the database with test data:

    python initdb.py

To run the application:

    python talks.py
