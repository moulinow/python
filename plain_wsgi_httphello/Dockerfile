#https://davescripts.com/docker-container-with-centos-7-apache-mod-wsgi-python-3
FROM centos:7

# Install Apache
RUN yum -y update
RUN yum -y install httpd httpd-tools

# Install Python 3
RUN yum -y install python3

# Install mod_wsgi
RUN yum -y install mod_wsgi

# Update Apache Configuration
RUN sed -E -i -e '/<Directory "\/var\/www\/html">/,/<\/Directory>/s/AllowOverride None/AllowOverride All/' /etc/httpd/conf/httpd.conf

RUN echo "" >> /etc/httpd/conf/httpd.conf \
 && echo "WSGIScriptAlias / /var/www/html/wsgi.py" >> /etc/httpd/conf/httpd.conf \
 && echo "<Directory /var/www/html>" >> /etc/httpd/conf/httpd.conf \
 && echo "<Files wsgi.py>" >> /etc/httpd/conf/httpd.conf \
 && echo "Require all granted" >> /etc/httpd/conf/httpd.conf \
 && echo "</Files>" >> /etc/httpd/conf/httpd.conf \
 && echo "</Directory>" >> /etc/httpd/conf/httpd.conf

EXPOSE 80

COPY ./wsgi.py /var/www/html/wsgi.py

# Start Apache
CMD ["/usr/sbin/httpd","-D","FOREGROUND"]

#build with docker build -t image_apache_python .
#Run   with docker run -it -p 8080:80 image_apache_python
