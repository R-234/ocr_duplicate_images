# import streamlit as st
# from PIL import Image
# import zipfile
# import os
# import io

# # Streamlit UI
# st.title("🖼️ Custom Image Copy Generator")
# st.write("Rename your image and create numbered copies!")

# # 1. File Uploader
# uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# if uploaded_file:
#     # 2. Rename Image (User Input)
#     default_name = os.path.splitext(uploaded_file.name)[0]  # Original filename (without extension)
#     custom_name = st.text_input(
#         "Rename your image (without extension)", 
#         value=default_name,
#         help="This will be the base name for all copies."
#     )

#     # 3. Number of Copies Input
#     num_copies = st.number_input(
#         "Number of copies", 
#         min_value=1, 
#         max_value=100, 
#         value=5,
#         help="How many copies do you want?"
#     )

#     # 4. Process and Download
#     if st.button("Generate Copies"):
#         if not custom_name:
#             st.error("Please enter a name for your image!")
#         else:
#             # Read the image
#             img = Image.open(uploaded_file)
#             extension = os.path.splitext(uploaded_file.name)[1].lower()

#             # Create ZIP in memory
#             zip_buffer = io.BytesIO()
#             with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
#                 # Save original (renamed) image
#                 img_bytes = io.BytesIO()
#                 img.save(img_bytes, format=img.format)
#                 zip_file.writestr(f"{custom_name}_original{extension}", img_bytes.getvalue())

#                 # Save copies (e.g., CustomName_1.jpg, CustomName_2.jpg)
#                 for i in range(1, num_copies + 1):
#                     img_bytes = io.BytesIO()
#                     img.save(img_bytes, format=img.format)
#                     zip_file.writestr(f"{custom_name}_{i}{extension}", img_bytes.getvalue())

#             # Download ZIP
#             st.success("✅ Copies generated!")
#             st.download_button(
#                 label="Download ZIP",
#                 data=zip_buffer.getvalue(),
#                 file_name=f"{custom_name}_copies.zip",
#                 mime="application/zip"
#             )

#             # Preview
#             st.image(img, caption=f"Preview: {custom_name}_original{extension}", width=300)



































import streamlit as st
from PIL import Image
import zipfile
import os
import io

# Streamlit UI
st.title("➕ Multiple Image Copy For Rishav")
st.write("This App will Devlope by Rakesh Rathaur!")
st.write("Rename your image with a number, and copies.")

# 1. File Uploader
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # 2. Rename Image (User Input)
    default_name = os.path.splitext(uploaded_file.name)[0]
    custom_name = st.text_input(
        "Rename your image (must start with a number, e.g., '14')", 
        value=default_name,
        help="Copies will increment from this number. Example: 14 → 14.jpg, 15.jpg, etc."
    )

    # 3. Number of Copies Input
    num_copies = st.number_input(
        "Number of copies", 
        min_value=1, 
        max_value=30, 
        value=5
    )

    # 4. Process and Download
    if st.button("Generate Copies"):
        if not custom_name:
            st.error("Please enter a name!")
        else:
            # Extract the base number (e.g., "14" from "14.jpg")
            try:
                base_number = int(''.join(filter(str.isdigit, custom_name)))
            except:
                st.error("⚠️ Name must contain a number (e.g., '14' or 'img2')!")
                st.stop()

            extension = os.path.splitext(uploaded_file.name)[1].lower()
            img = Image.open(uploaded_file)

            # Create ZIP in memory
            zip_buffer = io.BytesIO()
            with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                for i in range(num_copies):
                    # Increment the number (14 → 14, 15, ..., 18)
                    new_name = f"{base_number + i}{extension}"
                    img_bytes = io.BytesIO()
                    img.save(img_bytes, format=img.format)
                    zip_file.writestr(new_name, img_bytes.getvalue())

            # Download ZIP
            st.success(f"✅ Generated {num_copies} copies: {base_number}.jpg to {base_number + num_copies - 1}.jpg")
            st.download_button(
                label="Download ZIP",
                data=zip_buffer.getvalue(),
                file_name="image_copies.zip",
                mime="application/zip"
            )

            # Preview first image
            st.image(img, caption=f"First copy: {base_number}.jpg", width=300)
