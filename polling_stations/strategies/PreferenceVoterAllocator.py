class PreferenceVoterAllocator:
    def __init__(self, voters, preferences, polling_stations):
        self.voters = voters
        self.preferences = preferences
        self.polling_stations = polling_stations
        self.allocation_result = None
        self.station_capacity = None 

    def initialise_station_capacity(self):
        self.station_capacity = {}
        for _, row in self.polling_stations.iterrows():
            self.station_capacity[row['polling_station']] = row['voting_booth']

    def preference_based_allocation(self):
        allocation = {}
        sorted_preferences = self.preferences.sort_values(by=['voter','preference_priority'])

        for _, row in sorted_preferences.iterrows():
            voter = row['voter']
            station = row['polling_station']

            if self.station_capacity[station] > 0:
                if voter in allocation:
                    allocation[voter].append(station)
                else:
                    allocation[voter] = [station]
                self.station_capacity[station] -= 1

        self.allocation_result = allocation

    def print_allocation_result(self):
        if self.allocation_result:
            print(self.allocation_result)
        else:
            print("Run allocation first.")

if __name__ == '__main__':

    import pandas as pd
    import numpy as np

    voters = pd.read_excel('/Users/tundra/Documents/polling_stations/data/voters.xlsx')
    preferences = pd.read_excel('/Users/tundra/Documents/polling_stations/data/preferences.xlsx')
    polling_stations = pd.read_excel('/Users/tundra/Documents/polling_stations/data/polling_stations.xlsx')  

preference_voter_allocator = PreferenceVoterAllocator(voters, preferences, polling_stations)
preference_voter_allocator.initialise_station_capacity()
preference_voter_allocator.preference_based_allocation()

preference_voter_allocator.print_allocation_result()