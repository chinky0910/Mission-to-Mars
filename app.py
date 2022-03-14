{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4f78a47e",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Import Dependencies\n",
    "from flask import Flask, render_template\n",
    "from flask_pymongo import PyMongo\n",
    "import scraping\n",
    "\n",
    "#Set up Flask\n",
    "app = Flask(__name__)\n",
    "\n",
    "#Connect to Mongo using PyMongo\n",
    "# Use flask_pymongo to set up mongo connection\n",
    "app.config[\"MONGO_URI\"] = \"mongodb://localhost:27017/mars_app\"\n",
    "mongo = PyMongo(app)\n",
    "\n",
    "#Define the route for the HTML page\n",
    "@app.route(\"/\")\n",
    "def index():\n",
    "   mars = mongo.db.mars.find_one()\n",
    "   return render_template(\"index.html\", mars=mars)\n",
    "\n",
    "#Add next route and function to our code\n",
    "@app.route(\"/scrape\")\n",
    "def scrape():\n",
    "   mars = mongo.db.mars\n",
    "   mars_data = scraping.scrape_all()\n",
    "   mars.update({}, mars_data, upsert=True)\n",
    "   return \"Scraping Successful!\"\n",
    "\n",
    "#Run the code\n",
    "if __name__ == \"__main__\":\n",
    "   app.run()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
