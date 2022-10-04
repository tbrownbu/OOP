import InsectClass as i

#this creates two different instances. Housefly and mosquito
housefly = i.insect(2,4)
mosquito = i.insect(4,8)


housefly.flight_length()
mosquito.flight_length()


print("The housefly can fly up to", housefly.get_flight())
print("The mosquito can fly up to", mosquito.get_flight())
