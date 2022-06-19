
mkdir -pv /var/www/app
cp /codes/nginx/index.html /var/www/app/index.html
cp /codes/nginx/sites-enabled/app /etc/nginx/sites-enabled/app
service nginx restart
python3 /codes/app/app.py