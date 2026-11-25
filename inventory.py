class SupplyItem: 
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
    
    

