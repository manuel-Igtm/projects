we have create one product with a product key
code:
catergory1 = Category.objects.create(name=stationery)
product1 = Product.objects.create(name = "stapler",description = "it is used to staple papers",price = 300, category= catergory1)

