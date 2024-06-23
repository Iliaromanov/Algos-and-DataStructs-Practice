class UndergroundSystem:
    def __init__(self):
        self.trip_totals = {} # s1-s2: [total_trip_time, num_trips]
        self.check_in_station = {} # id: [stationName, t]

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in_station[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        s1, start_t = self.check_in_station[id]
        del self.check_in_station[id]
        key = f"{s1}-{stationName}"
        trip_time = t - start_t
        if key not in self.trip_totals:
            self.trip_totals[key] = [0, 0]
        self.trip_totals[key][0] += trip_time
        self.trip_totals[key][1] += 1


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, num_trips = self.trip_totals[f"{startStation}-{endStation}"]
        return total_time / num_trips


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)