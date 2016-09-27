# guessanumber

You need to enable cgi module to run with ubuntu 14.04.

1) Enable/Disable below module from shell
	sudo a2dismod mpm_event
	sudo a2enmod mpm_prefork cgi

2) Enable cgi-bin from conf file
	1) find this file : /etc/apache2/sites-enabled/000-default.conf
	2) find "DocumentRoot /var/www/html" or "DocumentRoot /var/www" in above conf file
	3) Add following line after "DocumentRoot /var/www/html" according apache server's default configuration
		ScriptAlias /cgi-bin/ "/var/www/html/cgi-bin/"
		OR
		ScriptAlias /cgi-bin/ "/var/www/cgi-bin/"

3) Restart server with below command
	sudo service apache2 restart

4) Make "cgi-bin" directory on following location 
	"var/www" or "var/www/html"

5) put demo.py file in "cgi-bin"

6) Put below url in browser
	http://localhost/cgi-bin/demo.py
	http://YOURIPADDRESS/cgi-bin/demo.py



