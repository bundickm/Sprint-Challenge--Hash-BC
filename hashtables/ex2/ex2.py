#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve,)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    # Add all tickets to the table for lookup, set start position if source is 'NONE'
    for i in range(length):
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)
        if tickets[i].source is 'NONE':
            route[0] = tickets[i].destination

    # Loop through asking each leg what it's destination is and adding it to the route
    for i in range(length):
        # print(route)
        if route[i-1] is not None:
            route[i] = hash_table_retrieve(hashtable, route[i-1])
    return route
