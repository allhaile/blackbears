interests = {"Outdoors": False, "Restaurants": False, "Art": False, "Landmarks and Historical Sites": False, "Shopping": False}

#likes is an array of catagories that exist in intersts. 
def newUser(self, likes):
	for l in likes:
		self.interests(l) = True


