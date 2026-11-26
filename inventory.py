#beginning feature 1: 
    
class  SupplyItem: 
    def __init__(self, item_id, name, unit_cost, min_stock, locations): 
        self.item_id=item_id 
        self.name=name
        self.unit_cost=unit_cost
        self.min_stock=min_stock 
        self.locations=locations
    
    
    
    def total_stock(self): 
        return sum(self.locations.values())
    
    
    def is_stock_below_min(self): 
       if self.total_stock()<self.min_stock:
           return True 
       else: 
           return False
       
        
     
    #incorporating feature 2 here, issuing stock with conditions
    
    def issue_stock(self,location,quantity): 
        if quantity<=0:
            return False 
        if location not in self.locations:
            return False 
        if quantity>self.locations[location]:
            return False 
          
        self.locations[location]-=quantity
        return True
          
       
    def add_stock(self,location,quantity): 
        if quantity<=0:
            return False
        if location not in self.locations:
            return False

        self.locations[location]+=quantity
        return True 


    def transfer_stock(self, from_location, to_location, quantity):
        if quantity<=0: 
            return False
        if from_location not in self.locations:
            return False 
        if quantity>self.locations[from_location]:
            return False
        
        self.locations[from_location]-=quantity
        self.locations[to_location]=self.locations.get(to_location,0)+quantity
        return True 






#continuing feature 1 below: 

def search_by_location(items, location): 
         matches=[]
         for item in items:
             if location in item.locations: 
                 matches.append((item, item.locations[location]))
     
        
         return matches
    
    
    
def search_by_item(items, term): 
        matches=[]
        clean_term=term.strip().lower()
        
        for item in items:
            if item.item_id.lower() == clean_term or clean_term in item.name.lower():
                matches.append(item)
        
        return matches
    
    
 
    
    
  
    
item = SupplyItem("P01", "Pipette Tips", 12.0, 20, {"Fridge A": 30})

print(item.issue_stock("Fridge A", 10), item.locations)        # True, {'Fridge A': 20}
print(item.issue_stock("Fridge A", 99), item.locations)        # False, {'Fridge A': 20}
print(item.add_stock("Fridge A", 15), item.locations)          # True, {'Fridge A': 35}
print(item.transfer_stock("Fridge A", "Shelf B", 5), item.locations)  # True, {'Fridge A': 30, 'Shelf B': 5}
print(item.transfer_stock("Fridge A", "Shelf B", 99), item.locations) # False, {'Fridge A': 30, 'Shelf B': 5}

print(search_by_location([item], "Shelf B"))                   # [(item, 5)]
print(search_by_item([item], "pipette"))                       # [item]
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       

