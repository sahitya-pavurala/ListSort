#!C:\Python26\python.exe
'''

Program to sort a list in such a way that all words are in the list are in
alphabetical order and all integers are in numerical order

'''
import os
import re
 


def getExistantFilename():
    '''

        Returns a filename chosen by a user that exists in the path given
        and also checks for exceptions

    '''

    inputfilename = raw_input( "What is the input file name? ")
    while( not os.path.exists( inputfilename ) ):
        inputfilename = raw_input( "Sorry, " + inputfilename + " not found. Try again: ")
    outputfilename = raw_input("what is the outputfile name ? ")
        
    return [inputfilename , outputfilename ]


def getAndOpenUsersChoiceOfFile():
    '''

        Returns user's chosen inputfilename , outfilename and connected file object
        exit(1) on IOError; exit(-1) on any other exception

    '''

    inputfilename , outputfilename = getExistantFilename()
	
    try:
        fileObj = open( inputfilename, 'r' )
    except IOError:
        print "IOError exception occured!!!"
        exit(1)
    except:
        print "something is wrong!!!"
        exit(-1)

    return [inputfilename,outputfilename , fileObj]

def fileProcess(fileObj):
    '''
        process the contents of the file and sort them in the list
        anf finally returning the finalList

    '''
    list1=[]
    list2=[]
    words=[]
    finalList= []
    j = 0
    k = 0
    for line in fileObj :
        word = line.rsplit()
        for item in range(len(word)) :
            new_string = re.sub("[^a-zA-Z0-9]","",word[item])
            words.append(new_string)
            if words[item].isdigit():
                words[item] = int(words[item])
                list2.append(words[item])
                list2.sort()
            else:
                list1.append(words[item])
                list1.sort()
    for i in range(len(words)) :
        if type(words[i]) == int and i <= len(words):
            finalList.append(list2[j])
            j = j+1
        else:
            finalList.append(list1[k])
            k = k+1
    
        
    return finalList


def fileWrite(finalList, outputfilename):
    '''

        Writing the contens of the finalList into the
        output file given as outputfilename

    '''
    for i in range(len(finalList)):
        finalList[i] = str(finalList[i])
    fw = open(outputfilename , 'w')
    #for line in finalList:
    for line in finalList:
        fw.write(line)
        fw.write(' ')

    fw.close()
    



def main():
    
    inputfilename,outputfilename, fileObj = getAndOpenUsersChoiceOfFile()

    finalList = fileProcess( fileObj )
    fileWrite(finalList , outputfilename)
    


if __name__ == '__main__':
    main()
    
