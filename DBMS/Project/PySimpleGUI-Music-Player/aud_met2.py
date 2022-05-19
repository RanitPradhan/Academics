import pandas as pd
music_det = {
		'Title' : ['1','2','3','4','5'],	
		'Artist': ['1','2','3','4','5'],
		'Genre' : ['1','2','3','4','5'],
		'Year Released' : ['1','2','3','4','5'],
		'Bitrate' : ['1','2','3','4','5'],
		'Composer' : ['1','2','3','4','5'],
		'Filesize' : ['1','2','3','4','5'],
		'AlbumArtist' : ['1','2','3','4','5'],
		'Duration' : ['1','2','3','4','5'],
		'TrackTotal' : ['1','2','3','4','5']
	}  
df = pd.DataFrame(music_det)

print (df)
df.to_csv('album_data.csv',na_rep='Unkown')