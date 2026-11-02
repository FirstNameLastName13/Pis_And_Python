doll_one = {
    "size": 5,
    "inner_doll": None
}
doll_two = {
    "size": 12, 
    "inner_doll": {
        "size": 7, 
        "inner_doll": None
    }
}
doll_three = {
    "size": 20, 
    "inner_doll": {
        "size": 15, 
        "inner_doll": {
            "size": 10, 
            "inner_doll": {
                "size": 3, 
                "inner_doll": None
            }
        }
    }
}
def open_doll(doll):
    if doll["inner_doll"] == None:
        return doll["size"]
    else:
        return open_doll(doll["inner_doll"])

print(open_doll(doll_one))
