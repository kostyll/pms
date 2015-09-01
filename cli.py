import os

import common


class PMS(object):
    def __init__(self, project_dirrectory):
        self.project_path = project_dirrectory

    @staticmethod
    def init_project():
        if os.path.exists(common.project_dir):
            if os.path.isdir(common.project_dir):
                print "already initialized"
                return
            else:
                raise ValueError("%s is not dirrectory" % common.project_dir)
        else:
            os.mkdir(common.project_dir)


class CLIPMS(PMS):

    def __init__(self, arguments):
        self.arguments = arguments

        command, args = self.parse_args(" ".join(arguments))

        self.run_command(command, args)

    def parse_args(self, arguments):
        command, _, args = arguments.partition(" ")
        args = map(lambda x: x.strip(), args)
        return command, args

    def run_command(self, command, args):
        
        print "running command %s with args %s" % (command, args)

        command_func = getattr(self, 'command_' + command)

        command_func(args)

    def command_init(self, arguments):
        self.init_project()
