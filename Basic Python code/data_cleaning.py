import json
def load_data(filename):
    with open(filename , "r") as f:
        data = json.load(f)
    return data
data = load_data("store_data.json")   

#clean data
def clean_data(data):
    text_to_num ={ "one":1,"two":2,"three":3,"four":4,"five":5}
    cleaned_data =[]
    unique_users =set()


    for user in data:
        #clean ratings
        raw_rating = str(user["rating"]).strip().lower()
        if( raw_rating  in text_to_num):
             raw_rating = text_to_num[ raw_rating ]
        user["rating"] = raw_rating  

        #handle missing
        raw_age = user.get("age")
        if(raw_age == None or str(raw_age).strip() == ""):
            user["age"] = None
        
        #duplicates
        if(user["name"].strip() in unique_users ):
          continue
        
        unique_users.add(user["name"])   
        cleaned_data.append(user)   
        
    return cleaned_data

clean_data(data)