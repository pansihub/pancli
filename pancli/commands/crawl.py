from . import CommandBase

class CrawlCommand(CommandBase):
    def add_arguments(self, parser):
        parser.add_argument('spider', nargs='?')
        parser.add_argument('--package')
        parser.add_argument('-s', '--set', nargs='*', dest='setting_set')
        parser.add_argument('-o', '--output')

    def run(self, args):
        from ..runner import activate_project, execute
        package = args.package
        settings = activate_project(package)
        spider_name = args.spider
        if not spider_name:
            print('no spider name spicified')
        argv = argv=['scrapy', 'crawl', spider_name]
        for setting_arg in args.setting_set or []:
            setting_k, setting_v = setting_arg.split('=', 1)
            argv += ['-s', '%s=%s' % (setting_k, setting_v)]
        if args.output:
            argv += ['-o', args.output]
        execute(argv, settings=settings)
