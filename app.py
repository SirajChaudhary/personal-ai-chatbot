import streamlit as st

from src import (
    database_agent,
    image_agent,
    document_agent,
    web_agent,
    speech_to_text,
)

# Configure Streamlit page settings
st.set_page_config(page_title="Personal AI Chatbot 🤖")

# Application header
st.markdown(
    "<h1 style='color: aliceblue;'>Personal AI Chatbot 🤖</h1>",
    unsafe_allow_html=True,
)


def main():
    # Select data source
    option = st.sidebar.selectbox(
        "Select Source",
        ("Web", "Database", "File", "Image"),
        index=None,
    )

    # Display application information
    if option is None:
        st.subheader(":blue[About]")
        st.write(
            "Personal AI Chatbot is an AI powered bot built using Generative AI technologies "
            "that helps users quickly and efficiently access information from the internet, "
            "personal databases, flat files, and images.\n\n"
            "Key features of the chatbot:\n\n"
            "- Interact with information available on the internet\n"
            "- Interact with personal databases like MySQL using plain English instead of SQL\n"
            "- Interact with personal documents such as PDF, DOCX, XLSX, and PPTX files\n"
            "- Interact with personal images such as PNG, JPG, and JPEG formats\n\n"
            "Additional capabilities:\n\n"
            "- Uses a vector store (FAISS) for faster follow-up document queries\n"
            "- Uses caching for database queries to improve performance\n"
            "- Supports uploading multiple documents/images for unified querying"
        )
        st.subheader(":blue[Developed By]")
        st.write("Siraj Chaudhary")

    # Initialize upload variables
    uploaded_files = None

    # Image uploader (supports multiple images)
    if option == "Image":
        uploaded_files = st.file_uploader(
            "Upload images",
            type=["png", "jpg", "jpeg"],
            accept_multiple_files=True,
        )

    # Document uploader
    elif option == "File":
        uploaded_files = st.file_uploader(
            "Upload documents (PDF / Word / Excel / PPT)",
            type=["pdf", "docx", "xlsx", "pptx"],
            accept_multiple_files=True,
        )

    # User query input
    query = st.sidebar.text_area("Enter your query")

    # Execute query
    if st.sidebar.button("Run⚡"):
        with st.spinner("Personal AI Chatbot is working on your query. Kindly hold ⏳"):
            # Validate source selection
            if option is None:
                st.toast("Please select a data source", icon="⚠️")
                return

            # Validate query input
            if not query.strip():
                st.toast("Please enter a query", icon="⚠️")
                return

            try:
                # Database-based query
                if option == "Database":
                    st.write(database_agent.query_sql(query))

                # Image-based query (multi-image)
                elif option == "Image":
                    if not uploaded_files:
                        st.toast("Please upload at least one image", icon="⚠️")
                        return

                    images = image_agent.upload_images(uploaded_files)
                    st.write(image_agent.query_image(query, images))

                # Document-based query
                elif option == "File":
                    if not uploaded_files:
                        st.toast("Please upload at least one document", icon="⚠️")
                        return

                    st.write(document_agent.query_documents(uploaded_files, query))

                # Web-based query
                else:
                    st.write(web_agent.web_query(query))
                    st.balloons()

                st.toast("✨ Personal AI Chatbot Response")

            except Exception as e:
                st.error(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
