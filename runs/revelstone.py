# vim: syn=python

from align import *

FILE = [
  {
    'announce': '9w',
  },
  {
    'path': '6 w;sw;w;sw;w;2 sw;w;sw;w;sw;w;sw;climb;where',
    'name': '__announce__',
    'announce': 'The Land',
    'skip': 17,
  },
  {
    'path': 'd;w;sw;2 s;se;2 ne;plains;whistle;ride horse to revelstone;where',
    'name': '__announce__',
    'announce': 'Revelstone: 2x Bladeguard, 4x Bloodguard, Prothall, Variol, Birinair, Morham',
    'summary': True,
    'commands': 'whistle;ride horse to revelstone',
    'skip': 15,
  },
  {
    'path': '6 n;w',
    'target': 'bladeguard',
    'alignment': VERY_GOOD,
    'announce': 'Bladeguard 4m',
    'out': 'e',
    'in': 'w',
    'warnings': "Casts 'poison'",
    'flags': 'O',
  },
  {
    'path': '2 e',
    'target': 'bloodguard',
    'alignment': VERY_GOOD,
    'announce': 'Bloodguard 3m',
    'out': 'w',
    'in': 'e',
    'flags': 'O',
  },
  {
    'path': 'w;n',
    'target': 'prothall',
    'alignment': ANGELIC,
    'announce': 'Prothall 8.8m',
    'out': 's',
    'in': 'n',
    'warnings': "Casts 'earthquake'",
  },
  {
    'path': '3 s;e;u;2 n',
    'target': 'bloodguard',
    'alignment': VERY_GOOD,
    'announce': 'Bloodguard (duplicate) 3.5m',
    'out': 's',
    'in': 'n',
  },
  {
    'path': 'n;nw;sw;s',
    'target': 'bladeguard',
    'alignment': VERY_GOOD,
    'announce': 'Bladeguard (duplicate) 4m',
    'out': 'n',
    'in': 's',
    'warnings': "Casts 'poison'",
  },
  {
    'path': '2 s;d;e;s;3 w;2 n;w',
    'target': 'bloodguard',
    'alignment': VERY_GOOD,
    'announce': 'Bloodguard 3.5m',
    'out': 'e',
    'in': 'w',
  },
  {
    'target': 'lord',
    'alignment': ANGELIC,
    'announce': 'Variol 4.6m',
    'out': 'e',
    'in': 'w',
    'warnings': "Casts 'harm', 'harm body'",
  },
  {
    'path': 'e;2 n;w',
    'target': 'birinair',
    'alignment': SLIGHTLY_GOOD,
    'announce': 'Birinair 4.1m',
    'out': 'e',
    'in': 'w',
    'warnings': 'Throws chairs, Smashes oil lamp!',
  },
  {
    'path': 'e;n;e',
    'target': 'bloodguard',
    'alignment': VERY_GOOD,
    'announce': 'Bloodguard 3.4m',
    'out': 'w',
    'in': 'e',
  },
  {
    'path': 'n',
    'target': 'lord',
    'alignment': ANGELIC,
    'announce': 'Morham 3.5m',
    'out': 's',
    'in': 'n',
  },
  {
    'path': 's;4 e;n',
    'target': 'bloodguard',
    'alignment': VERY_GOOD,
    'announce': 'Bloodguard (invisible) 3.5m',
    'out': 's',
    'in': 'n',
  },
  {
    'target': 'lady',
    'alignment': ANGELIC,
    'announce': 'Tamarantha 3.5m',
    'out': 's',
    'in': 'n',
    'warnings': "Casts 'psychic crush' randomly",
  },
  {
    'path': 's;e;5 s;3 w;3 s;whistle;ride horse to plains',
    'announce': 'Plains',
    'commands': 'whistle;ride horse to plains',
  },
  {
    'path': 'watch',
    'announce': 'The Land',
  },
  {
    'path': 'climb;ne;e;ne;e;ne;e;2 ne;e;ne;e;ne;6 e',
    'name': '__announce__',
    'announce': '9w',
  },
  {
    'name': 'Unknown',
  },
  ]
