# Voter Allocation Strategies

## Introduction
This project implements four different strategies for allocating voters to polling stations. Each strategy considers various factors such as availability, preference, and discounts.

## Strategies

### 1. **Random Allocation**
   - Description: Voters are randomly distributed to polling stations until seats or voters are exhausted.
   - Usage: `RandomAllocation(voters, polling_stations).allocate_rooms()`

### 2. **Price-Based Allocation**
   - Description: Voters are assigned to the least expensive polling station, considering their preference and discount.
   - Usage: `PriceBasedAllocation(voters, preferences, polling_stations).allocate_rooms()`

### 3. **Availability and Preference Allocation**
   - Description: Allocation based on availability; places are distributed in order of voting booth availability, starting with the most roomy polling station and subordinately in order of preference until places or voters are exhausted.
   - Usage: `AvailabilityPreferenceAllocation(voters, preferences, polling_stations).allocate_rooms()`

### 4. **Discounted Cost Allocation**
   - Description: Allocation based on the discounted cost of polling stations for each voter, considering their preference.
   - Usage: `DiscountedCostAllocation(voters, preferences, polling_stations).allocate_rooms()`

## Usage
1. Clone the repository.
2. Import the necessary classes into your Python script or notebook.
3. Create instances of your voters, preferences, and polling stations datasets.
4. Instantiate the desired allocation strategy class.
5. Call the `allocate_rooms()` method to get the allocation result.



