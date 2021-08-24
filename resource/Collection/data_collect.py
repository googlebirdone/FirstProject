import subprocess
import re
import psutil


class Read_Cmd:
    def __init__(self, command, filter=None):
        self.cmd = command
        if filter is None:
            self.filter = None
        else:
            self.filter = filter

    def get_cmd_result(self):
        tmp = subprocess.Popen(self.cmd, stdout=subprocess.PIPE)
        if self.filter is None:
            return tmp
        else:
            # 使前一个的输出作为后一个的输入，规避管道符号无法识别问题
            return subprocess.Popen(self.filter, stdin=tmp.stdout, stdout=subprocess.PIPE)

    def get_info(self, pattern):
        result_list = []
        for line in self.get_cmd_result():
            pat = re.compile(pattern)
            # subprocess的输出均为bytes类型，处理时需要转化str,使用decode方式
            result_list.append(pat.findall(line.decode('utf-8'))[-1])
        return result_list

    def get_process_id(self, pattern):
        max_num = []
        if len(self.get_info(pattern)) == 0:
            return "get pid error"
        for num in self.get_info(pattern):
            max_num.append(psutil.Process(int(num)).nice())
        return min(max_num)









