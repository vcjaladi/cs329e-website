from flask import Flask # Import Flask package
from flask import render_template # Import render_template function
app = Flask(__name__) # Construct Flask object named 'app'

'''
@app.route() defines the URLs that route to the index() function.
The URLs will be appended to the end of the base URL.
Links within HTML files should use the defined routes (for example '/index') as
the values for href attributes.
URLs that will call the index() function if running app.py on localhost:
	http://localhost:5000/
	http://localhost:5000/index
'''
@app.route('/') # URL for function (default for home page)
@app.route('/index') # Secondary URL for function
def index():
	return render_template('index.html') # located in templates/
	
@app.route('/about')
def about():
	return render_template('about.html')

# Artist Page Routes	
@app.route('/artists')
def artists():
	return render_template('artists.html')

@app.route('/artist-Anderson_Paak')
def artist_anderson_paak():
	return render_template('artist-Anderson_Paak.html')

@app.route('/artist-Coldplay')
def artist_coldplay():
	return render_template('artist-Coldplay.html')

@app.route('/artist-Denzel_Curry')
def artist_denzel_curry():
	return render_template('artist-Denzel_Curry.html')

@app.route('/artist-Kendrick_Lamar')
def artist_kendrick_lamar():
	return render_template('artist-Kendrick_Lamar.html')

@app.route('/artist-Metallica')
def artist_metallica():
	return render_template('artist-Metallica.html')

@app.route('/artist-Radiohead')
def artist_radiohead():
	return render_template('artist-Radiohead.html')


# Set Page Routes
@app.route('/sets')
def sets():
	return render_template('sets.html')

@app.route('/set-Anderson_Staples_2017')
def anderson_staples():
	return render_template('set-Anderson_Staples_2017.html')

@app.route('/set-Coldplay_ACL_2011')
def coldplay_acl():
	return render_template('set-Coldplay_ACL_2011.html')

@app.route('/set-Coldplay_Glastonbury_2016')
def coldplay_glastonbury():
	return render_template('set-Coldplay_Glastonbury_2016.html')

@app.route('/set-Coldplay_Rock_in_Rio_2011')
def coldplay_rio():
	return render_template('set-Coldplay_Rock_in_Rio_2011.html')

@app.route('/set-Coldplay_T_in_the_Park_2011')
def coldplay_t():
	return render_template('set-Coldplay_T_in_the_Park_2011.html')

@app.route('/set-Denzel_Stubbs_2017')
def denzel_stubbs():
	return render_template('set-Denzel_Stubbs_2017.html')

@app.route('/set-Kendrick_ACL_2016')
def kendrick_acl():
	return render_template('set-Kendrick_ACL_2016.html')

@app.route('/set-Metallica_Rock_in_Rio_2015')
def metallica_rio():
	return render_template('set-Metallica_Rock_in_Rio_2015.html')

@app.route('/set-Radiohead_ACL_2016')
def radiohead_acl():
	return render_template('set-Radiohead_ACL_2016.html')

@app.route('/set-Radiohead_MSG_2016')
def radiohead_msg():
	return render_template('set-Radiohead_MSG_2016.html')

@app.route('/set-Radiohead_Worth_Farm_2011')
def radiohead_worth():
	return render_template('set-Radiohead_Worth_Farm_2011.html')


# Venue Page Routes
@app.route('/venues')
def venues():
	return render_template('venues.html')

@app.route('/venue-acl')
def venue_acl():
	return render_template('venue-acl.html')

@app.route('/venue-glastonbury')
def venue_glastonbury():
	return render_template('venue-glastonbury.html')

@app.route('/venue-msg')
def venue_msg():
	return render_template('venue-msg.html')

@app.route('/venue-rockinrio')
def venue_rio():
	return render_template('venue-rockinrio.html')

@app.route('/venue-staples')
def venue_staples():
	return render_template('venue-staples.html')

@app.route('/venue-stubbs')
def venue_stubbs():
	return render_template('venue-stubbs.html')

@app.route('/venue-tinthepark')
def venue_t():
	return render_template('venue-tinthepark.html')

# Run application
if __name__ == '__main__':
        app.run('107.170.32.219', '80')  # Run application

