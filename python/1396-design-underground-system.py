class UndergroundSystem:
    '''
    person_dict:
        key=id
        value=(
            check_in_station,
            check_in_time
        )

    station_dict:
        key=starting_station_name
        value=ending_station_dict

        ending_station_dict:
            key=ending_station_name
            value=average_time_between_starting_station_and_ending_station


    __init__:
        - initialize person_dict
        - initialize station_dict

        Time: O(1)

    checkIn:
        - fill in person_dict values
        Time: O(1)

    checkOut:
        - GET the starting_station and check_in_time from the person_dict using their id
        - SET person_dict, key=id, their values to default, which is None
        (this resets the person values so that they can use the transit again)

        calculate the new average
            - time it takes to get from starting station to ending station = ending_station_time - starting_station_time
            - get the currently recorded average time from starting_station to ending_station
            - take the average of these averages (add both, then divide by 2)
            - record this number as the new number

            - if there is no currently recorded average time, then just make the first number the new average time

        Time: O(1)

    getAverageTime:
        - lookup in dictionary starting staion to ending station
        Time: O(1)

    p is the number of people
    s is the number of stations
    Space: O(p + s*s)
        ;(s*s) each staion maps to every other station

    '''

    def __init__(self):
        self.person = {}
        self.stations = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.person:
            self.person[id] = {}

        self.person[id]['starting_station'] = stationName
        self.person[id]['starting_time'] = t
        # print(id, self.person[id])

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # this problem assumes that checkIn is called before checkOut, which is why we don't have to check if the person exist or if there is a time
        starting_station, starting_time = self.person[id][
            'starting_station'], self.person[id]['starting_time']
        # reset the values for the person checkIn
        # b/c checkIn is called before checkOut, technically we don't have to set the values back to None since they'll get overrided anyways
        self.person[id]['starting_station'], self.person[id]['starting_time'] = None, None

        station_to_station_time = t - starting_time

        if starting_station not in self.stations:
            self.stations[starting_station] = {}

        if stationName not in self.stations[starting_station]:
            self.stations[starting_station][stationName] = [
                station_to_station_time, 1]
        else:
            self.stations[starting_station][stationName][0] += station_to_station_time
            self.stations[starting_station][stationName][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.stations[startStation][endStation][0] / self.stations[startStation][endStation][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
