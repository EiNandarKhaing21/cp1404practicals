from prac_06.guitar import Guitar

guitar_1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar_2 = Guitar("Fender Stratocaster", 2014, 765.40)
guitar_3 = Guitar("Line 6 JTV-59", 1976, 12012.90)

print(guitar_1)
print(guitar_1.get_age())
print(guitar_1.is_vintage())
print("------")
print(guitar_2)
print(guitar_2.get_age())
print(guitar_2.is_vintage())
print("------")
print(guitar_3)
print(guitar_3.get_age())
print(guitar_3.is_vintage())