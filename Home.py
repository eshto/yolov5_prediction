import streamlit as st

st.set_page_config(page_title="Home",
                   layout='wide',
                   page_icon='./images/home.png')

st.title('YOLOV5 Object Detection app')
st.caption('This web application demostrates My object detection project')

# Content

st.markdown("""
### This app detects objects from images
- Automatically detectsa 20 objects from an image
- [Click here to try it](/yolo_for_image/)
            
These are the objects the Model will predict
1. person
2. car
3. chair
4. bottle
5. potted-plant
6. bird
7. dog
8. sofa
9. bicycle
10. horse
11. boat
12. motorbike
13. cat
14. tv-monitor
15. cow
16. sheep
17. aeroplane
18. train
19. dining-table
20. bus
""")