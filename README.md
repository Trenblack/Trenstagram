# Trenstagram
API to edit profile data on your Instagram account using Python.

# Features
- Edit your instagram profile data
	- Profile picture
	- Username
	- Name
	- Bio
	- External website
- Scrape data from other profiles
	- Profile Picture
	- Bio
	- *more coming soon*

# How to use
1. Clone this repo.
2. Install requirements.
`pip3 install requirements.txt`
3. Import Trenstagram
`from ig import Trenstagram`
4. Create instance of Trenstagram.
`api = Trenstagram()`
6. Login
`api.login(USERNAME, PASSWORD, EMAIL)`
7. You can now use api to edit information.
`api.change_bio("hello word!")`

