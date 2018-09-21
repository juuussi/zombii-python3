# vim: syn=python

from align import *

FILE = [
  {
    'announce': '9w',
  },
  {
    'path': '11 n;15 nw;5 ne;n;ne;n;ne;path;where',
    'name': '__announce__',
    'announce': 'Maester: Ghost of Rades, Queen, King, 2x Elite Guardsman, Dirke, Ghost, Blacksmith, Abbot, Weaponsmith, Armourer',
    'summary': True,
    'skip': 15,
  },
  {
    'path': 'nw;ne;4 n;open gates;n;close gates;10 n;open gates;n;close gates;4 n;2 e;2 n;open northeast door;ne;close southwest door;open upstairs door;upstairs;close downstairs door;3 w;open north door;n;close south door;ne;n;open north door;n',
    'target': 'advisor',
    'alignment': VERY_EVIL,
    'announce': 'Ghost of Rades 1.7m',
    'out': 's',
    'in': 'n',
    'skip': 13,
  },
  {
    'path': 'open south door;s;close north door',
    'target': 'queen',
    'alignment': GOOD,
    'announce': 'Ghost Queen 1.2m',
    'out': 's',
    'in': 'n',
    'warnings': "Casts 'banishment', 'golden arrow', 'fireball', 'poison'",
    'flags': 'AB',
  },
  {
    'path': 'w',
    'target': 'king',
    'alignment': GOOD,
    'announce': 'Ghost King 1.3m',
    'out': 'e',
    'in': 'w',
    'warnings': "Casts 'banishment', 'power blast', 'choke'",
    'flags': 'B',
  },
  {
    'target': 'guardsman',
    'alignment': GOOD,
    'announce': '2x Ghost Guardsman 1.1m',
    'out': 'e',
    'in': 'w',
    'warnings': "Casts 'banishment', Uses 'slash' randomly",
    'flags': 'AB',
  },
  {
    'path': 'w',
    'target': 'guardsman',
    'alignment': GOOD,
    'announce': 'Ghost Guardsman 1.1m',
    'out': 'e',
    'in': 'w',
    'warnings': "Casts 'banishment', Uses 'slash' randomly",
    'flags': 'AB',
  },
  {
    'path': '2 e;sw;s;open south door;s;close north door;3 w;2 s;open west door;w;close east door;search corpse;enter passage',
    'commands': 'enter passage',
  },
  {
    'path': 'stairs;open east door;e',
    'target': 'dirke',
    'alignment': EVIL,
    'announce': 'Dirke 1.3m',
    'out': 'w',
    'in': 'e',
    'warnings': "Casts 'poison', Uses 'thrust'",
  },
  {
    'path': 'open west door;w;close east door;stairs;n;open east door;e;close west door;2 n;6 e;open downstairs door;downstairs;close upstairs door;open southwest door;sw;close northeast door;2 s;2 w;4 s;open gates;s;close gates;8 s;3 e;open south door;south',
    'target': 'ghost',
    'alignment': NEUTRAL,
    'announce': 'Ghost 1.1m',
    'out': 'n',
    'in': 's',
    'warnings': "Casts 'golden arrow', 'cause serious wounds'",
  },
  {
    'path': 'take key;drop key;open north door;n;close south door;3 n;8 w;n;e',
    'target': 'ghost',
    'alignment': GOOD,
    'announce': 'Blacksmith 1.2m',
    'out': 'w',
    'in': 'e',
    'warnings': "Casts 'cause serious wounds', 'golden arrow'",
    'flags': 'O',
  },
  {
    'path': 'w;2 n;open west door;w;close east door;n;open north door;n;close south door;n;open east door;e;close west door;e;s',
    'target': 'abbot',
    'alignment': VERY_GOOD,
    'announce': 'Abbot 1.2m',
    'out': 'n',
    'in': 's',
    'warnings': "Casts 'harm body'",
  },
  {
    'path': 'n;w;open west door;w;close east door;s;open south door;s;close north door;s;open east door;e;close west door;3 s;5 e;2 s;w',
    'target': 'ghost',
    'alignment': GOOD,
    'announce': 'Weaponsmith 1.2m',
    'out': 'e',
    'in': 'w',
    'warnings': "Casts 'acid arrow', 'magic missile'",
  },
  {
    'path': 'e;s;4 w;n',
    'target': 'armourer',
    'alignment': GOOD,
    'announce': 'Armourer 1.2m',
    'out': 's',
    'in': 'n',
  },
  {
    'path': 's;4 e;2 s;open gates;s;close gates;4 s;sw;se',
    'announce': 'Maester',
  },
  {
    'path': 'path;sw;s;sw;s;5 sw;15 se;11 s',
    'name': '__announce__',
    'announce': '9w',
  },
  {
    'name': 'Unknown',
  },
  ]
