from . import CommandBase

class CrawlCommand(CommandBase):
    def add_arguments(self, parser):
        parser.add_argument('spider', nargs='?')

    def run(self, args):
        from ..runner import activate_project, execute
        settings = activate_project()
        spider_name = args.spider
        if not spider_name:
            print('no spider name spicified')
        execute(argv=['scrapy', 'crawl', spider_name], settings=settings)
