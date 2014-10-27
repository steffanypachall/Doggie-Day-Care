import webbrowser
import os

#main page layout
main_page_content= '''
<!DOCTYPE html>
<head>
<link rel ="stylesheet" type="text/css" href="/Users/Steffany/Documents/ddc.css"</link>
<title>Dogs at Doggie Day Care</title>
<html lang="en">
<body style="background-color: lightblue;">
	<h1 align="center" style="font-family: cursive;" font-size="75px" >{breed} at Doggie Day Care</h1>
	<div class="content">
		{dog_tiles}
	</div>
</body>
</html>
</head>
'''

#a single dog tile 
dog_tiles_content= '''
<div class="dog-details">
		<img src="{dog_image}"/>
		<div class="info">
			<strong>Name:</strong> {dog_name}<br>
			<strong>Age:</strong> {age}<br>
			<strong>Sex:</strong> {sex}<br>
			<strong>Additional Info:</strong> {additional_info}
		</div>			
	</div>
'''
#creating the dog tile info it will really have
def create_dog_tiles(dogs):
	content=""
	for dog in dogs:
		content += dog_tiles_content.format(
			#inputs the dog image
			dog_image = dog.dog_image,
			#inputs the dog name
			dog_name = dog.dog_name,
			#inputs the dogs age
			age = dog.age,
			#inputs the dogs gender
			sex = dog.sex,
			#inputs additional info about the dog
			additional_info = dog.additional_info
			)
	return content


#create or overwrite output file
def create_breed_pages(dog_list):
	for key, value in dog_list.iteritems():
		#opens and creates a new file for to use for the dogs in each breed
		output_file = open("{new_page}.html".format(new_page = key), "w+")

		#replace dog_tiles with actual content
		true_content = main_page_content.format(breed= key, dog_tiles=create_dog_tiles(value))
		output_file.write(true_content)
		output_file.close()
