#Assignment:    Assignment 8D
#
#Program Name:  ks_assignment_8D.py
#
#Purpose:       To pull song data from an xml file and display it.
#
#Author:        Keaton Smith
#Course:        192CIS115.600
#
#Created:       April 5, 2019


# Set named constants
RECORDS = "student_files8D/Records.xml" # Path to the xml file

HEADER = '''
               *************************************************                
               *** Listing of The Top 100 Pop Hits From 2015 ***                
               *************************************************
               
 #                     Artist                                Title                Length
---   ----------------------------------------   ------------------------------   ------
'''.strip('\n')
# Template for displaying a song's info
SONG_TEMPLATE = "{0:>3}   {1:<40}   {2:<30}   {3:^6}"

def main():
    #
    #   Function:   main
    #
    #   Author:     Keaton Smith
    #   Date:       April 5, 2019
    #   Filename:   ks_assignment_8D.py
    #
    #   Description:
    #
    #   This function will take song data from the file at the path RECORDS and
    #   will display the information found in a organized manner.
    #
    #   Arguments:
    #       None
    #
    #   Returns:
    #       None
    #

    # Print the header
    print(HEADER)

    # Get the song info from the file.
    songs = loadSongs(RECORDS)

    # count is used to number the songs in order.
    count = 0
    for song in songs:
        count += 1
        # Print out the song's info
        print(SONG_TEMPLATE.format(count,
                                   song['artist'],
                                   song['name'],
                                   song['length']))

def loadSongs(filePath):
    #
    #   Function:   loadSongs
    #
    #   Author:     Keaton Smith
    #   Date:       April 5, 2019
    #   Filename:   ks_assignment_8D.py
    #
    #   Description:
    #
    #   This function will load a custom xml file and take info about songs from
    #   it.
    #
    #   Arguments:
    #       str: filePath - The path to the file to be loaded and parsed.
    #
    #   Returns:
    #       list: songs - Contains dictionary objects consisting of song info
    #                       using the following keys: 'artist', 'name', 'length'
    #

    # Open file
    with open(filePath, 'r') as file:
        # Initialize variables
        songs = []          # List to hold all the songs.
        nameTag = False     # Flag for if a name opening tag is found
        lengthTag = False   # Flag for if a length opening tag is found

        for line in file:
            # This will occur the line after a name opening tag
            if nameTag:
                nameTag = False
                songs[-1]['name'] = line.strip()

            # This will occur the line after a length opening tag
            elif lengthTag:
                lengthTag = False
                songs[-1]['length'] = line.strip()

            # Check for an album opening tag
            elif '<Album' in line:
                # Add a new song entry to the list song.
                songs.append({})
                # Break the list a part at double quotes
                b = line.split('"')
                # The index 1 is used because the line that a new album
                # is created on contains something like artist="name">.
                # It is the content inside of the double quotes that needs
                # to be parsed out.
                songs[-1]['artist'] = b[1]

            # Check for an name opening tag
            elif '<Name' in line:
                # This will cause the most recent song entry's 'name' key to be
                # set to the value of the next line.
                nameTag = True

            # Check for an length opening tag
            elif '<Length' in line:
                # This will cause the most recent song entry's 'length' key to
                # be set to the value of the next line.
                lengthTag = True

        # Return the list of songs pulled from the file
        return songs

# Call main
main()
