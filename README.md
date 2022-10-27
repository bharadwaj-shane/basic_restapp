# basic_restapp
 
This is a sample django rest application demonstrating calling an api from a python application simulating long running processes. A sleep method of 20 seconds has been added to simulate the process. 
### 2 api's have been exposed from the application 
  1) <host>/mathcal/ [GET]
  2) <host>/mathcal/calc [POST]

The common method which creates two dataframe of given row and column then randomly fills data in the 2 DF and performs dot project. It then finds the mean and standard deviation of each of the columns, converts the data into a list and passes the data as a json response.

For the API 1 GET request, it creates 2 DF of 10000,10000 and performs the above mentioned operations.
For the API 2 POST requests, pass the data in the following format,
 {
    "row1":10000,
    "row2":10000,
    "col1":10000,
    "col2":10000
}

All the required packages has been listed in requirements.txt which can be installed via the pip statement in a python environment. 

To deploy the application in a server, we will be using gunicorn and nginx to serve as our application interface and web server.

Install gunicorn and nginx in the system. 

### Setup the gunicorn.socket file with the following values

[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target

### Setup the gunicorn.service file with the following values

[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=<hostsystem_username>
Group=www-data
WorkingDirectory=/home/<hostsystem_username>/myprojectdir
ExecStart=/home/<hostsystem_username>/pythonenv/bin/gunicorn \  ### This is path to the gunicorn installation in the python env
          --access-logfile - \
          --workers 3 \
          --threads 3 \
          --bind unix:/run/gunicorn.sock \
          myproject.wsgi:application

[Install]
WantedBy=multi-user.target

--> Refer https://docs.gunicorn.org/en/latest/settings.html#worker-processes for the appropriate values as per the system config.

### values for Nginx's new server block in sites-available directory:

server {
    listen 80;
    server_name <server_domain_or_IP>;

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}



