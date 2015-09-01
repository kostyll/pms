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

    @staticmethod
    def find_project():
        cwd = os.getcwd()
        print "CWD = %s" % cwd
        cwd_dir_parent = cwd
        while True:
            cwd_dir = os.path.join(cwd_dir_parent, common.project_dir)
            if os.path.exists(cwd_dir) and os.path.isdir(cwd_dir):
                return os.path.dirname(cwd_dir)
            else:
                result = os.path.dirname(cwd_dir_parent)
                if cwd_dir_parent == result:
                    return None
                else:
                    cwd_dir_parent = result
                # print "gussing %s" % cwd_dir_parent

    @staticmethod
    def get_tasks(parentdir):
        tasks = []
        try:
            for line in open(os.path.join(parentdir, 'dev_tasks.txt'), 'rt'):
                tasks.append(self.parse_task_line(line))
            return tasks
        except:
            return tasks

    @staticmethod
    def parse_task_line(taskline):
        return taskline



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

    def command_get(self, arguments):
        print self.find_project()

    def command_tasks(self, arguments):
        parent_dir = self.find_project()
        if parent_dir:
            tasks = self.get_tasks(parent_dir)
            for task in tasks:
                print "Task %s" % task
            

