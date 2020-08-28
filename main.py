import random

adjectives = [
    "Abrupt", "Adorable", "Adventurous", "Aggressive", "Agitated", "Alert",
    "Aloof", "Amiable", "Amused", "Annoyed", "Antsy", "Anxious", "Appalling",
    "Appetizing", "Apprehensive", "Arrogant", "Ashamed", "Astonishing",
    "Attractive", "Average", "Batty", "Beefy", "Bewildered", "Biting",
    "Bitter", "Bland", "Blushing", "Bored", "Brave", "Bright", "Broad",
    "Bulky", "Burly", "Charming", "Cheeky", "Cheerful", "Chubby", "Clean",
    "Clear", "Cloudy", "Clueless", "Clumsy", "Colorful", "Colossal",
    "Combative", "Comfortable", "Condemned", "Condescending", "Confused",
    "Contemplative", "Convincing", "Convoluted", "Cooperative", "Corny",
    "Costly", "Courageous", "Crabby", "Creepy", "Crooked", "Cruel",
    "Cumbersome", "Curved", "Cynical", "Dangerous", "Dashing", "Decayed",
    "Deceitful", "Deep", "Defeated", "Defiant", "Delicious", "Delightful",
    "Depraved", "Depressed", "Despicable", "Determined", "Dilapidated",
    "Diminutive", "Disgusted", "Distinct", "Distraught", "Distressed",
    "Disturbed", "Dizzy", "Drab", "Drained", "Dull", "Eager", "Ecstatic",
    "Elated", "Elegant", "Emaciated", "Embarrassed", "Enchanting",
    "Encouraging", "Energetic", "Enormous", "Enthusiastic", "Envious",
    "Exasperated", "Excited", "Exhilarated", "Extensive", "Exuberant", "Fancy",
    "Fantastic", "Fierce", "Filthy", "Flat", "Floppy", "Fluttering", "Foolish",
    "Frantic", "Fresh", "Friendly", "Frightened", "Frothy", "Frustrating",
    "Funny", "Fuzzy", "Gaudy", "Gentle", "Ghastly", "Giddy", "Gigantic",
    "Glamorous", "Gleaming", "Glorious", "Gorgeous", "Graceful", "Greasy",
    "Grieving", "Gritty", "Grotesque", "Grubby", "Grumpy", "Handsome", "Happy",
    "Harebrained", "Healthy", "Helpful", "Helpless", "High", "Hollow",
    "Homely", "Horrific", "Huge", "Hungry", "Hurt", "Icy", "Ideal", "Immense",
    "Impressionable", "Intrigued", "Irate", "Irritable", "Itchy", "Jealous",
    "Jittery", "Jolly", "Joyous", "Juicy", "Jumpy", "Kind", "Lackadaisical",
    "Large", "Lazy", "Lethal", "Little", "Lively", "Livid", "Lonely", "Loose",
    "Lovely", "Lucky", "Ludicrous", "Macho", "Magnificent", "Mammoth",
    "Maniacal", "Massive", "Melancholy", "Melted", "Miniature", "Minute",
    "Mistaken", "Misty", "Moody", "Mortified", "Motionless", "Muddy",
    "Mysterious", "Narrow", "Nasty", "Naughty", "Nervous", "Nonchalant",
    "Nonsensical", "Nutritious", "Nutty", "Obedient", "Oblivious", "Obnoxious",
    "Odd", "Old-fashioned", "Outrageous", "Panicky", "Perfect", "Perplexed",
    "Petite", "Petty", "Plain", "Pleasant", "Poised", "Pompous", "Precious",
    "Prickly", "Proud", "Pungent", "Puny", "Quaint", "Quizzical", "Ratty",
    "Reassured", "Relieved", "Repulsive", "Responsive", "Ripe", "Robust",
    "Rotten", "Rotund", "Rough", "Round", "Salty", "Sarcastic", "Scant",
    "Scary", "Scattered", "Scrawny", "Selfish", "Shaggy", "Shaky", "Shallow",
    "Sharp", "Shiny", "Short", "Silky", "Silly", "Skinny", "Slimy", "Slippery",
    "Small", "Smarmy", "Smiling", "Smoggy", "Smooth", "Smug", "Soggy", "Solid",
    "Sore", "Sour", "Sparkling", "Spicy", "Splendid", "Spotless", "Square",
    "Stale", "Steady", "Steep", "Sticky", "Stormy", "Stout", "Straight",
    "Strange", "Strong", "Stunning", "Substantial", "Successful", "Succulent",
    "Superficial", "Superior", "Swanky", "Sweet", "Tart", "Tasty", "Teeny",
    "Tender", "Tense", "Terrible", "Testy", "Thankful", "Thick", "Thoughtful",
    "Thoughtless", "Tight", "Timely", "Tricky", "Trite", "Troubled", "Uneven",
    "Unsightly", "Upset", "Uptight", "Vast", "Vexed", "Victorious", "Virtuous",
    "Vivacious", "Vivid", "Wacky", "Weary", "Whimsical", "Whopping", "Wicked",
    "Witty", "Wobbly", "Wonderful", "Worried", "Yummy", "Zany", "Zealous",
    "Zippyadorable", "Acrobatic", "Adaptable", "Agile", "Arboreal", "Ardent",
    "Artful", "Astute", "Attentive", "Authentic", "Avid", "Beardless",
    "Benevolent", "Bionic", "Blissful", "Bodacious", "Brilliant", "Bubbly",
    "Careful", "Cautious", "Circumspect", "Cognizant", "Collectible",
    "Communicative", "Compact", "Compassionate", "Constant", "Convivial",
    "Cordial", "Cosmic", "Creative", "Cryptic", "Crystalline", "Cunning",
    "Curious", "Dancing", "Daring", "Dauntless", "Dazzling", "Dexterous",
    "Discerning", "Distinctive", "Dreaming", "Dynamic", "Earnest", "Easygoing",
    "Eccentric", "Effervescent", "Elaborate", "Eloquent", "Elusive",
    "Energized", "Erudite", "Essential", "Ethereal", "Extraordinary", "Exotic",
    "Fearless", "Feisty", "Fiery", "Flourishing", "Flying", "Focused",
    "Fortunate", "Frolicking", "Gargantuan", "Gesticulating", "Gleeful",
    "Grateful", "Gregarious", "Harmonious", "Hatless", "Heroic", "Hydraulic",
    "Idealistic", "Illustrious", "Imaginative", "Impartial", "Imperturbable",
    "Improbable", "Incredible", "Inimitable", "Influential", "Inquisitive",
    "Insightful", "Inspired", "Intrepid", "Intricate", "Intuitive",
    "Invaluable", "Inventive", "Jaunty", "Joyful", "Jubilant", "Jumping",
    "Keen", "Laughing", "Legendary", "Lenient", "Loquacious", "Luminescent",
    "Magnetic", "Majestic", "Marvelous", "Masked", "Mechanical", "Mercurial",
    "Meritorious", "Merry", "Methodical", "Meticulous", "Mighty", "Mirthful",
    "Mischievous", "Modest", "Momentous", "Multicolored", "Murmuring",
    "Musical", "Mustachioed", "Nascent", "Neighborly", "Noble", "Nomadic",
    "Noncommittal", "Observant", "Omnidirectional", "Omnivorous", "Optimal",
    "Optimistic", "Otherworldly", "Outgoing", "Outspoken", "Panoramic",
    "Peaceful", "Perceptive", "Perpetual", "Perplexing", "Perspicacious",
    "Philosophical", "Picturesque", "Playful", "Practical", "Precise",
    "Precocious", "Prestigious", "Primeval", "Primordial", "Prismatic",
    "Proactive", "Proficient", "Prototypical", "Prudent", "Purposeful",
    "Qualified", "Quotable", "Radiant", "Reclusive", "Recurring", "Reflective",
    "Rejoicing", "Relaxed", "Remarkable", "Renowned", "Resilient", "Resolute",
    "Resourceful", "Rigorous", "Roaring", "Salient", "Salubrious", "Sanguine",
    "Sapient", "Satisfied", "Scholarly", "Scintillating", "Scrupulous",
    "Selective", "Sincere", "Singing", "Sleek", "Sleepy", "Sophisticated",
    "Spectacular", "Squeaky", "Stately", "Strategic", "Striped", "Stupendous",
    "Stylish", "Sufficient", "Swimming", "Symbolic", "Symmetrical", "Taciturn",
    "Terrestrial", "Tessellated", "Theoretical", "Thriving", "Timeless",
    "Topographical", "Transparent", "Tranquil", "Ubiquitous", "Uncanny",
    "Unclouded", "Undisputed", "Unexpected", "Unfathomable", "Unflappable",
    "Unique", "Universal", "Unofficial", "Unseen", "Unthinkable", "Uproarious",
    "Variegated", "Versatile", "Vigilant", "Vigorous", "Vociferous",
    "Wandering", "Watchful", "Windswept", "Wondrous", "Zestful"
]

# random.shuffle(adjectives)

# for i in range (0, len(adjectives)):
# 	adjectives[i] = adjectives[i].capitalize()

bonuses = []

for adjective in adjectives:
    bonus = []
    bonus.append(random.randint(5, 30) / 10)
    bonus.append(random.randint(5, 30) / 10)
    bonus.append(random.randint(5, 30) / 10)
    bonus.append(random.randint(5, 30) / 10)
    bonuses.append(bonus)

implicits = dict(zip(adjectives, bonuses))

print(implicits)
