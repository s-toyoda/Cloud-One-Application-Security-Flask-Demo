# Application Security - Flask demo

A simple Flask app with [Application Security](https://docs.app-security.trendmicro.com/) embedded. 

```
docker run \
--name flask-app-sec \
-d -p 5000:5000 \
-e TREND_AP_KEY=<AP_KEY> \
-e TREND_AP_SECRET=<AP_SECRET> \
oznetnerd/flask-app-sec
```