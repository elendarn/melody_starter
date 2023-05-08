#library for understanding music
from music21 import *
#for listing down the file names
import os
#Array Processing
import numpy as np
#save&load dictionary
import pickle

notes_dict={}

def read_midi(file):
    '''
    Input: directory of midi file (str), Output: notes of given song (list)
    ----------------------------------------------------------------------    
    Takes given midi and translate choosen instrument chords and notes and return as a list
    '''
    
    print("Loading Music File:  ",file)
    
    notes=[]
    notes_to_parse = None
    
    #parsing a midi file
    midi = converter.parse(file)

    #grouping based on different instruments
    s2 = instrument.partitionByInstrument(midi)

    #Looping over all the instruments
    for part in s2.parts:    
        #select elements of only piano
        if 'Piano' in str(part): 
            notes_to_parse = part.recurse() #See different piano channels: piano right, piano,piano left. 
                                            #Lib method or sth
      
            #finding whether a particular element is note or a chord
            for element in notes_to_parse:  
                #note
                if isinstance(element, note.Note):
                    notes.append(str(element.pitch))                    
                #chord
                if isinstance(element, chord.Chord):
                    notes.append('.'.join(str(n) for n in element.normalOrder))
           
    return notes



def artist_collection(path,artist_names):
    '''
    Input: list of directories of midi files, Output: notes of all songs of all artists
    ------------------------------------------------------------------------------------
    '''
    for count, artist in enumerate(artist_names, start=1):
        the_path=(path+artist+'/')
        files=[i for i in os.listdir(the_path) if i.endswith(".mid")]

        #reading each midi file into a dictionary. Keys, song number; values, notes of that song
        for k, i in enumerate(files, start=1):
            print(f'=================================== Loading files {k}/{len(files)}, artists: {count}/{len(artist_names)}')
            label=count
            notes_dict[label] = read_midi(the_path+i)
    
    return notes_dict
        
def save_collection(collection, save_file_name):
    '''
    Input:collection:      dictionary of all songs. Keys song, values notes
          save_file_name:  name of will be saved file
          
    Output: Pickle file
    '''
    with open(f'saved_pickle_files/{save_file_name}.pickle', 'wb') as handle:
        pickle.dump(collection, handle, protocol=pickle.HIGHEST_PROTOCOL)
    
    
def main(path, artist_names, save_file_name):
    save_collection(artist_collection(path, artist_names), save_file_name)

path='midi_files/'
all_artist_names = [i for i in os.listdir(path)]
all_artist_names=all_artist_names[0:17]
saved='bach_col'

main(path, all_artist_names, saved)
    
