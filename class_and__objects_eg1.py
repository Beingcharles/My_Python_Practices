class peak_district:
    name=""
    hike=""
    def peaks(self):
        print("let's explore the peaks")
    def lake(self):
        print("be careful, the water in the lake is freezing")

charles=peak_district()
balaji=peak_district()

charles.name="Charles"
balaji.name="Balaji"

charles.hike="yes"
balaji.hike="no"

charles.swim="no"
balaji.swim="yes"

print(charles.name)
print(balaji.name)
print("hike: ",charles.hike)
print("hike: ",balaji.hike)
print("swim: ",charles.swim)
print("swim: ",balaji.swim)

charles.peaks()
balaji.lake()


