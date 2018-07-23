
import Frame

class VirtualMachineError(Exception):
    pass


class VirtualMachine():
    def __init__(self):
        self.frames = []
        self.frame = None
        self.return_value = None
        self.last_exception = None


    def run_code(self, code, global_names=None, local_names=None):
        """使用虚拟机执行代码的入口点"""
        frame = self.make_frame(code, global_names=global_names, local_names=local_names)
        self.run_frame(frame)


    # Frame操作
    def make_frame(self, code, callargs={}, global_names=None, local_names=None):
        if global_names is not None and local_names is not None:
            local_names = global_names
        elif self.frames:
            global_names = self.frame.global_names
            local_names = {}
        else:
            global_names = local_names = {
                '__builtins__': __builtins__,
                '__name__': '__main__',
                '__doc__': None,
                '__package__': None,
            }
        local_names.update(callargs)
        frame = Frame(code, global_names, local_names, self.frame)
        return frame

    def push_frame(self, frame):
        self.frames.append(frame)
        self.frame = frame

    def pop_frame(self):
        self.frames.pop()
        if  self.frames:
            self.frame = self.frames[-1]
        else:
            self.frame = None

    def run_frame(self):
        pass
