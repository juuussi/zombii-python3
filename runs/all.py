# vim: syn=python

from . import angarock
import importlib
importlib.reload(angarock)

from . import azynya
importlib.reload(azynya)

from . import bard_guild
importlib.reload(bard_guild)

from . import brownie_fields
importlib.reload(brownie_fields)

from . import cantador
importlib.reload(cantador)

from . import castle_greenlight
importlib.reload(castle_greenlight)

from . import circus
importlib.reload(circus)

from . import cleric_guild
importlib.reload(cleric_guild)

from . import concordia
importlib.reload(concordia)

from . import damorra_swamps
importlib.reload(damorra_swamps)

from . import darkwater
importlib.reload(darkwater)

from . import deep_forest_ranger_outpost
importlib.reload(deep_forest_ranger_outpost)

from . import dragons
importlib.reload(dragons)

from . import dryads
importlib.reload(dryads)

from . import dusk
importlib.reload(dusk)

from . import harbour
importlib.reload(harbour)

from . import hemlock
importlib.reload(hemlock)

from . import hillside
importlib.reload(hillside)

from . import keep
importlib.reload(keep)

from . import maester
importlib.reload(maester)

from . import mage_guild
importlib.reload(mage_guild)

from . import malbeth
importlib.reload(malbeth)

from . import manor
importlib.reload(manor)

from . import medo
importlib.reload(medo)

from . import mellarnia
importlib.reload(mellarnia)

from . import minas_tirith
importlib.reload(minas_tirith)

from . import neckbreaker_desert
importlib.reload(neckbreaker_desert)

from . import newbie_fields
importlib.reload(newbie_fields)

from . import obizuth
importlib.reload(obizuth)

from . import ranger_forest
importlib.reload(ranger_forest)

from . import ravenloft
importlib.reload(ravenloft)

from . import revelstone
importlib.reload(revelstone)

from . import saurus
importlib.reload(saurus)

from . import temple_of_burning_night
importlib.reload(temple_of_burning_night)

from . import terray
importlib.reload(terray)

from . import towanda
importlib.reload(towanda)

from . import turre
importlib.reload(turre)

from . import tyrir
importlib.reload(tyrir)

from . import uhruul
importlib.reload(uhruul)

from . import valley_of_mystery
importlib.reload(valley_of_mystery)

from . import varalors
importlib.reload(varalors)

from . import yellow_tower
importlib.reload(yellow_tower)

from . import zombie_city
importlib.reload(zombie_city)


CITY_SKIPS = (
  zombie_city.FILE[0]['skip'] +
  cleric_guild.FILE[1]['skip'] +
  bard_guild.FILE[1]['skip'] +
  mage_guild.FILE[1]['skip'] + 1)

FILE = (
  [
    {
      'announce': '9w',
    },
    {
      'path': '9 e',
      'name': '__announce__',
      #'announce': 'ZombieCity',
      'announce': zombie_city.FILE[0]['announce'],
      'summary': True,
      'skip': (
        CITY_SKIPS +
        cantador.SKIPS +
        mellarnia.SKIPS - 1),
    },
  ] +
  zombie_city.FILE[1:-1] +
  cleric_guild.FILE[1:-1] +
  bard_guild.FILE[1:-1] +
  mage_guild.FILE[1:-1] +
  [
    {
      'path': '3 e;4 n;w;buy transport to ravenkall;where',
      'name': cantador.FILE[0]['name'],
      'announce': cantador.FILE[0]['announce'],
      'summary': True,
      'commands': 'buy transport to ravenkall',
      'items': 'all gold',
      'skip': cantador.SKIPS,
    },
  ] +
  cantador.FILE[1:-2] +
  [
    {
      'path': '6 n;ne;n;ne;n;2 ne;n;ne;n;ne;n;ne;enter;2 n;ne;2 nw;w;3 sw;4 w;sw;w;2 sw;w;nw;3 n;7 ne;2 n;climb;cs',
      'name': '__announce__',
      'announce': 'CS',
    },
    {
      'path': '3 e;4 n;w;buy transport to erend;where',
      'name': mellarnia.FILE[0]['name'],
      'announce': '1ne',
      'commands': 'buy transport to erend',
      'items': 'all gold',
      'skip': mellarnia.SKIPS,
    },
  ] +
  mellarnia.FILE[1:-1] +
  [
    {
      'path': 'sw;enter;buy transport to zombiecity',
      'name': '__announce__',
      'announce': 'CS',
      'commands': 'buy transport to zombiecity',
      'items': 'all gold',
    },
    {
      'path': '9 w',
      'name': '__announce__',
      'announce': '9w',
    },
  ] +
  revelstone.FILE[1:-1] + # cold
  uhruul.FILE[1:-1] +
  terray.FILE[1:-1] + # pois
  tyrir.FILE[1:-1] +
  dragons.FILE[1:-1] +
  towanda.FILE[1:-1] +
  yellow_tower.FILE[1:-1] +
  valley_of_mystery.FILE[1:-1] +
  turre.FILE[1:-1] + # psio
  varalors.FILE[1:-1] + # psio
  ranger_forest.FILE[1:-1] + # magi
  keep.FILE[1:-1] + # magi
  castle_greenlight.FILE[1:-1] + # magi
  obizuth.FILE[1:-1] + # fire
  neckbreaker_desert.FILE[1:-1] + # fire, banish
  malbeth.FILE[1:-1] + # banish
  azynya.FILE[1:-1] + # acid
  deep_forest_ranger_outpost.FILE[1:-1] +
  concordia.FILE[1:-1] +
  medo.FILE[1:-1] +
  ravenloft.FILE[1:-1] +
  angarock.FILE[1:-1] + # cold
  saurus.FILE[1:-1] + # psio
  dusk.FILE[1:-1] + # cold
  harbour.FILE[1:-1] +
  minas_tirith.FILE[1:-1] + # fire
  circus.FILE[1:-1] +
  dryads.FILE[1:-1] +
  brownie_fields.FILE[1:-1] +
  newbie_fields.FILE[1:-1] +
  hemlock.FILE[1:-1] +
  maester.FILE[1:-1] + # magi
  temple_of_burning_night.FILE[1:-1] +
  hillside.FILE[1:-1] + # fire
  darkwater.FILE[1:-1] +
  manor.FILE[1:-1] + # psio
  damorra_swamps.FILE[1:-1] +
  [
    {
      'name': 'Unknown',
    },
  ]
  )
