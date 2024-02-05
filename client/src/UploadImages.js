import React, {useEffect, useState} from "react";

function UploadImages(){
    const [image, setImage] = useState(null);

    function onImageChage(e) {
        e.preventDefault();
        setImage(e.target.files[0]);
    }

    useEffect(() => {
        if (!image) return; // Do nothing if image is not selected
 
        const uploadImage = async () => {
            try {
                const formData = new FormData();
                formData.append('image', image);

                const response = await fetch('http://localhost:5000/upload', {
                    method: 'POST',
                    body: formData,
                });

                if (response.ok) {
                    console.log('Image uploaded successfully');
                } else {
                    console.error('Failed to upload image');
                }
            } catch (error) {
                console.error('Error uploading image:', error);
            }
        };

        uploadImage(); // Call the uploadImage function whenever the image changes
    }, [image]); // Dependency array with 'image'



    return (
        <form>
            <label htmlFor="imageUpload">Choose an image:</label>
            <input type = "file" accept = "image/*" onChange={onImageChage}/>
        </form>
    )
}


export default UploadImages;