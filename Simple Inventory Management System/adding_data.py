import json
#adding datas into json file

products_details={
    "1001":{"Name":"Hamam","Quantity":"1 piece","Price":"35","Stock":"25"},
    "1002":{"Name":"Lifebuoy","Quantity":"1 piece","Price":"30","Stock":"45"},
    "1003":{"Name":"Hamam Lemon","Quantity":"1 piece","Price":"35","Stock":"55"},
    "1004":{"Name":"Lux","Quantity":"1 piece","Price":"28","Stock":"40"},
    "1005":{"Name":"Mysore Sandal","Quantity":"1 piece","Price":"38","Stock":"25"},
    "1006":{"Name":"Medimix","Quantity":"1 piece","Price":"26","Stock":"32"},
    "1007":{"Name":"Chandrika","Quantity":"1 piece","Price":"26","Stock":"30"},
    "1008":{"Name":"Margo","Quantity":"1 piece","Price":"30","Stock":"30"},
    "1009":{"Name":"Dove","Quantity":"1 piece","Price":"29","Stock":"30"},
    "1010":{"Name":"Dettol","Quantity":"1 piece","Price":"33","Stock":"30"},
    "1011":{"Name":"Santoor","Quantity":"1 piece","Price":"27","Stock":"30"},
    "1012":{"Name":"Pears Blue","Quantity":"1 piece","Price":"40","Stock":"35"},
    "1013":{"Name":"Pears Yellow","Quantity":"1 piece","Price":"42","Stock":"20"},
    "1014":{"Name":"Pears Green","Quantity":"1 piece","Price":"42","Stock":"20"},
    "1015":{"Name":"Lux International","Quantity":"1 piece","Price":"35","Stock":"25"},
    "1016":{"Name":"Cinthol Original","Quantity":"1 piece","Price":"35","Stock":"25"},
    "1017":{"Name":"Cinthol Lemon","Quantity":"1 piece","Price":"35","Stock":"25"},
    "1018":{"Name":"Cinthol Cool","Quantity":"1 piece","Price":"35","Stock":"25"},
    "1019":{"Name":"Liril","Quantity":"1 piece","Price":"30","Stock":"50"},
    "1020":{"Name":"Nature Power Rose","Quantity":"1 piece","Price":"30","Stock":"28"},
    "1021":{"Name":"Nature Power Lemon","Quantity":"1 piece","Price":"30","Stock":"28"},
}

#before placing orders or adding products 
js=json.dumps(products_details)
fd=open("before_record.json","w")
fd.write(js)
fd.close()