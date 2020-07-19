from . import CommandBase

class CrawlCommand(CommandBase):
    def add_arguments(self, parser):
        parser.add_argument('spider', nargs='?')
        parser.add_argument('--package')

    def run(self, args):
        from ..runner import activate_project, execute
        package = args.package
        settings = activate_project(package)
        spider_name = args.spider
        if not spider_name:
            print('no spider name spicified')
        execute(argv=['scrapy', 'crawl', spider_name], settings=settings)
