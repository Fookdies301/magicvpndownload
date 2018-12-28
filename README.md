# magicvpndownload
Heroku app to download files in US server and get that using an API

#### When to use ???
Lets say you need to download files from a website that opens only in US location. For the purpose you have written a selenium script, and unfortunately your production server is in Europe. So in that case this app might be your free/easy VPN kind of solution to use.

#### Stacks touched:
1. `Dropbox API` to download files to the dropbox file and generate temporary download link which will be returned by the API
2. `Gmail API` to send notification
3. Restricts many request from one IP address in per hour, per day basis
4. Uses `flask`, `python 3`,
5. Free heroku server for deployment

#### How to deploy ???
