## To add new store details use POSTMAN tool
    
### URL : http://127.0.0.1:5000/store
    Method will be POST.
    Content type will be appplication/json.
    Pass below data in Raw format in Body Tag.
    {
      
        "items": [
            {
                "name": "apple",
                "price": 100
            }
        ],
        "name": "beautiful store 4"
    }

## To get store details of existing store
### URL : http://127.0.0.1:5000/store/beautiful store 2
    Method will be GET
    here beautiful store 2 is store name
    This API will fetch store details and item details both

## To add items to existing store 
### URL : http://127.0.0.1:5000/store/beautiful store 2/item
    Method will be post
    Pass below data in Raw format in Body Tag.
    
        {
                "name": "plants",
                "price": 50
            }
 

## To get item details in existing store
### URL : http://127.0.0.1:5000/store/beautiful store 2/item
    Method will be GET
    here beautiful store 2 is store name
    This API will give only item details 
       