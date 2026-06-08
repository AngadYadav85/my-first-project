import streamlit as st
import json
from pathlib import Path

DATABASE = "movies.json"

# Load Data
if Path(DATABASE).exists():
    with open(DATABASE, "r") as file:
        movies = json.load(file)
else:
    movies = []

# Save Data
def save_data():
    with open(DATABASE, "w") as file:
        json.dump(movies, file, indent=4)

st.set_page_config(page_title="Movie Booking System", page_icon="🎬")

st.title("🎬 Movie Booking System")

menu = st.sidebar.selectbox(
    "Choose an Option",
    ["Add Movie", "Book Ticket", "Cancel Ticket", "Show Movies"]
)

# Add Movie
if menu == "Add Movie":
    st.header("➕ Add Movie")

    movie_name = st.text_input("Movie Name")
    seats = st.number_input(
        "Total Seats",
        min_value=1,
        step=1
    )

    if st.button("Add Movie"):
        movies.append({
            "movie_name": movie_name,
            "available_seats": seats
        })
        save_data()
        st.success("Movie added successfully!")

# Book Ticket
elif menu == "Book Ticket":
    st.header("🎟️ Book Ticket")

    if movies:
        movie_list = [m["movie_name"] for m in movies]

        selected_movie = st.selectbox(
            "Select Movie",
            movie_list
        )

        seats = st.number_input(
            "Number of Tickets",
            min_value=1,
            step=1
        )

        if st.button("Book"):
            for movie in movies:
                if movie["movie_name"] == selected_movie:
                    if seats > movie["available_seats"]:
                        st.error("Seats not available!")
                    else:
                        movie["available_seats"] -= seats
                        save_data()
                        st.success(
                            f"{seats} ticket(s) booked successfully!"
                        )

    else:
        st.warning("No movies available.")

# Cancel Ticket
elif menu == "Cancel Ticket":
    st.header("❌ Cancel Ticket")

    if movies:
        movie_list = [m["movie_name"] for m in movies]

        selected_movie = st.selectbox(
            "Select Movie",
            movie_list
        )

        seats = st.number_input(
            "Tickets to Cancel",
            min_value=1,
            step=1
        )

        if st.button("Cancel"):
            for movie in movies:
                if movie["movie_name"] == selected_movie:
                    movie["available_seats"] += seats
                    save_data()
                    st.success("Ticket cancelled successfully!")

    else:
        st.warning("No movies available.")

# Show Movies
elif menu == "Show Movies":
    st.header("🎥 Available Movies")

    if movies:
        for movie in movies:
            st.info(
                f"*{movie['movie_name']}*\n\n"
                f"Available Seats: {movie['available_seats']}"
            )
    else:
        st.warning("No movies added yet.")