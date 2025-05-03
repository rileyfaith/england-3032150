class HashMap:
    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % self.size
    
    def _bucket(self, key):
        return self.hash_table[self._hash_function(key)]
    
    def put(self, key, value):
        self._bucket(key).append((key, value))

    def get(self, key) -> int:
        bucket = self._bucket(key)
        values = [v for k, v in bucket if k == key]
        return values or None

    def remove(self, key, value):
        bucket = self._bucket(key)
        if not bucket:
            return False
        
        removed = False
        if value is None:
            orig_len = len(bucket)
            bucket[:] = [(k, v) for k, v in bucket if k != key]
            removed = orig_len != len(bucket)
        else:
            for idx, (k, v) in enumerate(bucket):
                if k == key and v == value:
                    del bucket[idx]
                    removed = True
                    break
        return removed

    def display(self) -> list[list]:
        contents: list[list] = []
        for i, bucket in enumerate(self.hash_table):
            plain_bucket = [v for _, v in bucket]
            contents.append(plain_bucket)
            print(f"Bucket {i:02d}: {plain_bucket}")
        return contents

    def max_passengers_in_flight(self, flight_number):
        flights = self.get(flight_number)
        if not flights:
            return None
        max_node = max(flights, key=lambda fn: fn.passengers)
        return max_node.trip_id, max_node.passengers


class FlightNode:

    def __init__(self, flight_number, trip_id, passengers):
        self.flight_number = flight_number
        self.trip_id = trip_id
        self.passengers = passengers

    def __repr__(self):
        return (
            f"FlightNode(flightnumber) = {self.flight_number}, "
            f"trip_id = {self.trip_id}, passengers = {self.passengers}"
        )
    
# Display the hash map
my_hash_map = HashMap(7)
0, 1, 4, 9, 16, 25, 36, 49, 64, 81
my_hash_map.put("aaa", 0)
my_hash_map.put("bbb", 1)
my_hash_map.put("ccc", 4)
my_hash_map.put("ddd", 9)
my_hash_map.put("eee", 16)
my_hash_map.put("fff", 25)
my_hash_map.put("ggg", 36)
my_hash_map.put("hhh", 49)
my_hash_map.put("ccc", 64)
my_hash_map.put("ccc", 81)
my_hash_map.display()  

# Retrieve values
print("Retrieve values:")
print("aaa:", my_hash_map.get("aaa"))  
print("bbb:", my_hash_map.get("bbb"))
print("ccc:", my_hash_map.get("ccc"))

# Remove a key-value pair
my_hash_map.remove("bbb", 1)  

# Display the updated hash map
my_hash_map.display() 

#Max Passengers on Trip
my_map = HashMap(11)
# Add flight nodes (flight_number, trip_id, passengers)
my_map.put(16, FlightNode(16, "Trip 1", 300))
my_map.put(16, FlightNode(16, "Trip 2", 700))
my_map.put(29, FlightNode(29, "Trip 1", 800))
my_map.put(29, FlightNode(29, "Trip 2", 250))
my_map.put(36, FlightNode(29, "Trip 3", 500))
my_map.put(36, FlightNode(36, "Trip 1", 500))
my_map.put(36, FlightNode(36, "Trip 2", 340))
my_map.put(36, FlightNode(36, "Trip 3", 900))
my_map.put(36, FlightNode(36, "Trip 4", 400))
my_map.put(49, FlightNode(49, "Trip 1", 250))
my_map.put(49, FlightNode(49, "Trip 2", 550))

max_passengers = my_map.max_passengers_in_flight(49)
if max_passengers is not None:
    print("Largest number of people in flight at once :", max_passengers)
else:
    print("Flight not found in the map")
