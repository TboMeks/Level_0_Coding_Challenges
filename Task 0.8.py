def convert(minutes):
    print(minutes//60)
    print(minutes % 60)


minutes = int(input())
print(str(minutes//60)+" hours "+str(minutes % 60)+" minutes")
