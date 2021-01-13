# Similarity-search
Playground for image similarity search using vector-ai.

# Requirements
To use this repository you will need to install vector-ai via pip and request the api key by calling
```
from vectorai import ViClient, request_api_key

api_key = request_api_key(username=<username>, email=<email>, description=<description>, referral_code="github_referred")
```
# Usage
First log in to the api using the login details for vector-ai
```
from vectorai import ViClient
from vectorai.models.deployed import ViImage2Vec

vi_client = ViClient(username, api_key, url)
image_encoder = ViImage2Vec(username, api_key, url)
```
Create a collection of images to be used for similarity search. The images must be uploaded to the network and given as urls. Create a collection from the list of urls.
```
import similarity_search
similarity_search.create_collection(vi_client, image_encoder, collection, collection_name)
```
Use the created collection to search for similar images to an image in the collection with the given id or to a reference image with the given url.
```
#By id
search_by_id_results = similarity_search.search_by_id(vi_client, collection_name, search_id)
vi_client.show_json(search_by_id_results, image_fields=['image'], image_width=150, nrows=10)

#By reference
search_results = similarity_search.search_by_ref(vi_client, collection_name, ref_img_url)
vi_client.show_json(search_results, image_fields=['image'], image_width=150, nrows=10)
```
To select a picture from the collection by id you can browse the pictures from the list of urls and their ids.
```
similarity_search.display_images(list_of_img_urls)
```