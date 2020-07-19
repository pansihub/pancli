import sys
from . import CommandBase

class CrawlCommand(CommandBase):
    def add_arguments(self, parser):
        parser.add_argument('spider', nargs='?')
        parser.add_argument('--package')
        parser.add_argument('-s', '--set', nargs='*', dest='setting_set')
        parser.add_argument('-o', '--output')
        parser.add_argument('-f', '--file')
        parser.add_argument('--logfile')

    def run(self, args):
        from ..runner import activate_project, execute
        from ..runner2 import empty_settings, SpiderSetting
        package = args.package
        project_settings = activate_project(package)
        spec = empty_settings
        if args.file:
            spec = SpiderSetting.from_file(args.file)
        spider_name = args.spider or spec.spider_name
        if not spider_name:
            print('No spider name specified.')
            sys.exit(1)
        argv = argv=['scrapy', 'crawl', spider_name]
        for setting_arg in args.setting_set or []:
            setting_k, setting_v = setting_arg.split('=', 1)
            argv += ['-s', '%s=%s' % (setting_k, setting_v)]
        if args.output:
            argv += ['-o', args.output]
        if args.logfile:
            argv += ['--logfile', args.logfile]
        execute(argv, settings=project_settings)
