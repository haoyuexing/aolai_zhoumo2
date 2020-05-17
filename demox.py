import faker


f = faker.Faker("zh_CN")

for i in range(10):
    print(f.phone_number())
