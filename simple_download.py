#simple script to download image files from internet

from sys import argv
import urllib2
import os.path

def simple_downloder(filename):
	num_of_success = 0
	with open(filename, 'rt') as input_file: # Iterate over the lines of the input file
		for line in input_file:
			url = line[:-1]  	#remove \n from the end of each line
			if not line.strip(): #ignore empty lines in input file
				print "\nEmpty line(s) in input file."
				continue
			elif not line.startswith("https://"): #ignore invalid url in input file
				print "\nInvalid url."
				continue
			elif not url.endswith(".jpg"): #ignore invalid file name in input file
				print "\nInvalid file name."
				continue
			elif urllib2.urlopen(url).getcode()!= 200 : #check if site is up
				print "\nWebsite is offline."
				continue								
				
			file_name = url.split('/')[-1]
			u = urllib2.urlopen(url)
			
			download_directory = 'C:\Users\Nahin PC\Downloads'  #change the directory according to your prefered location
			complete_path = os.path.join(download_directory, file_name)
			
			output_file = open(complete_path, 'wb')
			meta = u.info()
			file_size = int(meta.getheaders("Content-Length")[0])
			print "\nDownloading  %s ..." % (file_name)
			
			buffer = u.read(file_size)

			num_of_success+=1
			output_file.close()
				
		input_file.close()
	
	return num_of_success


