# Tickermaster-API

This app contains a REST API that will query TicketMaster's API to get event details.

The request.json file can be used to modify the query parameters

To run the app:

1. Create a virtual env

2. Open terminal and type:
```
pip install -r requirements.txt

```

3. In a terminal window and type: 
```
python main.py 

```

This will run the REST API using Flask

4. Open another terminal window and type: 
``` 
python script.py 

```

This will send a POST request to the REST API in main.py, store the returned data in a file, and store that file in AWS S3. 