class Laptop:
    price=0
    processor=""
    ram=""

HP=Laptop()
DELL=Laptop()
LENOVO=Laptop()

HP.price="Price: 49999"
HP.processor="Processor: i5"
HP.ram="Ram: 8GB"

DELL.price="Price: 69999"
DELL.processor="Processor: i5"
DELL.ram="Ram: 12GB"

LENOVO.price="Price: 89999"
LENOVO.processor="Processor: i7"
LENOVO.ram="Ram: 16GB"

print(HP.ram)
print(DELL.price)
print(LENOVO.processor)

