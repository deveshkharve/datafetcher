# datafetcher
simple URL fetcher which fetches any provided URL and displays the resonse as close as possible to the actual URL.

It users redis for persisting results which have already been fetched, hence therefore avoids fetching data from source everytime it is requested.

Tech Stack is based on 
Python3.6
Flask
Redis/  Or can be connected with MySql. Connection class is provided and can be used once connection is configured.
