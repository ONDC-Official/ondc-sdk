# ondc-sandbox

to build
add following file in .env to build
```bash
REACT_APP_BASE_URL=<values>
REACT_APP_FIREBASE_API_KEY=<values>
REACT_APP_FIREBASE_AUTH_DOMAIN=<values>
REACT_APP_GOOGLE_API_KEY=<values>
```

to deploy docker-compose

1) copy docker-compose-with-images.yaml
2) add .env file
3) git clone
```bash
git clone https://github.com/Open-network-for-digital-commerce/biap-client-node-js.git
scp -r biap-client-node-js/config <instance-name>:~/biap-client-node-js/
```
4) git clone
```bash
git clone  https://github.com/Open-network-for-digital-commerce/biap-app-ui-front.git
```
5) scp init-letsencrypt.sh <instance-name>:~/   
6) docker-compose build


```bash
docker build --platform linux/x86_64  -t navdeep710/ondc-python-protocol-layer:v2 . && docker push navdeep710/ondc-python-protocol-layer:v2
docker build --platform linux/x86_64  -t navdeep710/ondc-protocol-layer-server:v3 . && docker push navdeep710/ondc-protocol-layer-server:v3
docker build --platform linux/x86_64  -t navdeep710/ondc-client-layer-server:v3 . && docker push navdeep710/ondc-client-layer-server:v3

```

adding following at the time of certificates is very important

```nginx configuration
location /.well-known/acme-challenge/ {
        root /var/www/certbot;
    }
```

# HOW to run locally
1) you need a ngrok instance to be running locally so you can publish yourself to the internet
2) install ngrok
   1) brew install --cask ngrok 
```bash
```shell
ngrok http 8080
```
3) copy the url to the clipboard
4) now we need to setup the docker-compose env file
5) pick the .env-local file and ask the admin for keys that need to replaced
6) run
```shell
docker-compose -f docker-compose-without-ssl.yaml up -d
``` 