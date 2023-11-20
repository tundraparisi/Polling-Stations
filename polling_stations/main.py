
import pandas as pd 
from allocation_strategies import *

from strategies.RandomVoterAllocator import RandomVoterAllocator
from strategies.PreferenceVoterAllocator import PreferenceVoterAllocator
from strategies.PriceVoterAllocator import PriceVoterAllocator
from strategies.AvailabilityVoterAllocator import AvailabilityVoterAllocator

voters = pd.read_excel('/Users/tundra/Documents/polling_stations/data/voters.xlsx')
preferences = pd.read_excel('/Users/tundra/Documents/polling_stations/data/preferences.xlsx')
polling_stations = pd.read_excel('/Users/tundra/Documents/polling_stations/data/polling_stations.xlsx')

TheRandomAllocator = RandomVoterAllocator(voters, polling_stations)