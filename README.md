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