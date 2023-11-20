class AvailabilityVoterAllocator:
    def __init__(self, voters, preferences, polling_stations):
        self.voters = voters
        self.preferences = preferences
        self.polling_stations = polling_stations
        self.allocation_result = {}

    def allocate_voters(self):
        # Sort polling stations by voting booth availability (most roomy first)
        sorted_stations = self.polling_stations.sort_values(by='voting_booth', ascending=False)

        # Iterate through preferences and allocate voters
        for _, pref_row in self.preferences.iterrows():
            voter = pref_row['voter']
            station = pref_row['polling_station']

            # Check if the station has available voting booths
            if sorted_stations.loc[sorted_stations['polling_station'] == station, 'voting_booth'].iloc[0] > 0:
                # Deduct discount from station cost
                discount = self.voters.loc[self.voters['voter'] == voter, 'discount'].iloc[0]
                station_cost = self.polling_stations.loc[self.polling_stations['polling_station'] == station, 'station_cost'].iloc[0]
                discounted_cost = station_cost * (1 - discount)

                # Update allocation result
                if voter in self.allocation_result:
                    self.allocation_result[voter].append({'polling_station': station, 'discounted_cost': discounted_cost})
                else:
                    self.allocation_result[voter] = [{'polling_station': station, 'discounted_cost': discounted_cost}]

                # Update voting booth availability
                sorted_stations.loc[sorted_stations['polling_station'] == station, 'voting_booth'] -= 1

        return self.allocation_result
    
if __name__ == '__main__':

    import pandas as pd
    import numpy as np

    voters = pd.read_excel('/Users/tundra/Documents/polling_stations/data/voters.xlsx')
    preferences = pd.read_excel('/Users/tundra/Documents/polling_stations/data/preferences.xlsx')
    polling_stations = pd.read_excel('/Users/tundra/Documents/polling_stations/data/polling_stations.xlsx')   


# Create an instance of the VoterAllocator class
allocator = AvailabilityVoterAllocator(voters, preferences, polling_stations)

# Allocate voters
availability_allocation_result = allocator.allocate_voters()

# Print the allocation result
print("Allocation Result:")
print(availability_allocation_result)