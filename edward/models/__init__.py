"""
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from edward.models.random_variable import RandomVariable
from edward.models.random_variables import *

from tensorflow.python.util.all_util import remove_undocumented
from edward.models import random_variables as _module

_allowed_symbols = [
    'RandomVariable',
]
for name in dir(_module):
  obj = getattr(_module, name)
  if (isinstance(obj, type) and
          issubclass(obj, RandomVariable) and
          obj != RandomVariable):
    _allowed_symbols.append(name)

remove_undocumented(__name__, allowed_exception_list=_allowed_symbols)
