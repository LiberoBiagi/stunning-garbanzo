def fuzzy_logic_movement(self, tile):
       
        fuzzy_movement = self.combine_rules(
            self.rule_food_availability(tile),
            self.rule_terrain_conditions(tile),
            self.rule_proximity_to_home(tile)
        )

        return fuzzy_movement

    def combine_rules(self, *rules):
      
        weights = [0.5, 0.3, 0.2]  
        combined_value = sum(w * r for w, r in zip(weights, rules))

        return combined_value

    def rule_food_availability(self, tile):
       
        food_level = tile.get_density() if tile.vegetob else 0  
        nearby_individuals = tile.entity.social if tile.entity else 0  

       
        if food_level < 50 and nearby_individuals > 0.3:
            return 0.8  
        else:
            return 0.2  

    def rule_terrain_conditions(self, tile):
        
        terrain_conditions = tile.land  
        if terrain_conditions == 0:
            return 0.7 
        else:
            return 0.3  

    def rule_proximity_to_home(self, tile):
        
        proximity_to_home = tile.entity.social if tile.entity else 0.5  

       
        if proximity_to_home > 0.7:
            return 0.6  
        else:
            return 0.4 

