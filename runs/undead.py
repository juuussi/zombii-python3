# vim: ft=python

from . import brownie_tree
import importlib
importlib.reload(brownie_tree)

from . import cantador_undead
importlib.reload(cantador_undead)

from . import castle_greenlight
importlib.reload(castle_greenlight)

from . import keep_undead
importlib.reload(keep_undead)

from . import maester_undead
importlib.reload(maester_undead)

from . import mage_guild_undead
importlib.reload(mage_guild_undead)

from . import pyramid
importlib.reload(pyramid)

from . import ravenkall_sewers
importlib.reload(ravenkall_sewers)

from . import uhruul_undead
importlib.reload(uhruul_undead)


CITY_SKIPS = (
  mage_guild_undead.FILE[1]['skip'])

FILE = (
  [
    {
      'announce': '9w',
    },
  ] +
  brownie_tree.FILE[1:-1] +
  castle_greenlight.FILE[1:-1] +
  uhruul_undead.FILE[1:-1] +
  maester_undead.FILE[1:-1] +
  [
    {
      'path': '9 e',
      'name': '__announce__',
      'announce': 'CS',
      'skip': (
        CITY_SKIPS +
        cantador_undead.SKIPS + 2),  # 9e+9w
    },
  ] +
  mage_guild_undead.FILE[1:-1] +
  [
    {
      'path': '3 e;4 n;w;buy transport to ravenkall;where',
      'name': cantador_undead.FILE[0]['name'],
      'announce': cantador_undead.FILE[0]['announce'],
      'commands': 'buy transport to ravenkall',
      'items': 'all gold',
      'skip': cantador_undead.SKIPS,
    },
  ] +
  cantador_undead.FILE[1:-1] +
  [
    {
      'path': '6 n;ne;n;ne;n;2 ne;n;ne;n;ne;n;ne;enter;2 n;ne;2 nw;w;3 sw;4 w;sw;w;2 sw;w;nw;3 n;7 ne;2 n;climb;cs',
      'name': '__announce__',
      'announce': 'CS',
    },
    {
      'path': '9 w',
      'name': '__announce__',
      'announce': '9w',
    },
  ] +
  keep_undead.FILE[1:-1] +
  [
    {
      'name': 'Unknown',
    },
  ]
  )
