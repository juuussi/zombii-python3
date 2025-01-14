# vim: syn=python

from .align import *

FILE = [
  {
    'name': '__announce__',
    'announce': 'CS: Grandma Mimmi, Coham, Dunstan, Samsuurian, Bargh, Cyndre, Akashia, Sarmak, Janina, Security man, Barbledrak, Burly Captain, Bruno, Magistrate, Security Guard',
    'summary': True,
    'skip': 21,
  },
  {
    'path': '2 n;e',
    'target': 'mimmi',
    'alignment': EVIL,
    'announce': 'Grandma Mimmi 3.5m',
    'out': 'w',
    'in': 'e',
    'warnings': "Casts 'harm body', 'harmony hand'",
    'skip': 19,
  },
  {
    'path': 'w;n;3 e;s;w',
    'target': 'coham',
    'alignment': NEUTRAL,
    'announce': 'Coham 3.1m',
    'out': 'e',
    'in': 'w',
    'warnings': "Casts 'hellfire', 'fireball'",
    'flags': 'A',
  },
  {
    'path': 'e;s;w',
    'target': 'dukat',
    'alignment': NEUTRAL,
    'announce': 'Dukat 2.1m',
    'out': 'e',
    'in': 'w',
    'warnings': "Casts 'snowstorm', 'banishment', 'fireball'",
    'flags': 'AB',
  },
  {
    'path': 'e;2 s',
    'target': 'dunstan',
    'alignment': SLIGHTLY_GOOD,
    'announce': 'Dunstan 3.8m',
    'out': 'n',
    'in': 's',
  },
  {
    'path': 'n;w;s',
    'target': 'samsuurian',
    'alignment': ANGELIC,
    'announce': 'Samsuurian 5m',
    'out': 'n',
    'in': 's',
    'flags': 'O',
  },
  {
    'path': 'e',
    'target': 'bargh',
    'alignment': NEUTRAL,
    'announce': 'Bargh 3.9m',
    'out': 'w',
    'in': 'e',
    'warnings': "Casts 'creeping doom', 'terror'",
    'flags': 'B',
  },
  {
    'path': 'w;n;w;n',
    'target': 'cyndre',
    'alignment': VERY_GOOD,
    'announce': 'Cyndre 3.6m',
    'out': 's',
    'in': 'n',
    'warnings': "Casts 'snowstorm', 'prismatic spray'",
    'flags': 'A',
  },
  {
    'path': '2 s',
    'target': 'tinker',
    'alignment': NEUTRAL,
    'announce': 'Tinker 2m',
    'out': 'n',
    'in': 's',
    'warnings': "Casts 'terror', 'harm body'",
    'flags': 'B',
  },
  {
    'path': 'n;e;n',
    'target': 'akashia',
    'alignment': ANGELIC,
    'announce': 'Akashia 6.3m',
    'out': 's',
    'in': 'n',
    'warnings': "Casts 'project force'",
  },
  {
    'path': '2 e',
    'target': 'sarmak',
    'alignment': ANGELIC,
    'announce': 'Sarmak 6.3m',
    'out': 'w',
    'in': 'e',
  },
  {
    'path': '2 w;s;2 w;s;w',
    'target': 'janina',
    'alignment': GOOD,
    'announce': 'Janina 3.5m',
    'out': 'e',
    'in': 'w',
    'warnings': "Casts 'psychic crush', 'harm body', 'harmony hand'",
  },
  {
    'path': 'e;s;w;s',
    'target': 'man',
    'alignment': VERY_GOOD,
    'announce': 'Security man 7.8m',
    'out': 'n',
    'in': 's',
    'warnings': "Casts 'cold ray', 'creeping doom'",
  },
  {
    'path': 'n;4 w;pick tulip',
    'target': 'barbledrak',
    'alignment': VERY_GOOD,
    'announce': 'Barbledrak 4.2m',
    'out': 'n',
    'in': 's',
    'warnings': 'Throws bombs, Stuns randomly',
    'flags': 'AO',
  },
  {
    'path': '2 n;2 e;3 n;e;s;e',
    'target': 'captain',
    'alignment': VERY_GOOD,
    'announce': 'Burly Captain 1.9m',
    'out': 'w',
    'in': 'e',
    'warnings': "Uses 'slash'",
  },
  {
    'path': 'w;2 n',
    'target': 'bruno',
    'alignment': GOOD,
    'announce': 'Bruno 1.6m',
    'out': 'out',
    'in': 'n',
  },
  {
    'path': 'out;2 e;3 n',
    'target': 'magistrate',
    'alignment': VERY_GOOD,
    'announce': 'Magistrate 1.6m',
    'out': 's',
    'in': 'n',
  },
  {
    'path': 's;4 e;9 s',
    'target': 'statue',
    'announce': 'Statue of Tonto (use skills at statue)',
    'out': 'n',
    'in': 's',
  },
  {
    'target': 'guard',
    'alignment': VERY_GOOD,
    'announce': 'Security Guard 1.4m',
    'out': 'n',
    'in': 's',
    'warnings': "Casts 'firebolt', 'icebolt'",
    'flags': 'O',
  },
  {
    'path': '4 n;4 w',
    'name': '__announce__',
    'announce': 'CS',
  },
  {
    'name': 'Unknown',
  },
  ]
