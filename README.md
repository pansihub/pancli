# pancli
pancli (also known as Pansi Cli), is a tool for running scrapy spider or interacting to ScrapyDD server.

pancli give some useful supplymentary functions to scrapy command line, some of the functions are:
1. Execute spider from a egg packaged project.
2. Install package required libraries at run-time if necessary.
3. Package a scrapy project into egg.


# Installation
pancli is available on pypi, you can install it by simply run:

```
pip install pancli
```

# Usages
## Run a spider

Run a spider is very easy by executing `pancli crawl {spider_name}`, the command is compatiable with `scrapy crawl`

One special and the most wonderful parameter is the `-f ` parameter, which specifies a FIGURE file in which all settings/parameters/plugins of a spider can be writen as a simple JSON/YAML file. If you run spider very often, FIGURE file can save tons of time.

FIGURE fields:

* spider: the target spider name which is the same in the `scrapy list` command.
* settings: (dict) settings can be used to populate all settings at runtime, not only the literal/string values, but list/dicts

And other parameters, the more detail documentation is coming soon.

## package a spider
A packaged spider is extremely portable, with one spider package and a FIGURE file, you can easily crawl the whole internet.

When your current dir is in the scope of scrapy project(with any ancient folder which contains a scrapy.cfg file), you can easily run the following commmand to build a spider package.

```
pancli package
```

If you haven't create setup.py for the project, this command will help you create one.

And this command is inspired by [scrapyd-client](https://github.com/scrapy/scrapyd-client)



