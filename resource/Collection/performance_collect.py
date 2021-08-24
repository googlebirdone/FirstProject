from resource.Collection.data_collect import Read_Cmd
import psutil


class Performance_time:
    def __init__(self, name):
        self.name = name

    def get_time(self):
        js = ''


class Performance_memory(Read_Cmd):
    def __init__(self, pattern):
        self.pattern = pattern

    def get_memory(self):
        try:
            p = psutil.Process(self.get_process_id(self.pattern))
        except Exception as e:
            return str(e)
        return p.memory_info.vms/(1024**2)





