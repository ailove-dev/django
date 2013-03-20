Django Ailove Edition
=======================

What's inside?
--------------

* Django
* South Migrations
* Grappelli Filebrowser
* Grappelli Admin Interface
* Custom Template Tags (utilities.templatetags)
* Advanced Model Capabilities (utilities.capable)
* Unique Names for Uploaded Files (utilities.uploadrename)

Preparations
------------

You need to make some preparations for your django project to work properly

Python
~~~~~~~~~~~~~~~~~~~~~~~

At first you need to install Python. Every Python version installs itself with a MAJOR version number, for example
/usr/local/lib/python2.6 or /usr/local/lib/python2.7 etc, so if you want to make your python version PRIMARY on
the system, then you run make install and it will create a symlink from /usr/local/bin/python2.7 to /usr/local/bin/python,
if you don't want such a behaviour, you run make altinstall and no symlink will be created. Now let's download latest
python version from 2.x branch, extract it somewhere, cd into dir and run the following commands::

    ./configure --prefix=/usr/local
    make
    sudo make install

mod_wsgi
~~~~~~~~~~~~~~~~~~~~~~~

Now you need to install mod_wsgi for apache web server. If you don't use apache you have a lot of other options, but we use
mod_wsgi and we are happy with it, so if you use another web server you are on your own.

If you are a mac user like me, first run the following command (I assume you have XCode installed)::

    sudo ln -s /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/ /Applications/Xcode.app/Contents/Developer/Toolchains/OSX10.8.xctoolchain

Then download the last version of mod_wsgi, extract it somewhere, cd into dir and run the following commands::

    ./configure --with-python=/usr/local/bin/python
    make
    sudo make install

Then add the following line to your httpd.conf and restart your apache::

    LoadModule wsgi_module libexec/apache2/mod_wsgi.so

Of course you may have different paths than me, so go figure out your paths yourself.

Installation
------------

Now you are ready to install Django. Let's guess you have project named "project". To create project run the
following commands::

    mkdir project
    cd project
    mkdir cache conf data repo tmp logs
    echo -e "DB_HOST = 127.0.0.1\nDB_NAME = django\nDB_USER = user\nDB_PASSWORD = " > conf/database
    chmod 777 *
    git clone https://github.com/ailove-dev/django.git repo/dev
    cd repo/dev
    rm -rf .git
    git init
    git add .gitignore *
    git commit -m "Initial commit"

About directories structure
~~~~~~~~~~~~~~~~~~~~~~~

* cache - for framework cache
* conf - host independed configuration INI files parsed by app/config.py file
* data - directory for uploaded files. Use directory alias for virtual host Alias /data /path/to/project/data
* repo - this directory is used to store git repo. We have placed it into repo/dev directory.
* tmp - use this dir to store tmp files as session and etc.
* logs - store the logs here

Virtualenv
~~~~~~~~~~~~~~~~~~~~~~~

Now you need to install virtualenv. This is a tool to create isolated python environments and it's really very useful.
Download last version of virtualenv, extract it somewhere, cd into dir and run the following command::

    sudo /usr/local/bin/python setup.py install --prefix=/usr/local

Great, you have just installed your global virtualenv. Now you have to make an isolated environment for you project::

    cd into_project_dir
    /usr/local/bin/virtualenv --no-site-packages --distribute python

Now you have a directory called python in your project's dir. To activate your project's isolated environment run::

    source python/bin/activate

To install some package for the project run::

    pip install PACKAGE

To list all installed packages run::

    pip list

To list all packages that have newer versions available, run::

    pip list --outdated

To deactivate your isolated environment run::

    deactivate

Project Initialization
~~~~~~~~~~~~~~~~~~~~~~~

Now you have to run some commands to initialize your project. You have to activate your project's isolated environment
like I explained in previous step for this commands to work properly, I will remind you how to do it::

    source python/bin/activate

Now you need to install latest version of some useful packages::

    pip install -r repo/dev/requirements.txt

Then you need to initialize your database and create an admin superuser::

    python repo/dev/manage.py syncdb

Lastly you need to move some static files, so your webserver has access to them::

    python repo/dev/manage.py collectstatic

Add admin user
~~~~~~~~~~~~~~

If for some reason you didn't create admin superuser in previous step you can do it with the following command::

    python repo/dev/manage.py createsuperuser

Cleaning
~~~~~~~~~~~~~~

Don't forget to deactivate your isolated environment when your are done::

    deactivate

Login to Django Admin
~~~~~~~~~~~~~~~~~~~~~

Open http://project-url.lo/admin in your browser and fill the authorization form

Enjoy!

That's actually all you need to successfully run a django project. Your next step will be to create an app
in your project and start developing. Django has great documentation so you have to read it thoroughly to do
everything in a proper way. Happy coding!