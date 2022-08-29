# HOW to run locally
1) Make sure you've pulled all sub-directories, [CMD](https://stackoverflow.com/questions/1030169/pull-latest-changes-for-all-git-submodules)
2) You need a ngrok instance to be running locally so you can publish yourself to the internet
3) Install ngrok
   1) `brew install --cask ngrok`
```bash
```shell
ngrok http 5555
```
4) Copy the url to the clipboard
5) Now we need to setup the docker-compose env file
6) Pick the .env-local file and ask the admin for keys that need to replaced
7) Get `firebase-service-account.json` and `juspay.pem` from admin and place them under the path `biap-client-node-js/config/dev`
8) Run
```shell
docker-compose -f docker-compose-for-local.yaml --env-file .env-local up -d
``` 
9) Open `http://localhost`