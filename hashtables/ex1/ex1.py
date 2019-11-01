#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve,)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for item in range(length):
        # Ask for the matching pair, if found return it, else add item to hashtable
        package_pair = hash_table_retrieve(ht, limit - weights[item])
        if package_pair is not None:
            return (item, package_pair)
        else:
            hash_table_insert(ht, weights[item], item)
    # No match, return None
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
