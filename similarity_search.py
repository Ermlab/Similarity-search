from IPython.display import Image, display
from IPython.core.display import HTML 

def display_images(images):
    imagesList=''.join(
    ["<div>\
         <img style='width:170px; float: left; border: 1px solid black;' src='%s'>\
         <h3 style='width:0px; position: relative; top:-25px; right:165px; float: left;'> %d </h3>\
     </div>" % (str(s), i) for i, s in enumerate(images)])
    display(HTML(imagesList))
    
def create_collection(vi_client, image_encoder, images, collection_name):
    vi_client.delete_collection(collection_name)
    
    documents = []
    for i, image in enumerate(images):
        documents.append({
            'image': image,
            'image_id' : str(i),
            '_id': i
        })

    vi_client.insert_documents(collection_name, documents, models={'image':image_encoder.encode})
    
def search_by_id(vi_client, collection_name, search_id):
    return vi_client.search_by_id(collection_name, str(search_id), 'image_vector_', page_size=10)
    
def search_by_ref(vi_client, collection_name,  ref_img_url):
    return vi_client.search_image(collection_name, ref_img_url, 'image_vector_', page_size=10)