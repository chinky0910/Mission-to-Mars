<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Mission to Mars</title>
    <link
      rel="stylesheet"
      href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"
    />
  </head>
  <body>
    <div class="container">
      <!-- Add Jumbotron to Header -->
      <div class="jumbotron text-center" style="background-color: #f3d6ca">
        <h1 style="color: #d16b3b">Mission to Mars</h1>
        <!-- Add a button to activate scraping script -->
        <p><a class="btn btn-danger btn-lg" href="/scrape" role="button">Scrape New Data</a></p>
      </div>

      <!-- Add section for Mars News -->
      <div class="row" id="mars-news">
        <div class="col-sm-12">
          <div class="media">
            <div class="media-body">
              <h2>Latest Mars News</h2>
              <h4 class="media-heading">{{ mars.news_title }}</h4>
              <p>{{ mars.news_paragraph }}</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Section for Featured Image and Facts table -->
      <div class="row" id="mars-featured-image">
        <div class="col-md-8">
          <h2>Featured Mars Image</h2>

          <!-- if images is False/None/non-existent, then default to error message -->
          <img
            src="{{mars.featured_image | default('static/images/error.png', true) }}"
            class="img-responsive"
            alt="Responsive image"
          />
        </div>

        <div class="col-md-4">
          <!-- Mars Facts -->
          <div class="row" id="mars-facts" >
            <h2>Mars Facts</h2>
             <table border="5"  style="background-color: #f3d6ca" class="dataframe table table-striped" 
             src="{{ mars.facts | safe }}"></table>
          </div>
        </div>
      </div>

      <!-- Section for Mars Hemispheres -->
      <div class="row" id="mars-hemispheres">
        <div class="page-header">
          <h2 class="text-center">Mars Hemispheres</h2>
        </div>

        {% for hemisphere in mars.hemispheres %}
        <div class="col-md-3">
          <div class="img-thumbnail">
            <img src="{{hemisphere.img_url | default('static/images/error.png', true)}}" alt="..." class="img-thumbnail">
            <div class="caption">
              <h3>{{hemisphere.title}}</h3>
            </div>
          </div>
        </div>
        {% endfor %}
      </div>
    </div>
  </body>
</html>
