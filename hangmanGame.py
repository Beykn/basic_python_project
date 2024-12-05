import random 
fruits = {
    "apple": "A sweet and juicy fruit, usually red, green, or yellow in color.",
    "pear": "A sweet and slightly juicy fruit, typically elongated in shape.",
    "banana": "A tropical fruit, soft and sweet, with a yellow peel.",
    "strawberry": "A small red fruit, usually sweet with a slightly tangy taste.",
    "orange": "An orange-colored citrus fruit, rich in vitamin C and very juicy.",
    "melon": "A large, sweet fruit, usually with yellow rind and juicy flesh.",
    "watermelon": "A green-skinned fruit with red, juicy flesh, perfect for summer.",
    "grape": "Small, round fruits that come in various colors, sweet or slightly tart.",
    "cherry": "Small and bright red, sweet and slightly juicy fruit.",
    "peach": "A soft, fuzzy fruit with a sweet and aromatic taste."
}

vegetables = {
    "carrot": "A crunchy orange root vegetable, rich in beta-carotene.",
    "broccoli": "A green vegetable with a tree-like structure, rich in vitamins.",
    "spinach": "A leafy green vegetable, packed with iron and nutrients.",
    "potato": "A starchy root vegetable, versatile for many dishes.",
    "tomato": "A red, juicy vegetable often used in salads and sauces.",
    "onion": "A bulb vegetable, used for its strong flavor in cooking.",
    "garlic": "A pungent bulb vegetable, adds flavor and has health benefits.",
    "pepper": "A crunchy vegetable that can be sweet, mild, or spicy.",
    "cucumber": "A refreshing green vegetable, often eaten raw in salads.",
    "cabbage": "A leafy vegetable with tightly packed leaves, used in salads and soups.",
    "pumpkin": "A large orange squash, used in soups, pies, and decorations.",
    "corn": "A yellow vegetable with kernels on a cob, sweet and starchy."
}

items = {
    "table": "A flat surface supported by legs, used for work or dining.",
    "chair": "A piece of furniture designed for sitting, often with a backrest.",
    "lamp": "A device that provides light, usually electric.",
    "clock": "A device used to measure and display time.",
    "book": "A collection of written pages bound together, used for reading.",
    "pen": "A tool used for writing or drawing with ink.",
    "backpack": "A bag with shoulder straps, used for carrying items.",
    "bottle": "A container with a narrow neck, used to store liquids.",
    "phone": "A portable electronic device for communication.",
    "mirror": "A reflective surface, typically used for checking appearance."
}

clothes = {
    "tshirt": "A casual short-sleeved top, usually made of cotton.",
    "jeans": "Durable, denim pants, popular for casual wear.",
    "jacket": "A short coat worn for warmth or style.",
    "sweater": "A warm knitted garment, typically with long sleeves.",
    "dress": "A one-piece garment for women, covering the body and legs.",
    "skirt": "A garment that hangs from the waist, covering the legs partially.",
    "scarf": "A long piece of fabric worn around the neck for warmth or style.",
    "hat": "A head covering worn for protection or fashion.",
    "shoes": "Footwear designed to protect and comfort the feet.",
    "socks": "Soft coverings for the feet, worn inside shoes."
}

catagory = {
    "1" : "fruits",
    "2" : "vegetables",
    "3" : "items",
    "4" : "clothes"
}

def findWord(str2):
    live = 7
    while(live != 0):
        letter = str(input('Enter a letter: '))
        if letter in str2:
            print(letter)
        else:
            live -= 1
            

def createUnderline(str1):
    strlen = len(str1)
    for i in range(strlen):
        print('_ ', end='')
    print()
    word = []
    for x in str1:
        word.append(x)    
    print(word)
    
    findWord(word)
    
    

print('CATAGORIES:')
for x in catagory:
    print('-',catagory[x].upper())
        
user_input = str(input('Choose a category: '))
lowercase_input = user_input.lower()
print(catagory.values())

    
if lowercase_input not in catagory.values():
    print('There is not such a catagory')
    
elif lowercase_input in globals():  # Eğer global değişkenlerde bu isimde bir sözlük varsa
    chosen_dict = globals()[lowercase_input]  # Sözlüğü alın
    makelistkeys = list(chosen_dict)
    makelistvalues = list(chosen_dict.values())
    num =len(makelistkeys)
  
    randomChoise = random.randrange(1,num+1)
    
    print('Description for secret word: ',makelistvalues[randomChoise])
    
    createUnderline(makelistkeys[randomChoise])
    
    # random_value = random.choice(list(chosen_dict.values()))  # Rastgele bir değer seç
    # print(f"Random value from {lowercase_input}: {random_value}")
else:
    print("The dictionary you entered does not exist.")   

