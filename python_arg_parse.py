#!/usr/bin/env python
# this script is sample code which shows Sub-command behavior more easier than
# argparse in the python default library. uroboros is like wrapper library that
# is inspired by spf13/cobra
from uroboros import Option, Command
from uroboros.constants import ExitStatus


class RootCommand(Command):

    name = 'APPLICATION_NAME'
    long_description = 'write long description here'

    def build_option(self, parser):
        parser.add_argument('--version', action='store_true', default=False, help='Print version')
        return parser

    def run(self, args):
        if args.version:
            print("{name} v{version}".format(name=self.name, version='0.1.0'))
        else:
            print(self.long_description)
            self.print_help()
        return ExitStatus.SUCCESS


class CommonOption(Option):

    def build_option(self, parser):
        parser.add_argument('--format', type=str, default="json", help="specify output format. default: json")
        parser.add_argument('--config', type=str, default="", help="specify config file path.")
        return parser


class SubCmdGet(Command):

    name = 'get'

    short_description = 'whrite short description here'
    long_description = 'whrite long description here'
    options = [CommonOption()]

    def build_option(self, parser):
        pass

    def run(self, args):
        self.print_help()


# common option:
# --config : config path
# --format : output fromat

# sub-command structure
# root
# ├─ get
# │   └── data
# └─ show
#     └── data

# root
root_cmd = RootCommand()

# 1st tier subcommands
sub_cmd_crawl = SubCmdCrawl()
sub_cmd_get = SubCmdGet()
sub_cmd_describe = SubCmdDescribe()

# 2nd tier subcommands
sub_cmd_get_vtms     = SubCmdGetVtms()
sub_cmd_get_vss      = SubCmdGetVirtualServers()
sub_cmd_get_pools    = SubCmdGetPools()
sub_cmd_get_monitors = SubCmdGetMonitors()

# add 2nd to 1st tier
sub_cmd_get.add_command(sub_cmd_get_vtms)
sub_cmd_get.add_command(sub_cmd_get_vss)
sub_cmd_get.add_command(sub_cmd_get_pools)
sub_cmd_get.add_command(sub_cmd_get_monitors)

# add 1st tier to root
root_cmd.add_command(
    sub_cmd_crawl,
    sub_cmd_get,
)


if __name__ == '__main__':
    exit(root_cmd.execute())
