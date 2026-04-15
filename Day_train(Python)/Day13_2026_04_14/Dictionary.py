capital = {
    "United States" : "Washington DC",
    "Japan" : "Tokyo",
    "France" : "paris",
    "Russia" : "Moscow",
}

# get()
print(capital.get("Japan"))
print(capital.get("France"))

# update
capital.update({"Germany":"Berlin"})
print(capital)

# pop
capital.pop("United States")
print(capital)

# values()
print(capital.values())

# items()
print(capital.items())