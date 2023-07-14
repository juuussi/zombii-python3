# vim: syn=python

from . import ancient_forest
import importlib
importlib.reload(ancient_forest)

from . import black_mines
importlib.reload(black_mines)

from . import dream
importlib.reload(dream)

from . import fireplane
importlib.reload(fireplane)

from . import grimhildr
importlib.reload(grimhildr)

from . import kriesha
importlib.reload(kriesha)

from . import prison
importlib.reload(prison)

from . import ravenkall_crossing
importlib.reload(ravenkall_crossing)

from . import serpent_lake
importlib.reload(serpent_lake)

from . import stonemen
importlib.reload(stonemen)

from . import wolves
importlib.reload(wolves)


SKIPS = (
  ravenkall_crossing.FILE[0]['skip'] +
  prison.FILE[1]['skip'] +
  serpent_lake.FILE[1]['skip'] +
  ancient_forest.FILE[1]['skip'] +
  stonemen.FILE[1]['skip'] +
  black_mines.FILE[1]['skip'] +
  #fireplane.FILE[1]['skip'] +
  kriesha.FILE[1]['skip'] +
  dream.FILE[1]['skip'] +
  grimhildr.FILE[1]['skip'] +  # cold
  wolves.FILE[1]['skip'] + 1)

FILE = (
  [
    {
      'name': 'Cantador',
      'announce': ravenkall_crossing.FILE[0]['announce'],
      'summary': True,
    },
  ] +
  ravenkall_crossing.FILE[1:-1] +
  [
    {
      'path': '2 e;6 n;2 w;3 n',
      'name': '__announce__',
      'announce': '1n',
    },
  ] +
  prison.FILE[1:-1] +
  serpent_lake.FILE[1:-1] +
  ancient_forest.FILE[1:-1] +
  stonemen.FILE[1:-1] +
  black_mines.FILE[1:-1] +
  #fireplane.FILE[1:-1] +
  kriesha.FILE[1:-1] +
  dream.FILE[1:-1] +
  grimhildr.FILE[1:-1] +
  wolves.FILE[1:-1] +
  [
    {
      'path': '3 s;2 e;6 s;2 w',
      'name': '__announce__',
      'announce': 'Ravenkall Crossing',
    },
    {
      'name': 'Unknown',
    },
  ]
  )
