# Web Stack Debugging #2 Postmortem
## Summary
Initially, our Nginx server was running under the `root` user. For security purposes, we changed our Nginx settings so that it runs under the `nginx` user.

## Timeline
2019-1-17 
* *14:51 PST* - Engineer discovered that Nginx was running under Root user
* *14:56 PST* - Killed Apache processes on server
* *14:58 PST* - Checked nginx.conf file. Changed user setting to 'nginx'.
* *15:03 PST* - Checked default file for sites-enabled. Allowed server to listen to all active IPs on port 8080.
* *15:08 PST* - Restarted Nginx server.
* *15:10 PST* - Server is now running as `Nginx` user and is listening to all active IPs on port 8080.

## Root Cause and Resolution
An engineer was doing maintence on the server under the root user and never switched back to the Nginx user. To prevent this from happening again, I edited the nginx config file to automatically default to use the `nginx` user. Also, to make sure that the server was listening to all active IPs on port 8080, I edited the default file for sites-enabled. I restarted the server and was now running under the `nginx` user and listening to all active IPs on port 8080.

## Corrective and Preventative Measures
* Add monitoring to users on server
* Restrict privileges for certain users
