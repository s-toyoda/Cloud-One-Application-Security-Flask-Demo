# Application Security - Flask demo

A simple Flask app with [Application Security](https://docs.app-security.trendmicro.com/) embedded. 

## Start app

Start the app using the following command:

```
docker run \
--name flask-app-sec \
-d -p 5000:5000 \
-e TREND_AP_KEY=<AP_KEY> \
-e TREND_AP_SECRET=<AP_SECRET> \
oznetnerd/flask-app-sec
```

## Settings

1. Enable the **"Malicious File Upload"** policy.

![alt text](images/policy.png)

2. Upload a file with malware (e.g EICAR test file).

![alt text](images/upload.png)

3. You will be redirected to the default block page:

![alt text](images/block.png)

4. Check events:

![alt text](images/events.png)

5. And details of the malware:

![alt text](images/report.png)

# Contact

* Blog: oznetnerd.com
* Email: will@oznetnerd.com