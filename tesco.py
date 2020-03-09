import requests
import json

# configuration
tesco_grocery_url = 'https://dev.tescolabs.com/grocery/products/'
tesco_product_url = 'https://dev.tescolabs.com/product/'
ocp_key = 'f772cb0b7a29449da9140e2cb20bffea'

class Tesco:
    def FindProduct(self, product = '', offset = 0, limit = 1):
        response = requests.get(tesco_grocery_url,
                                params={'query': product, 
                                        'offset': offset,
                                        'limit': limit
                                        },
                                headers={'Ocp-Apim-Subscription-Key': ocp_key })
        if response:
            print('success')
            print(response.url)
            data = response.json()
            count = 1
            #print(data['uk']['ghs']['products']['results'])
            for r in data['uk']['ghs']['products']['results']:
                print(f'{count}. {r["name"]}, price {r["price"]}')
                count +=1
        else:
            print('failed')

if __name__ == '__main__':

    t = Tesco()

    t.FindProduct('kenco smooth instant coffee', 0, 10)






