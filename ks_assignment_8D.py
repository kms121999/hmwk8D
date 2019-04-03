#
#
#
#
#


'''

'''

RECORDS = "student_files8D/Records.xml" #??? is this right?

def main():
    #
    #
    #
    #

    pass


def loadFile():
    #
    #
    #
    #

    pass

def getSongs():
    #
    #
    #
    #
    #

    pass


#scratch

xml = '''<Discography>
	<Album Artist="Mark Ronson Featuring Bruno Mars">
		<Track>
			<Name>
				Uptown Funk!
			</Name>
			<Length>
				4:30
			</Length>
		</Track>
	</Album>
	<Album Artist="Mark Ronson Featuring Bruno Mars">
		<Track>
			<Name>
				Thinking Out Loud
			</Name>
			<Length>
				4:41
			</Length>
		</Track>
	</Album>






</Discography>'''


songs = []
count = 0
name = False
length = False

for line in xml.split('\n'):
    if '<Album' in line:
        songs.append({})
        b = line.split('"')
        songs[count]['artist'] = b[1]

    if name:
        name = False
        songs[count]['name'] = line.strip()

    if length:
        length = False
        songs[count]['length'] = line.strip()

    if '<Name' in line:
        name = True

    if '<Length' in line:
        length = True

    if '/Album' in line:
        count += 1
        
