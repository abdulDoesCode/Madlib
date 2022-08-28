# this is handle ranom integer gives index from dictionary made 
from locale import locale_alias
from random import randint
import copy

# this is the mad lib project that will lead me back into coding with py

# types of ways to print in py 
# print("words to" + friendName)
# print("words to {}".format(friendName))  # this assigns the thing to curly
# print(f"words to {friendName}") # same as the previous entery

# this is the story and insert paceholders'{}' for the words ou want to randomly select
story = ( 
    "One day my {} friend and I decided to go to the {} concert in {}. "+
    "We really wanted to see the {} play the {}. So, we {} our {} "+ 
    "down to the {} and bought some {}s. We got into the concert and "+
    "it was a lot of fun. We ate some {} {} and drank some {} {}. "+
    "We plan to go again next time!"
)
# this is a dictionary that holds all the info dictTag:[itme(s) *in list*]
word_dict = {
    'adjective':['greedy','abrasive','grubby','groovy','rich','harsh','tasty','slow'],
    'city_name':['Istanbul','Cairo','Izmir','Antalya','Bodrum'],
    'noun':['people', 'map','music','dog','hamster','ball','hotdog','salad'],
    'action verb':['run','fall','crawl','scurry','cry','watch','swim','jump','bounce'],
    'bands noun':['NOLANDS','ACDC','Kendrik Lamar','Eminem','Arcitc Monkeys','Protugal. The Man','KALEO']
}

# creating a function that will random select words from the word_dict on the tag you made

def get_word(type,local_dict): # parameters 
    words = local_dict[type] # this chooses a randome index we made
    # print(words)
    count = len(words) - 1 # sub 1 to get valid length
    # print(count)
    index = randint(0,count) # this chooses the randome index number function
    # print(index)
    return local_dict[type].pop(index) # this returns the index we use and removes it from the list to not be reused


def createStory():
    ''' create a random story from word dict '''
    # create a local copy of the dict so that we can pop words as used
    local_dict = copy.deepcopy(word_dict) # here we replicate the dict using the deepcopy
    return story.format( # this is to fill the {} in the story written 
        get_word('adjective', local_dict), 
        get_word('bands noun', local_dict),
        get_word('city_name', local_dict),
        get_word('noun', local_dict),
        get_word('noun', local_dict),
        get_word('action verb', local_dict),
        get_word('noun', local_dict),
        get_word('noun', local_dict),
        get_word('noun', local_dict), 
        get_word('adjective', local_dict),
        get_word('noun', local_dict),
        get_word('adjective', local_dict),
        get_word('noun', local_dict)
)

story1 = createStory()
print("STORY: " + story)

