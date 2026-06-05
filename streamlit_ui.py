import streamlit as st
from pathlib import Path
import os
import shutil

st.set_page_config(page_title="File Manager", page_icon="📂", layout="centered")

st.title("📂 File & Folder Manager")

# -----------------------------
# Function to show files/folders
# -----------------------------
def readfileandfolder():
    p = Path(".")
    items = list(p.rglob("*"))

    st.subheader("📁 Available Files & Folders")
    
    if items:
        for index, file in enumerate(items):
            st.write(f"{index + 1} - {file}")
    else:
        st.info("No files or folders found.")


# -----------------------------
# Create File
# -----------------------------
def create_file():
    st.subheader("📝 Create File")

    file_name = st.text_input("Enter file name")
    content = st.text_area("Enter file content")

    if st.button("Create File"):
        p = Path(file_name)

        if p.exists():
            st.error("File already exists!")
        else:
            with open(file_name, "w") as file:
                file.write(content)

            st.success("File created successfully!")


# -----------------------------
# Read File
# -----------------------------
def read_file():
    st.subheader("📖 Read File")

    file_name = st.text_input("Enter file name to read")

    if st.button("Read File"):
        p = Path(file_name)

        if p.exists():
            with open(file_name, "r") as file:
                data = file.read()

            st.text_area("File Content", data, height=200)
        else:
            st.error("File not found!")


# -----------------------------
# Update File
# -----------------------------
def update_file():
    st.subheader("✏️ Update File")

    file_name = st.text_input("Enter file name to update")

    option = st.radio(
        "Choose update option",
        ["Overwrite Content", "Append Content"]
    )

    content = st.text_area("Enter new content")

    if st.button("Update File"):
        p = Path(file_name)

        if p.exists():

            if option == "Overwrite Content":
                with open(file_name, "w") as file:
                    file.write(content)

            elif option == "Append Content":
                with open(file_name, "a") as file:
                    file.write(content)

            st.success("File updated successfully!")

        else:
            st.error("File does not exist!")


# -----------------------------
# Delete File
# -----------------------------
def delete_file():
    st.subheader("🗑️ Delete File")

    file_name = st.text_input("Enter file name to delete")

    if st.button("Delete File"):
        p = Path(file_name)

        if p.exists():
            os.remove(p)
            st.success("File deleted successfully!")
        else:
            st.error("File does not exist!")


# -----------------------------
# Rename File
# -----------------------------
def rename_file():
    st.subheader("🔄 Rename File")

    file_name = st.text_input("Enter current file name")
    new_file = st.text_input("Enter new file name")

    if st.button("Rename File"):
        p = Path(file_name)

        if p.exists():
            p.rename(new_file)
            st.success("File renamed successfully!")
        else:
            st.error("File not found!")


# -----------------------------
# Create Folder
# -----------------------------
def create_folder():
    st.subheader("📁 Create Folder")

    folder_name = st.text_input("Enter folder name")

    if st.button("Create Folder"):
        p = Path(folder_name)

        if p.exists():
            st.error("Folder already exists!")
        else:
            p.mkdir()
            st.success("Folder created successfully!")


# -----------------------------
# Delete Folder
# -----------------------------
def delete_folder():
    st.subheader("❌ Delete Folder")

    folder_name = st.text_input("Enter folder name")

    if st.button("Delete Folder"):
        p = Path(folder_name)

        if p.exists():

            try:
                p.rmdir()
                st.success("Folder deleted successfully!")

            except:
                st.error("Folder is not empty!")

        else:
            st.error("Folder does not exist!")


# -----------------------------
# Sidebar Menu
# -----------------------------
menu = st.sidebar.selectbox(
    "Choose an Option",
    [
        "Show Files & Folders",
        "Create File",
        "Read File",
        "Update File",
        "Delete File",
        "Rename File",
        "Create Folder",
        "Delete Folder"
    ]
)

# -----------------------------
# Menu Handling
# -----------------------------
if menu == "Show Files & Folders":
    readfileandfolder()

elif menu == "Create File":
    create_file()

elif menu == "Read File":
    read_file()

elif menu == "Update File":
    update_file()

elif menu == "Delete File":
    delete_file()

elif menu == "Rename File":
    rename_file()

elif menu == "Create Folder":
    create_folder()

elif menu == "Delete Folder":
    delete_folder()