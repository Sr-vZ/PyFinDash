from textual.app import App, ComposeResult
from textual.widgets import Static, Welcome, Header, Footer, Checkbox, Label
from textual.binding import Binding
from textual.reactive import reactive, watch
from textual.containers import Container, Horizontal


class Title(Static):
    pass


class DarkSwitch(Horizontal):
    def compose(self) -> ComposeResult:
        yield Checkbox(value=self.app.dark)
        yield Static("Dark mode toggle", classes="label")

    def on_mount(self) -> None:
        watch(self.app, "dark", self.on_dark_change, init=False)

    def on_dark_change(self, dark: bool) -> None:
        self.query_one(Checkbox).value = self.app.dark

    def on_checkbox_changed(self, event: Checkbox.Changed) -> None:
        self.app.dark = event.value


class Sidebar(Container):
    def compose(self) -> ComposeResult:
        yield Container(Label("Menu", id="menu"))
        # yield OptionGroup(Message("test"), Version())
        # yield DarkSwitch()


class Dashboard(App):
    CSS_PATH = "style.css"
    # BINDINGS = [
    #     Binding(key="q", action="quit", description="Quit the app"),
    #     Binding(
    #         key="question_mark",
    #         action="help",
    #         description="Show help screen",
    #         key_display="?",
    #     ),
    #     # Binding(
    #     #     key="tab",
    #     #     action="toggle_sidebar",
    #     #     description="Delete the thing",
    #     # ),
    #     ("ctrl+b", "toggle_sidebar", "Sidebar"),
    #     Binding(key="delete", action="delete", description="Delete the thing"),
    #     Binding(key="j", action="down", description="Scroll down", show=False),
    # ]
    BINDINGS = [
        # ("ctrl+b", "toggle_sidebar", "Sidebar"),
        ("ctrl+b", "app.toggle_class('Sidebar', '-active')", "Sidebar"),
        ("ctrl+t", "app.toggle_dark", "Toggle Dark mode"),
        ("ctrl+s", "app.screenshot()", "Screenshot"),
        ("f1", "app.toggle_class('TextLog', '-hidden')", "Notes"),
        Binding("ctrl+c,ctrl+q", "app.quit", "Quit", show=True),
    ]
    show_sidebar = reactive(False)

    def compose(self) -> ComposeResult:
        yield Container(
            # Sidebar(classes="-hidden"),
            Sidebar(),
            Header(),
            Welcome(),
        )
        # yield Static("Sidebar", id="sidebar")

        yield Footer()
        # yield Static("Sidebar", id="sidebar")

    def action_toggle_sidebar(self) -> None:
        sidebar = self.query_one(Sidebar)
        self.set_focus(None)
        if sidebar.has_class("-hidden"):
            sidebar.remove_class("-hidden")
        else:
            if sidebar.query("*:focus"):
                self.screen.set_focus(None)
            sidebar.add_class("-hidden")
        # app.toggle_class("#sidebar", "-active")

    def on_button_pressed(self) -> None:
        # self.bind("tab", "toggle_class('#sidebar', '-active')")
        self.exit()


if __name__ == "__main__":
    app = Dashboard()
    app.run()
