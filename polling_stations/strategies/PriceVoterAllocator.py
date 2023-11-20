class PriceVoterAllocator:
    def __init__(self, voters, polling_stations):
        self.voters = voters
        self.polling_stations = polling_stations
        self.allocation = {}  # Dictionary to store the assignment of voters to polling stations
        self.station_capacity = {}  # Dictionary to track the remaining capacity of each polling station

    def price_based_allocation(self):
        # Initialize the capacity of polling stations
        for _, row in self.polling_stations.iterrows():
            self.station_capacity[row['polling_station']] = row['voting_booth']

        # Sort polling stations by price (from cheapest to most expensive)
        sorted_stations = self.polling_stations.sort_values(by='station_cost')

        # Iterate through voters and assign them to polling stations based on price and capacity
        for _, row in self.voters.iterrows():
            voter = row['voter']
            discount = row['discount']

            # Calculate the maximum price the voter is willing to pay
            max_price = 1 - discount

            # Find the first available polling station with a price less than or equal to the maximum price
            for _, station_row in sorted_stations.iterrows():
                station = station_row['polling_station']
                station_cost = station_row['station_cost']

                if station_cost <= max_price and self.station_capacity[station] > 0:
                    # Assign the voter to the polling station
                    if voter in self.allocation:
                        self.allocation[voter].append(station)
                    else:
                        self.allocation[voter] = [station]
                    # Update the capacity of the polling station
                    self.station_capacity[station] -= 1
                    break

        return self.allocation
    
if __name__ == '__main__':

    import pandas as pd
    import numpy as np

    voters = pd.read_excel('/Users/tundra/Documents/polling_stations/data/voters.xlsx')
    preferences = pd.read_excel('/Users/tundra/Documents/polling_stations/data/preferences.xlsx')
    polling_stations = pd.read_excel('/Users/tundra/Documents/polling_stations/data/polling_stations.xlsx')   


hotel_allocator = PriceVoterAllocator(voters, polling_stations)
price_allocation_result = hotel_allocator.price_based_allocation()
print(price_allocation_result)
