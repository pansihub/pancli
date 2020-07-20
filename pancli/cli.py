import sys
import argparse
from pancli.commands.package import PackageCommand
from pancli.commands.crawl import CrawlCommand
from pancli.commands.plugin import PluginCommand

cmds = {
    'package': PackageCommand(),
    'crawl': CrawlCommand(),
    'plugin': PluginCommand()
}


def _pop_command_name(argv):
    i = 0
    for arg in argv[1:]:
        if not arg.startswith('-'):
            del argv[i]
            return arg
        i += 1


def main(argv = None):
    if argv is None:
        argv = sys.argv
    
    parser = argparse.ArgumentParser('')
    
    command = _pop_command_name(argv)

    if not command:
        print('Please specify command.')
        print('Available commands:')
        for available_command in cmds.keys():
            print('    ' + available_command)
        sys.exit(1)

    try:
        cmd = cmds[command]
    except KeyError:
        print(f"Invalid command {command}")
        sys.exit(1)
    
    cmd.add_arguments(parser)
    parser.usage = f'pansi {command}'
    args = parser.parse_args()
    cmd.run(args)


if __name__ == '__main__':
    main()