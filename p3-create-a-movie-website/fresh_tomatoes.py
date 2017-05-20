# Intro to Programming Nanodegree
# Project 3 - Create a Movie Website
# Ricardo Yoshitomi

import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            background-color: #F5F5F0;
            margin-bottom: 10px;
            padding-top: 20px;
            padding-bottom: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        .movie-info {
            background-color: #F5F5F0;
            margin-bottom: 10px;
            padding-top: 20px;
            padding-bottom: 20px;
            height: 382px;
        }
        h3 {
            margin: 0;
            color: #3399ff;
        }
        h5 {
            margin-top: 5px;
            color: #3399ff;
        }
        .people {
            padding-left: 0;
            list-style:none;
        }
        .extra-info {
            background-color: #F5F5F0;
            padding-left: 15px;
            border-left: 1px solid #E1E1D0;
            list-style:none;
        }
        li {
            margin-bottom: 5px;
        }
        strong {
            color: #6f6f6f;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Ricardo's Favorite Movies</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content1 = '''
<div class="col-md-3 col-lg-3 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
</div>
<div class="col-md-6 col-lg-6 movie-info text-left">
    <h3>{movie_title} ({release_year})</h3>
    <h5>{movie_genre}</h5>
    <p>{brief_description}</p>
    <ul class="people">
        <li><strong>Director: </strong>{directed_by}</li>
        <li><strong>Writers: </strong>{movie_writers}</li>
        <li><strong>Stars: </strong>{starring}</li>
    </ul>
</div>
<div class="col-md-3 col-lg-3 movie-info text-left">
    <ul class="extra-info">
        <li><strong>Release Date: </strong>{release_date}</li>
        <li><strong>Duration: </strong>{running_time}</li>
        <li><strong>Country: </strong>{movie_country}</li>
        <li><strong>Language: </strong>{movie_language}</li>
</div>
'''

movie_tile_content2 = '''
<div class="col-md-6 col-lg-6 movie-info text-left">
    <h3>{movie_title} ({release_year})</h3>
    <h5>{movie_genre}</h5>
    <p>{brief_description}</p>
    <ul class="people">
        <li><strong>Director: </strong>{directed_by}</li>
        <li><strong>Writers: </strong>{movie_writers}</li>
        <li><strong>Stars: </strong>{starring}</li>
    </ul>
</div>
<div class="col-md-3 col-lg-3 movie-info text-left">
    <ul class="extra-info">
        <li><strong>Release Date: </strong>{release_date}</li>
        <li><strong>Duration: </strong>{running_time}</li>
        <li><strong>Country: </strong>{movie_country}</li>
        <li><strong>Language: </strong>{movie_language}</li>
</div>
<div class="col-md-3 col-lg-3 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    count = 1
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)
        # Alternate the position of the boxes on the page
        count += 1
        if count%2 == 0:
            movie_tile_content = movie_tile_content1
        else:
            movie_tile_content = movie_tile_content2
        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            brief_description=movie.description,
            directed_by=movie.director,
            movie_writers=movie.writers,
            starring=movie.stars,
            release_year=movie.year,
            movie_genre=movie.genre,
            running_time=movie.duration,
            movie_country=movie.country,
            movie_language=movie.language,
            release_date=movie.date
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
