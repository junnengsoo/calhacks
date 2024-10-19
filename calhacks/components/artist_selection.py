import reflex as rx

class ArtistSelectionState(rx.State):
    artists: list[dict] = [
        {"name": "Taylor Swift", "icon": "music"},
        {"name": "Ed Sheeran", "icon": "guitar"},
        {"name": "Beyoncé", "icon": "mic"},
        {"name": "Drake", "icon": "headphones"},
        {"name": "Adele", "icon": "radio"},
        {"name": "Bruno Mars", "icon": "music"},
        {"name": "Ariana Grande", "icon": "mic"},
        {"name": "The Weeknd", "icon": "headphones"},
        {"name": "Lady Gaga", "icon": "music"},
        {"name": "Justin Bieber", "icon": "mic"}
    ]
    selected_artists: list[str] = []

    def toggle_artist(self, artist: str):
        if artist in self.selected_artists:
            self.selected_artists.remove(artist)
        else:
            self.selected_artists.append(artist)

    def log_selected_artists(self):
        print("Selected Artists:", self.selected_artists)
        return rx.window_alert(f"Selected Artists: {', '.join(self.selected_artists)}")

def artist_icon_checkbox(artist: dict) -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.icon(
                tag="alarm_clock",
                size=32,
                color=rx.cond(
                    ArtistSelectionState.selected_artists.contains(artist["name"]),
                    rx.color("accent", 9),
                    rx.color("accent", 3)
                )
            ),
            width="60px",
            height="60px",
            border_radius="50%",
            bg=rx.cond(
                ArtistSelectionState.selected_artists.contains(artist["name"]),
                rx.color("accent", 2),
                rx.color("accent", 1)
            ),
            display="flex",
            justify_content="center",
            align_items="center",
            cursor="pointer",
            on_click=lambda: ArtistSelectionState.toggle_artist(artist["name"])
        ),
        rx.text(artist["name"], font_size="sm"),
        align_items="center",
        spacing="2",
    )

def artist_selection() -> rx.Component:
    return rx.vstack(
        rx.heading("Select Music Artists", size="lg"),
        rx.flex(
            rx.foreach(
                ArtistSelectionState.artists,
                artist_icon_checkbox
            ),
            wrap="wrap",
            spacing="4",
            justify="center",
            align_items="center",
            width="100%",
        ),
        rx.divider(),
        rx.text("Selected Artists:"),
        rx.ordered_list(
            rx.foreach(
                ArtistSelectionState.selected_artists,
                lambda artist: rx.list_item(artist)
            )
        ),
        rx.button(
            "Log Selected Artists",
            on_click=ArtistSelectionState.log_selected_artists,
            color_scheme="blue",
            margin_top="1em",
        ),
        width="100%",
        max_width="800px",
        spacing="4",
        align_items="center",
    )
