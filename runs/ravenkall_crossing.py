# vim: syn=python

from align import *

FILE = [
  {
    'name': '__announce__',
    'announce': 'Ravenkall Crossing: Radan, Joyce, Hu, Cho, Letitia, Margaret, Larvel, Bargough, Rufus, Gleeman, Inara, Ralph, Brandelwyn, Baroness, Baron',
    'summary': True,
    'skip': 19,
  },
  {
    'path': '6 e;6 n;w;open south door;s;e',
    'target': 'radan',
    'alignment': GOOD,
    'announce': 'Radan Nalashia (heals merchants) 1.7m',
    'out': 'w',
    'in': 'e',
    'skip': 17,
  },
  {
    'path': 'w;open north door;n;close south door;e;2 s;open west door;w',
    'target': 'joyce',
    'alignment': SLIGHTLY_GOOD,
    'announce': 'Joyce Ratclif 2.1m',
    'out': 'e',
    'in': 'w',
  },
  {
    'path': 'open east door;e;close west door;3 s;open west door;w',
    'target': 'hu',
    'alignment': VERY_GOOD,
    'announce': 'Hu 1.2m',
    'out': 'e',
    'in': 'w',
  },
  {
    'target': 'cho',
    'alignment': VERY_GOOD,
    'announce': 'Cho (protects her man) 1.5m',
    'out': 'e',
    'in': 'w',
  },
  {
    'path': 'open east door;e;close west door;n;2 w;2 n;2 w;n;e;n',
    'target': 'clerk',
    'alignment': SLIGHTLY_GOOD,
    'announce': 'Letitia Brocas 2.5m',
    'out': 'n',
    'in': 's',
  },
  {
    'path': 'open north door;n;close south door;5 w;5 s;w',
    'target': 'margaret',
    'alignment': GOOD,
    'announce': 'Margaret Ratclif 2.8m',
    'out': 'e',
    'in': 'w',
    'warnings': "Casts 'power blast', 'fireball', 'golden arrow', 'magic missile', 'acid arrow'",
    'flags': 'A',
  },
  {
    'path': 'e;2 n;4 w;n;open east door;e',
    'target': 'larvel',
    'alignment': GOOD,
    'announce': 'Larvel Harding 4m',
    'out': 'w',
    'in': 'e',
  },
  {
    'path': 'open west door;w;close east door;2 s;e',
    'target': 'bargough',
    'alignment': UNKNOWN,
    'announce': 'Bargough 3.5m',
    'out': 'w',
    'in': 'e',
  },
  {
    'path': 'w;2 s;2 e;n',
    'target': 'rufus',
    'alignment': GOOD,
    'announce': 'Rufus Mugwort 1.1m',
    'out': 's',
    'in': 'n',
  },
  {
    'path': 'w',
    'target': 'gleeman',
    'alignment': SLIGHTLY_GOOD,
    'announce': 'Gleeman 4m',
    'out': 'e',
    'in': 'w',
  },
  {
    'path': 'e;s;2 w;3 s;e;n;w',
    'target': 'sarth',
    'alignment': NEUTRAL,
    'announce': 'Sarth 3.1m',
    'out': 'e',
    'in': 'w',
  },
  {
    'path': 'e;s;w;2 s;2 e;3 ne;w;n;where Inara Maele',
    'target': 'inara',
    'alignment': VERY_GOOD,
    'announce': 'Inara Maele (wanders) 1.2m',
    'out': 's',
    'in': 'n',
    'warnings': "Casts 'skyfire', 'summon storm'",
    'flags': 'OA',
  },
  {
    'path': 's;e;3 sw;2 e;n;where ralph',
    'target': 'ralph',
    'alignment': SLIGHTLY_GOOD,
    'announce': 'Ralph (wanders) 2.5m',
    'flags': 'O',
  },
  {
    'path': 's;8 e',
    'target': 'brandelwyn',
    'alignment': VERY_GOOD,
    'announce': 'Brandelwyn 1.1m',
    'out': 'n',
    'in': 's',
    'warnings': "Casts 'acid arrow'",
    'flags': 'O',
  },
  {
    'path': '3 n;manor;open west door',
    'target': 'baroness',
    'alignment': SLIGHTLY_EVIL,
    'announce': 'Baroness (random) 7.7m',
  },
  {
    'target': 'baron',
    'alignment': UNKNOWN,
    'announce': 'Baron (random) 5m',
  },
  {
    'path': 'close west door;e;2 n;6 w',
    'name': '__announce__',
    'announce': 'Ravenkall Crossing',
  },
  {
    'name': 'Unknown',
  },
  ]
