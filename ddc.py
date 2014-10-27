import webbrowser
import os
import ddc_dogs

# the main page layout
main_page_content = '''
<!DOCTYPE html>
<head>
<link rel ="stylesheet" type="text/css" href="/Users/Steffany/Documents/ddc.css"/>
<title>Doggie Day Care</title>
<html lang="en">
<body style="background-color: lightblue;">
	<h1 align="center" style="font-family: cursive; font-size: 75px;">Doggie Day Care
	<img src="http://thumbs.dreamstime.com/z/dog-shy-terrier-silhouette-logo-pupphy-32916978.jpg" hieght="100" width="100" style="padding-top:15px"/>
	</h1>
	<h2 align="center">Current Breeds at Doggie Day Care</h2>
	<div class="content">
		{dog_tiles}
	</div>

</body>
</html>
</head>
'''

# a single dog_tile
dog_tiles_content = '''
	<div class="photos">
		<a href="{link}">
			<ul>
				<li>
				<span><img src="{dog_breed_image}"/></span>
				<span><h4>{dog_breed}</h4></span>
				<h6>Breed size: {dog_breed_size}</h6>
				</li>
			</ul>
		</a>
	</div>
'''


#creating the content dog_tiles will really have
def create_dog_tiles(breeds):
	content = ""
	# gets the current working directory to use in link
	path = os.getcwd()
	for breed in breeds:
		content += dog_tiles_content.format(
			#creats the file to use for the a href to make the image and breed clickable
			link = "file://{path}/{breed_name}.html".format(path = path, breed_name = breed.dog_name),
			#inputs image of that breed
			dog_breed_image = breed.dog_image,
			#inputs name of the breed
			dog_breed = breed.dog_name,
			#inputs the size of the breed
			dog_breed_size = breed.breed_size
		)
	return content


#create or overwrite output file
def open_ddc_page(breed_list, dog_list):
	ddc_dogs.create_breed_pages(dog_list)
	output_file = open("doggie_day_care.html", "w+")

	#replace dog_tiles with actual content
	true_content = main_page_content.format(dog_tiles=create_dog_tiles(breed_list))
	output_file.write(true_content)
	output_file.close()

	#open the output file in the browser
	url = os.path.abspath(output_file.name)
	webbrowser.open("file://" + url, new=1)








