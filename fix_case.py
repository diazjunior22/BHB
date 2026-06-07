import os

file_path = 'src/pages/TourDetail.jsx'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Party Boat
content = content.replace('../assets/bhb/Party Boat/1.jpg', '../assets/bhb/Party boat/1.jpg')
content = content.replace('../assets/bhb/Party Boat/2.jpg', '../assets/bhb/Party boat/2.jpg')
content = content.replace('../assets/bhb/Party Boat/3.jpg', '../assets/bhb/Party boat/3.jpg')
content = content.replace('../assets/bhb/Party Boat/4.jpg', '../assets/bhb/Party boat/4.jpg')
content = content.replace('../assets/bhb/Party Boat/5.jpg', '../assets/bhb/Party boat/5.jpg')

# Fix el dorado park
content = content.replace('../assets/bhb/el dorado park/1.jpeg', '../assets/bhb/El Dorado Park/1.jpeg')
content = content.replace('../assets/bhb/el dorado park/2.jpeg', '../assets/bhb/El Dorado Park/2.jpeg')
content = content.replace('../assets/bhb/el dorado park/3.jpeg', '../assets/bhb/El Dorado Park/3.jpeg')
content = content.replace('../assets/bhb/el dorado park/4.jpeg', '../assets/bhb/El Dorado Park/4.jpeg')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed case sensitivity issues in TourDetail.jsx")
