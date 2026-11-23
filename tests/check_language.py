"""Check the installed GTK UI language across real process restarts."""

import os
from pathlib import Path
import runpy
import subprocess
import sys
import tempfile


def descendants(widget, gtk):
    yield widget
    if isinstance(widget, gtk.Container):
        for child in widget.get_children():
            yield from descendants(child, gtk)


def phase(source, expected, switch_to, screenshot=None):
    import gi
    gi.require_version("Gtk", "3.0")
    gi.require_version("Gdk", "3.0")
    gi.require_version("Vte", "2.91")
    from gi.repository import Gdk, Gio, GLib, Gtk, Vte
    assert Gtk.init_check()[0], "A graphical test display is required"
    app = runpy.run_path(str(source))
    window, controls, _ = app["make_window"](Gtk, Vte, Gio, GLib)
    assert window.get_title() == "Ajan Atölyesi / Agent Workshop", window.get_title()
    selector = next(w for w in descendants(window, Gtk)
                    if isinstance(w, Gtk.ComboBox) and w.get_name() == "aa-language")
    assert selector.get_active_id() == expected, (expected, selector.get_active_id())
    labels = {w.get_label() for w in controls}
    expected_labels = {"en": {"Verify with Claude", "Verify with Codex"},
                       "tr": {"Claude ile teyit et", "Codex ile teyit et"}}
    assert expected_labels[expected] <= labels, labels
    all_text = {w.get_text() for w in descendants(window, Gtk) if isinstance(w, Gtk.Label)}
    assert {"en": "Choose a session", "tr": "Bir oturum seç"}[expected] in all_text, all_text
    faq_label = {"en": "Frequently asked questions", "tr": "Sık sorulan sorular"}[expected]
    faq_button = next(w for w in descendants(window, Gtk)
                      if isinstance(w, Gtk.Button) and w.get_label() == faq_label)
    faq_body = []
    def read_faq():
        dialog = next(w for w in Gtk.Window.list_toplevels()
                      if isinstance(w, Gtk.Dialog) and w.get_title() == faq_label)
        view = next(w for w in descendants(dialog, Gtk) if isinstance(w, Gtk.TextView))
        buffer = view.get_buffer()
        faq_body.append(buffer.get_text(*buffer.get_bounds(), False))
        dialog.response(Gtk.ResponseType.CLOSE)
        return False
    GLib.idle_add(read_faq)
    faq_button.clicked()
    assert faq_body[0].startswith("# " + faq_label), faq_body
    if screenshot:
        window.resize(1200, 750)
        def capture():
            px = Gdk.pixbuf_get_from_window(window.get_window(), 0, 0,
                                            window.get_allocated_width(), window.get_allocated_height())
            px.savev(screenshot, "png", [], [])
            Gtk.main_quit()
            return False
        GLib.timeout_add(450, capture)
        Gtk.main()
    if switch_to:
        selector.set_active_id(switch_to)
        while Gtk.events_pending():
            Gtk.main_iteration_do(False)
    window.hide()


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--phase":
        phase(Path(sys.argv[2]), sys.argv[3], sys.argv[4], sys.argv[5] or None)
        return
    source = (Path(sys.argv[1]).resolve() if len(sys.argv) > 1
              else Path(__file__).resolve().parents[1] / "bin/ajan-pencere")
    script = Path(__file__).resolve()
    screenshot_dir = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else None
    with tempfile.TemporaryDirectory(prefix="ajan-language-") as tmp:
        folder = Path(tmp)
        project = folder / "agent-orchestration-setup"
        project.mkdir()
        env = {k: v for k, v in os.environ.items() if not k.endswith("_API_KEY")}
        env.update(HOME=tmp, XDG_CONFIG_HOME=str(folder / "config"),
                   XDG_DATA_HOME=str(folder / "data"), XDG_CACHE_HOME=str(folder / "cache"),
                   LANG="C.UTF-8", LC_ALL="C.UTF-8")
        for expected, switch_to in [("en", "tr"), ("tr", "en"), ("en", "")]:
            screenshot = (str(screenshot_dir / ("desktop-" + expected + ".png"))
                          if screenshot_dir and switch_to else "")
            subprocess.run([sys.executable, "-B", str(script), "--phase", str(source),
                            expected, switch_to, screenshot], check=True, timeout=15,
                           env=env, cwd=project)
        assert not list(folder.rglob(".env")), "Changing language must not create a key file"
    print("GTK: English default, Turkish persisted, English restored; no key file written.")


if __name__ == "__main__":
    main()
