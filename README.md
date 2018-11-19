# Python Lab programs

### Getting CGI scripts to work on linux

    1) Install XAMPP
    2) Open /opt/lampp/etc/httpd.conf
    3) Search for "AddHandler" and add .py at the end
    4) Search for '<Directory "/opt/lampp/cgi-bin">'
    5) Change Options to "Options ExecCGI FollowSymLinks Indexes"
    6) Restart xampp