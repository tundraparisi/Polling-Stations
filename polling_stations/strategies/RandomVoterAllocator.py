class RandomVoterAllocator:
    def __init__(self, voters, polling_stations):
        self.voters = voters
        self.polling_stations = polling_stations
    
    def random_allocation(self):
        # Converti la colonna 'polling_station' in un array NumPy
        polling_stations_array = self.polling_stations['polling_station'].values
        
        # Converti la colonna 'voter' in un array NumPy
        voters_array = self.voters['voter'].values
        np.random.shuffle(voters_array)
   
        allocation = {}

        for voter in voters_array:
            station = np.random.choice(polling_stations_array)
            if station in allocation:
                allocation[station].append(voter)
            else:
                allocation[station] = [voter]
        return allocation

if __name__ == '__main__':

    import pandas as pd
    import numpy as np

    voters = pd.read_excel('/Users/tundra/Documents/polling_stations/data/voters.xlsx')
    preferences = pd.read_excel('/Users/tundra/Documents/polling_stations/data/preferences.xlsx')
    polling_stations = pd.read_excel('/Users/tundra/Documents/polling_stations/data/polling_stations.xlsx')         

    TheRandomAllocator = RandomVoterAllocator(voters, polling_stations)
    random_allocation_result = TheRandomAllocator.random_allocation()
    print(random_allocation_result)