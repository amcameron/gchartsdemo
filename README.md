Google Charts Demo Using Flask
==============================

A simple demo to show how you can use Flask and Jinja2 to quickly and easily
pass information into Google Charts.  You can get the data from anywhere and
you don't have to implement your own [Data Source]
(http://code.google.com/apis/chart/interactive/docs/dev/implementing_data_source_overview.html)
in order to use it!

Setup
-----

    $ git clone git://github.com/amcameron/gchartsdemo.git
    $ pip install flask

(You're using a [virtualenv](http://www.virtualenv.org/en/latest/index.html),
right?)

    $ python charts.py

Setup complete!  Connect to `http://localhost:5000/charts/` in your browser.

Credits
-------

* [Flask](http://flask.pocoo.org/)
* [Jinja2](http://jinja.pocoo.org/docs/)
* [Google Charts](http://code.google.com/apis/chart/interactive/docs/index.html)
and the [Google Charts Gallery]
(http://code.google.com/apis/chart/interactive/docs/gallery.html)
