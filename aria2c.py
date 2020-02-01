import subprocess
import _thread


class MetaSingleton(type):
    _instance = None
    def __call__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class Aria2c(metaclass=MetaSingleton):
    def __init__(self, **cnf):
        self.aria2c_path = cnf.get("aria2c_path")
        self.config_path = cnf.get("config_path")
        self._aria2c = False
        
    def run_aria2c(self):
        cmd = '{} --conf-path="{}"'.format(self.aria2c_path, self.config_path)
        subprocess.run(cmd, shell=True)

    def open_aria2c(self):
        if not self._aria2c:
            _thread.start_new_thread(self.run_aria2c, ())
            self._aria2c = True
        else:
            pass

    def close_aria2c(self):
        subprocess.run("TASKKILL /IM aria2c.exe /F", shell=True)
        self._aria2c = False
