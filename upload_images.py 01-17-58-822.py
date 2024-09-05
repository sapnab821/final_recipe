import cloudinary
import cloudinary.uploader
import os

# Configure Cloudinary with your credentials
cloudinary.config(
    cloud_name='dbitredaf',
    api_key='246954438558686',
    api_secret='HQnYJfjkpB7d0vkYrdsVA-6Yay8',
    secure=True
)

# Path to the directory containing images
image_directory = './media/recipes/'

# Upload all images from the specified directory while preserving their paths
for root, _, files in os.walk(image_directory):
    for filename in files:
        file_path = os.path.join(root, filename)
        
        # Compute the relative path of the file with respect to image_directory
        relative_path = os.path.relpath(file_path, image_directory)
        
        # Construct the Cloudinary public ID
        public_id = os.path.splitext(relative_path)[0].replace(os.sep, '/')
        
        print(f"Uploading {file_path} with public ID: {public_id}")
        
        # Upload the file to Cloudinary with the specified public ID
        try:
            response = cloudinary.uploader.upload(file_path, public_id=public_id)
            print(f"Upload successful: {response['url']}")
        except Exception as e:
            print(f"Error uploading {file_path}: {e}")
