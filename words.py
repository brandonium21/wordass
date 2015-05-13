from random_words import RandomWords
import unirest
import json
import time
import pprint
import pickle

randList = []
rw = RandomWords()
word_to_array = {}
def love():
    global word_to_array
    for x in xrange(0,10):
        random_word = rw.random_word()
        while random_word in word_to_array:
            random_word = rw.random_word()
        response = unirest.get("https://twinword-word-associations-v1.p.mashape.com/associations/?entry=" + random_word,headers={"X-Mashape-Key": "ipLwvszUNbmshWjvlVeG6uzWEFFnp1uZ62pjsn5Ot3dfqkzY0Z"})
        body_info = response.body
        #print body_info["associations_array"]
        wordass_array = body_info.get("associations_array")
        word_to_array[random_word] = wordass_array
        time.sleep(.01)

def clean_data():
    for key in word_to_array.keys():
        if word_to_array.get(key) == None:
            del word_to_array[key]
            print "deleted: " + key
def pickleit():
    global word_to_array

    pkl_file = open('word.pkl', 'rb')
    word_to_array = pickle.load(pkl_file)
    pkl_file.close()
    if type(word_to_array) is list:
        word_to_array = {}
    love()
    clean_data()
    outputfile = open('word.pkl', 'wb')
    pickle.dump(word_to_array, outputfile)
    outputfile.close()

    #pprint.pprint(len(word_to_array.keys()))

pickleit()
