## [flask with uwsgi and nginx](flask.mdvsh.co)

code to setup a simple Python application using the Flask micro-framework on Ubuntu (aws-server instance).

### tech

uWSGI application server to launch the application and Nginx to act as a front end reverse proxy.

---

/etc/nginx/sites-available/flask.mdvsh.co
```
server {
        listen 5000;
        server_name flask.mdvsh.co; # managed by Certbot


        location / {
                include uwsgi_params;
                uwsgi_pass unix:/home/ubuntu/src/cs-flash-cards/test_flask/test_flask.sock;
        }

    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/flask.mdvsh.co/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/flask.mdvsh.co/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

}
```

/etc/systemd/system/test_project.service
```
[Unit]
Description=uWSGI instance to serve test_flask project.
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/src/cs-flash-cards/test_flask
Environment="PATH=/home/ubuntu/src/cs-flash-cards/bin"
ExecStart=/home/ubuntu/src/cs-flash-cards/bin/uwsgi --ini test_flask.ini

[Install]
WantedBy=multi-user.target
```

---

