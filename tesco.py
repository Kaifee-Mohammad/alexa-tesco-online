import requests

# configuration
tesco_grocery_url = 'https://dev.tescolabs.com/grocery/products/'
tesco_product_url = 'https://dev.tescolabs.com/product/'
# key
ocp_key = 'f772cb0b7a29449da9140e2cb20bffea'

class Tesco:
    def FindProduct(self, query = '', offset = 0, limit = 1):
        response = requests.get(tesco_grocery_url,
                                params = {'query': query, 
                                        'offset': offset,
                                        'limit': limit
                                        },
                                headers = {'Ocp-Apim-Subscription-Key': ocp_key })
        if response:
            # print('success')
            # print(response.url)
            data = response.json()
            #count = 1
            return {
                "name": data['uk']['ghs']['products']['results'][0]["name"], 
                "price": data['uk']['ghs']['products']['results'][0]["price"]
                }
            # for r in data['uk']['ghs']['products']['results']:
            #     print(f'{count}. {r["name"]}, price {r["price"]}')
            #     count +=1
        else:
            print('failed')
    
if __name__ == '__main__':
    t = Tesco()
    # assert t.FindProduct('cawston', 0, 1)[0] == 'Cawston Press Rhubarb 4X330', 'product not found.'
    print(t.FindProduct('cawston', 0, 1)["name"])






