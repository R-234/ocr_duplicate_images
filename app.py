# import streamlit as st
# from PIL import Image, ImageOps
# import zipfile
# import os
# import io
# from PyPDF2 import PdfReader, PdfWriter

# # Streamlit UI
# st.title("➕ Multiple Image Copy For Rishav")
# st.write("This App Developed by Rakesh Rathaur!")
# st.write("Rename your file with a number, and create copies.")

# # 1. File Uploader
# uploaded_file = st.file_uploader("Upload a file", type=["jpg", "jpeg", "png", "pdf"])

# if uploaded_file:
#     # 2. Rename File (User Input)
#     default_name = os.path.splitext(uploaded_file.name)[0]
#     custom_name = st.text_input(
#         "Rename your file (must start with a number, e.g., '14')", 
#         value=default_name,
#         help="Copies will increment from this number. Example: 14 → 14.jpg, 15.jpg, etc."
#     )

#     # 3. Number of Copies Input
#     num_copies = st.number_input(
#         "Number of copies", 
#         min_value=1, 
#         max_value=30, 
#         value=5
#     )

#     # 4. Process and Download
#     if st.button("Generate Copies"):
#         if not custom_name:
#             st.error("Please enter a name!")
#         else:
#             try:
#                 base_number = int(''.join(filter(str.isdigit, custom_name)))
#             except:
#                 st.error("⚠️ Name must contain a number (e.g., '14' or 'img2')!")
#                 st.stop()

#             extension = os.path.splitext(uploaded_file.name)[1].lower()
            
#             # Create ZIP in memory
#             zip_buffer = io.BytesIO()
            
#             if extension in ['.jpg', '.jpeg', '.png']:
#                 # Handle image files
#                 img_bytes = uploaded_file.read()
#                 img = Image.open(io.BytesIO(img_bytes))
#                 img = ImageOps.exif_transpose(img)
                
#                 with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
#                     for i in range(num_copies):
#                         new_name = f"{base_number + i}{extension}"
#                         img_bytes = io.BytesIO()
#                         if img.format == 'PNG':
#                             img.save(img_bytes, format='PNG')
#                         else:
#                             img.save(img_bytes, format='JPEG', quality=95)
#                         zip_file.writestr(new_name, img_bytes.getvalue())
                
#                 # Preview first image
#                 st.image(img, caption=f"First copy: {base_number}{extension}", width=700)
                
#             elif extension == '.pdf':
#                 # Handle PDF files
#                 pdf_reader = PdfReader(uploaded_file)
#                 pdf_writer = PdfWriter()
                
#                 # Copy all pages from original PDF
#                 for page in pdf_reader.pages:
#                     pdf_writer.add_page(page)
                
#                 with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
#                     for i in range(num_copies):
#                         new_name = f"{base_number + i}{extension}"
#                         pdf_bytes = io.BytesIO()
#                         pdf_writer.write(pdf_bytes)
#                         zip_file.writestr(new_name, pdf_bytes.getvalue())
                
#                 st.write("PDF file processed. No preview available for PDF files.")
            
#             else:
#                 st.error("Unsupported file format!")
#                 st.stop()

#             # Download ZIP
#             st.success(f"✅ Generated {num_copies} copies: {base_number}{extension} to {base_number + num_copies - 1}{extension}")
#             st.download_button(
#                 label="Download ZIP",
#                 data=zip_buffer.getvalue(),
#                 file_name="file_copies.zip",
#                 mime="application/zip"
#             )



# import streamlit as st
# from PIL import Image, ImageOps
# import zipfile
# import os
# import io
# from PyPDF2 import PdfReader, PdfWriter

# # Configure page with centered layout
# st.set_page_config(
#     page_title="🖼️ Image Copies Processor",
#     page_icon="✨",
#     layout="centered",
#     initial_sidebar_state="collapsed"
# )

# # Streamlit UI
# st.title("➕ Multiple File Copy Generator")
# st.write("Developed by Rakesh Rathaur")
# # st.write("Upload images/PDFs to create numbered copies.")

# # File Uploader
# uploaded_file = st.file_uploader("Upload a file", type=["jpg", "jpeg", "png", "pdf"])

# if uploaded_file:
#     # Rename File
#     default_name = os.path.splitext(uploaded_file.name)[0]
#     custom_name = st.text_input(
#         "Rename your file (must contain a number)", 
#         value=default_name
#     )

#     # Number of Copies
#     num_copies = st.number_input("Number of copies", min_value=1, max_value=30, value=5)

#     # Manual Rotation Option (Only for Images)
#     rotation_angle = 0
#     if uploaded_file.type.startswith('image'):
#         st.subheader("🔄 Image Rotation Settings")
#         rotation_angle = st.selectbox(
#             "Manually rotate image (if auto-rotation fails)",
#             options=[0, 90, 180, 270],
#             index=0,
#             help="Select rotation angle if image appears sideways"
#         )

#     if st.button("Generate Copies"):
#         if not custom_name:
#             st.error("Please enter a name!")
#         else:
#             try:
#                 base_number = int(''.join(filter(str.isdigit, custom_name)))
#             except:
#                 st.error("Name must contain a number (e.g., '14' or 'file2')!")
#                 st.stop()

#             extension = os.path.splitext(uploaded_file.name)[1].lower()
#             zip_buffer = io.BytesIO()

#             if extension in ['.jpg', '.jpeg', '.png']:
#                 # Process Image
#                 img = Image.open(uploaded_file)
#                 img = ImageOps.exif_transpose(img)  # Auto-rotation
                
#                 # Apply Manual Rotation if selected
#                 if rotation_angle != 0:
#                     img = img.rotate(rotation_angle, expand=True)
                
#                 with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
#                     for i in range(num_copies):
#                         new_name = f"{base_number + i}{extension}"
#                         img_bytes = io.BytesIO()
                        
#                         # Explicitly set format based on extension
#                         if extension == '.png':
#                             img.save(img_bytes, format='PNG')
#                         else:
#                             img.save(img_bytes, format='JPEG', quality=95)
                            
#                         zip_file.writestr(new_name, img_bytes.getvalue())
                
#                 # Show Preview
#                 st.image(img, caption=f"Preview: {base_number}{extension}")

#             elif extension == '.pdf':
#                 # Process PDF
#                 pdf_reader = PdfReader(uploaded_file)
#                 pdf_writer = PdfWriter()
#                 for page in pdf_reader.pages:
#                     pdf_writer.add_page(page)
                
#                 with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
#                     for i in range(num_copies):
#                         new_name = f"{base_number + i}.pdf"
#                         pdf_bytes = io.BytesIO()
#                         pdf_writer.write(pdf_bytes)
#                         zip_file.writestr(new_name, pdf_bytes.getvalue())
                
#                 st.info("PDF copies created (no rotation for PDFs)")

#             # Download ZIP
#             st.success(f"Created {num_copies} copies from {base_number} to {base_number+num_copies-1}")
#             st.download_button(
#                 label="Download ZIP",
#                 data=zip_buffer.getvalue(),
#                 file_name="copies.zip",
#                 mime="application/zip"
#             )











































import streamlit as st
from PIL import Image, ImageOps
import zipfile
import os
import io
from PyPDF2 import PdfReader, PdfWriter

# Configure page with centered layout
st.set_page_config(
    page_title="🖼️ Image Copies Processor",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Streamlit UI
st.title("➕ Multiple File Copy Generator")
st.write("Developed by Rakesh Rathaur")

# File Uploader
uploaded_file = st.file_uploader("Upload a file", type=["jpg", "jpeg", "png", "pdf"])

if uploaded_file:
    # Rename File
    default_name = os.path.splitext(uploaded_file.name)[0]
    custom_name = st.text_input(
        "Rename your file (must contain a number)", 
        value=default_name
    )

    # Number of Copies
    num_copies = st.number_input("Number of copies", min_value=1, max_value=30, value=5)

    # Manual Rotation Option (Only for Images)
    rotation_angle = 0
    if uploaded_file.type.startswith('image'):
        st.subheader("🔄 Image Rotation Settings")
        rotation_angle = st.selectbox(
            "Manually rotate image (if auto-rotation fails)",
            options=[0, 90, 180, 270],
            index=0,
            help="Select rotation angle if image appears sideways"
        )

        # ✅ New Feature: Choose Output Image Format
        st.subheader("🖼️ Choose Output Image Format")
        output_format = st.selectbox(
            "Select image format for download",
            options=["jpg", "jpeg", "png"],
            index=0
        )

    if st.button("Generate Copies"):
        if not custom_name:
            st.error("Please enter a name!")
        else:
            try:
                base_number = int(''.join(filter(str.isdigit, custom_name)))
            except:
                st.error("Name must contain a number (e.g., '14' or 'file2')!")
                st.stop()

            extension = os.path.splitext(uploaded_file.name)[1].lower()
            zip_buffer = io.BytesIO()

            if extension in ['.jpg', '.jpeg', '.png']:
                # Process Image
                img = Image.open(uploaded_file)
                img = ImageOps.exif_transpose(img)  # Auto-rotation
                
                # Apply Manual Rotation if selected
                if rotation_angle != 0:
                    img = img.rotate(rotation_angle, expand=True)
                
                with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
                    for i in range(num_copies):
                        new_ext = "." + output_format.lower()  # user-selected format
                        new_name = f"{base_number + i}{new_ext}"
                        img_bytes = io.BytesIO()
                        
                        # Save in chosen format
                        if output_format.lower() == 'png':
                            img.save(img_bytes, format='PNG')
                        else:
                            img.save(img_bytes, format='JPEG', quality=95)
                            
                        zip_file.writestr(new_name, img_bytes.getvalue())
                
                # Show Preview
                st.image(img, caption=f"Preview: {base_number}.{output_format}")

            elif extension == '.pdf':
                # Process PDF
                pdf_reader = PdfReader(uploaded_file)
                pdf_writer = PdfWriter()
                for page in pdf_reader.pages:
                    pdf_writer.add_page(page)
                
                with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
                    for i in range(num_copies):
                        new_name = f"{base_number + i}.pdf"
                        pdf_bytes = io.BytesIO()
                        pdf_writer.write(pdf_bytes)
                        zip_file.writestr(new_name, pdf_bytes.getvalue())
                
                st.info("PDF copies created (no rotation for PDFs)")

            # Download ZIP
            st.success(f"Created {num_copies} copies from {base_number} to {base_number+num_copies-1}")
            st.download_button(
                label="Download ZIP",
                data=zip_buffer.getvalue(),
                file_name="copies.zip",
                mime="application/zip"
            )
