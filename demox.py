import faker


f = faker.Faker("zh_CN")

print(f.name())
print(f.phone_number())
print(f.street_address())
print(f.postcode())
