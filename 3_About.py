import streamlit as st
from PIL import Image

st.set_page_config(page_title="YOLO Object Detection",
                   layout='wide',
                   page_icon='./images/roundend-logo.png')


# Title and Description
st.title("YOLO Image Prediction Model")
st.write("Welcome to the About Page of my YOLO Image Prediction Model.")


# Introduction and Explanation
st.write(
    """
    My YOLO (You Only Look Once) image prediction model is a state-of-the-art deep learning algorithm 
    trained to recognize 20 different objects in images. The model has been meticulously trained on a 
    vast dataset, enabling it to accurately identify and locate various objects within an image. Some 
    of the objects My model can recognize include:
    1. Person
    2. Car
    3. Chair
    4. Bottle
    5. Potted Plant
    6. Bird
    7. Dog
    8. Sofa
    9. Bicycle
    10. Horse
    11. Boat
    12. Motorbike
    13. Cat
    14. TV Monitor
    15. Cow
    16. Sheep
    17. Aeroplane
    18. Train
    19. Dining Table
    20. Bus

    Our YOLO model's efficient architecture allows it to process images in real-time, making it suitable 
    for various applications such as object detection, surveillance, and image analysis. Feel free to 
    explore its capabilities by uploading your own images and witnessing the accurate predictions.
    """
)

# How to Use the Model
st.header("How to Use the Model")
st.write(
    """
   Using my YOLO image prediction model is simple and intuitive. Follow these steps to get started:
      
    1. **Click the Get Detection Button:**
       After uploading your image, click the "Get Detection" button to initiate the object detection process.
       Our YOLO model will analyze the image and identify the objects present in it.
       
    2. **View the Predictions:**
       Once the detection is complete, the model's predictions will be displayed on the image. Each detected 
       object will be outlined, and its label will be shown. You can explore the predictions and observe the 
       accuracy of the model.
       
    3. **Try Different Images:**
       Feel free to try different images to see how our YOLO model performs across various scenarios. Upload 
       images with different objects and backgrounds to witness the model's versatility.
       
    Please note that the accuracy of the predictions may vary based on the quality and complexity of the 
    uploaded image. Enjoy exploring our YOLO image prediction model!
    """
)

# About You or Your Team
st.header("About Me")
st.write(
    """
    Hi there! 👋 My name is Eshton Hinkle and I'm passionate about technology and design. I work as a web designer 
    and Help Desk technician, where I blend creativity with technical expertise to create seamless and 
    user-friendly digital experiences. While I've spent my professional life in the world of web design and IT 
    support, this project marks my exciting foray into the realm of computer vision.

    **My Computer Vision Journey:**
    
    This YOLO image prediction model represents my first venture into the fascinating field of computer vision. 
    I'm thrilled to explore the power of algorithms and deep learning in recognizing and interpreting visual 
    data. With each line of code, I am learning and growing, eager to enhance my skills and contribute meaningfully 
    to the world of artificial intelligence.

    **Why Computer Vision?**
    
    Computer vision captivates me because of its ability to bridge the gap between the digital world and our 
    physical surroundings. The potential applications are limitless, from improving security systems to enhancing 
    healthcare diagnostics. I am excited to delve deeper, learn more, and leverage this knowledge to create 
    innovative solutions.
    
    Thank you for being a part of my journey!
    """
)

# Contact Information
st.header("Contact Me")
st.write(
    """
     If you have any questions, suggestions, or just want to connect, feel free to reach out to me. I'm here to help!
    
    **Email:** [eshton.hinkle@gmail.com](mailto:eshton.hinkle@gmail.com)
    
    **LinkedIn:** [Eshton Hinkle](https://www.linkedin.com/in/eshton-hinkle/)
    
    Let's collaborate and explore the exciting world of computer vision together!
    """
)

# Footer
st.write(
    """
    Thank you for visiting my About Page! Feel free to explore the rest of the application and try out 
    the YOLO image prediction model.
    """
)
