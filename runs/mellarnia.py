# vim: syn=python

from . import abjurers_grove
import importlib
importlib.reload(abjurers_grove)

from . import isthmas
importlib.reload(isthmas)

from . import mephala
importlib.reload(mephala)

from . import pagoda
importlib.reload(pagoda)

from . import shaolin
importlib.reload(shaolin)


SKIPS = (
  abjurers_grove.FILE[1]['skip'] +
  isthmas.FILE[1]['skip'] +
  pagoda.FILE[1]['skip'] +
  shaolin.FILE[1]['skip'] +
  mephala.FILE[1]['skip'] + 2)

FILE = (
  [
    {
      'name': 'Mellarnia',
      'announce': '1ne',
    },
  ] +
  abjurers_grove.FILE[1:-1] +
  isthmas.FILE[1:-1] +
  pagoda.FILE[1:-1] +
  shaolin.FILE[1:-1] +  # fire
  mephala.FILE[1:-1] +  # fire
  [
    {
      'name': 'Unknown',
    },
  ]
  )
