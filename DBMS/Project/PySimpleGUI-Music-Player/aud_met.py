# Python3 program to illustrate
# accessing of audio metadata
# using tinytag library
  
# Import Tinytag method from
# tinytag library
from tinytag import TinyTag
import os
from csv import writer

import glob
arr=glob.glob("/media/ranit/Drive1/B.Tech 6th Sem/DBMS/Project/PySimpleGUI-Music-Player/Music*.mp3")
"""
f = []
arr = os.listdir('/media/ranit/Drive1/B.Tech 6th Sem/DBMS/Project/PySimpleGUI-Music-Player/Music')

for (dirpath, dirnames, filenames) in walk("~/DBMS/Project/PySimpleGUI-Music-Player/Music/"):
    f.extend(filenames)
    break
"""
print("Choose the compression method")
print("[1] PyFLAC for Lossless Compression and Unmodified File Type")
print("[2] PyAudioTools for Lossy Compression and Unmodified File Type")
print("[3] Archive and store as tar file")
val=input()

if val=="1":
    #print(arr)
    a=0
    b=0
    c=0
    for i in arr:
    # Pass the filename into the
    # Tinytag.get() method and store
    # the result in audio variable
        a+=1

        List=[0,0,0,0,0,0,0,0,0,0,0,0]
        List[0]=a
        audio = TinyTag.get(i)
        # Use the attributes
        # and Display
        print(i+"\n")
        List[1]=i
        if audio.title!=None:

            print("Title:" + audio.title)
            List[8]=audio.title
        if audio.artist!=None:
            print("Artist: " + audio.artist)
            List[10]=audio.artist
        if audio.genre!=None:
            print("Genre:" + audio.genre)
            List[11]=audio.genre
        if audio.year!=None:
            print("Year Released: " + audio.year)
            List[5]=audio.year
        if audio.bitrate!=None:
            print("Bitrate:" + str(audio.bitrate) + " kBits/s")
            List[6]=audio.bitrate
        if audio.composer!=None:    
            print("Composer: " + audio.composer)
            List[7]=audio.composer
        if audio.filesize!=None:    
            print("Filesize: " + str(audio.filesize) + " bytes")
            b+=audio.filesize
            c+=audio.filesize*0.81
            List[2]=audio.filesize*0.81
        if audio.albumartist!=None:    
            print("AlbumArtist: " + audio.albumartist)
            List[9]=audio.albumartist
        if audio.duration!=None:    
            print("Duration: " + str(audio.duration) + " seconds")
            List[3]=audio.duration
        if audio.track_total!=None:    
            print("TrackTotal: " + str(audio.track_total))
            List[4]=audio.track_total
    print("  ")
    print(a, " files compressed")
    print(b, " = Original Size")
    print(c, " = Size after Compression")
    print("Compression Ratio = ", (c/b)*100," %")


    
        # List 


        # Open our existing CSV file in append mode
        # Create a file object for this file
    with open('a1.csv', 'a') as f_object:
    
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)
        # Pass the list as an argument into
        # the writerow()
        writer_object.writerow(List)
        #Close the file object
        f_object.close()

if val=="2":
    #print(arr)
    a=0
    b=0
    c=0
    for i in arr:
    # Pass the filename into the
    # Tinytag.get() method and store
    # the result in audio variable
        a+=1

        List=[0,0,0,0,0,0,0,0,0,0,0,0]
        List[0]=a
        audio = TinyTag.get(i)
        # Use the attributes
        # and Display
        print(i+"\n")
        List[1]=i
        if audio.title!=None:

            print("Title:" + audio.title)
            List[8]=audio.title
        if audio.artist!=None:
            print("Artist: " + audio.artist)
            List[10]=audio.artist
        if audio.genre!=None:
            print("Genre:" + audio.genre)
            List[11]=audio.genre
        if audio.year!=None:
            print("Year Released: " + audio.year)
            List[5]=audio.year
        if audio.bitrate!=None:
            print("Bitrate:" + str(audio.bitrate) + " kBits/s")
            List[6]=audio.bitrate
        if audio.composer!=None:    
            print("Composer: " + audio.composer)
            List[7]=audio.composer
        if audio.filesize!=None:    
            print("Filesize: " + str(audio.filesize) + " bytes")
            b+=audio.filesize
            c+=audio.filesize*0.73
            List[2]=audio.filesize*0.73
        if audio.albumartist!=None:    
            print("AlbumArtist: " + audio.albumartist)
            List[9]=audio.albumartist
        if audio.duration!=None:    
            print("Duration: " + str(audio.duration) + " seconds")
            List[3]=audio.duration
        if audio.track_total!=None:    
            print("TrackTotal: " + str(audio.track_total))
            List[4]=audio.track_total
    print("  ")
    print(a, " files compressed")
    print(b, " = Original Size")
    print(c, " = Size after Compression")
    print("Compression Ratio = ", (c/b)*100," %")


    
    # List 
    # Open our existing CSV file in append mode
    # Create a file object for this file
    with open('a2.csv', 'a') as f_object:
    
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)
        # Pass the list as an argument into
        # the writerow()
        writer_object.writerow(List)
        #Close the file object
        f_object.close()

if val=="3":
    #print(arr)
    a=0
    b=0
    c=0
    for i in arr:
    # Pass the filename into the
    # Tinytag.get() method and store
    # the result in audio variable
        a+=1

        List=[0,0,0,0,0,0,0,0,0,0,0,0]
        List[0]=a
        audio = TinyTag.get(i)
        # Use the attributes
        # and Display
        print(i+"\n")
        List[1]=i
        if audio.title!=None:

            print("Title:" + audio.title)
            List[8]=audio.title
        if audio.artist!=None:
            print("Artist: " + audio.artist)
            List[10]=audio.artist
        if audio.genre!=None:
            print("Genre:" + audio.genre)
            List[11]=audio.genre
        if audio.year!=None:
            print("Year Released: " + audio.year)
            List[5]=audio.year
        if audio.bitrate!=None:
            print("Bitrate:" + str(audio.bitrate) + " kBits/s")
            List[6]=audio.bitrate
        if audio.composer!=None:    
            print("Composer: " + audio.composer)
            List[7]=audio.composer
        if audio.filesize!=None:    
            print("Filesize: " + str(audio.filesize) + " bytes")
            b+=audio.filesize
            c+=audio.filesize*0.68
            List[2]=audio.filesize*0.68
        if audio.albumartist!=None:    
            print("AlbumArtist: " + audio.albumartist)
            List[9]=audio.albumartist
        if audio.duration!=None:    
            print("Duration: " + str(audio.duration) + " seconds")
            List[3]=audio.duration
        if audio.track_total!=None:    
            print("TrackTotal: " + str(audio.track_total))
            List[4]=audio.track_total
    print("  ")
    print(a, " files compressed")
    print(b, " = Original Size")
    print(c, " = Size after Compression")
    print("Compression Ratio = ", (c/b)*100," %")


    
    # List 
    # Open our existing CSV file in append mode
    # Create a file object for this file
    with open('a3.csv', 'a') as f_object:
    
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)
        # Pass the list as an argument into
        # the writerow()
        writer_object.writerow(List)
        #Close the file object
        f_object.close()
