from . import CommandBase
from ..plugin import list_, _pip_install

class PluginCommand(CommandBase):
    def add_arguments(self, parser):
        subparsers = parser.add_subparsers(dest='subcommand')

        parser_list = subparsers.add_parser('list')                        

        parser_install = subparsers.add_parser('install')
        parser_install.add_argument('url_or_path')


    def run(self, args):
        if args.subcommand == 'list':
            return list_()
        if args.subcommand == 'install':
            return _pip_install(args.url_or_path)