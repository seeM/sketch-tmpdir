# AUTOGENERATED! DO NOT EDIT! File to edit: ../00_core.ipynb.

# %% auto 0
__all__ = ['tmpdir', 'TmpDir']

# %% ../00_core.ipynb 2
import os,shutil,subprocess,tempfile
from contextlib import contextmanager
from pathlib import Path

# %% ../00_core.ipynb 4
class TmpDir:
    "Create temporary workspaces."
    def __init__(self): self.cwd,self._dir,self.path = None,None,None

    def new(self, subdir=''):
        "Create and `cd` to `subdir` under a temp dir."
        if self.cwd is None: self.cwd = Path.cwd()
        self.dir = Path(tempfile.mkdtemp())
        self.path = self.dir/subdir
        self.path.mkdir(exist_ok=True, parents=True)
        os.chdir(self.path)

    @property
    def dir(self): return self._dir
    @dir.setter
    def dir(self, o):
        "`rm` current `dir` and set a new one."
        if self._dir: shutil.rmtree(self._dir)
        self._dir = o

    def close(self):
        "`rm` current `dir` and `cd` to original `cwd`."
        self.dir = None
        os.chdir(self.cwd)

    @contextmanager
    def __call__(self, subdir=''):
        "Work in a temp dir then `cd` back to original `cwd`."
        try:
            self.new(subdir)
            yield self.path
        finally: self.close()

# %% ../00_core.ipynb 6
tmpdir = TmpDir()
