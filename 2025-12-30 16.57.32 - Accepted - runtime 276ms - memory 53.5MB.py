from sortedcontainers import SortedSet

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_to_cuisine = {}  # food -> cuisine
        self.food_to_rating = {}   # food -> rating
        self.cuisine_foods = {}    # cuisine -> SortedSet of (-rating, food)
        
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_to_cuisine[food] = cuisine
            self.food_to_rating[food] = rating
            
            if cuisine not in self.cuisine_foods:
                self.cuisine_foods[cuisine] = SortedSet()
            self.cuisine_foods[cuisine].add((-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.food_to_cuisine[food]
        old_rating = self.food_to_rating[food]
        
        # Remove old entry
        self.cuisine_foods[cuisine].discard((-old_rating, food))
        
        # Add new entry
        self.food_to_rating[food] = newRating
        self.cuisine_foods[cuisine].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        # Return the food with highest rating (smallest -rating, then lexicographically smallest name)
        return self.cuisine_foods[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)