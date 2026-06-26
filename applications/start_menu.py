#!/usr/bin/env python3
"""
Start Menu (System7.1)

Simple GTK3/GTK4-based launcher that scans .desktop files in
/usr/share/applications and ~/.local/share/applications and displays
icons in a grid with a search box. Double-click or press Enter to launch.

Dependencies:
 - Python 3
 - PyGObject (python3-gi) and GTK 3 or 4

Install on Debian/Ubuntu:
  sudo apt install python3-gi gir1.2-gtk-3.0

Run:
  python3 applications/start_menu.py

Save this file as applications/start_menu.py in the repository.
"""

import os
import sys
from pathlib import Path

try:
    from gi.repository import Gtk, Gio, GdkPixbuf
except Exception as e:
    print("This script requires PyGObject and GTK. On Debian/Ubuntu: sudo apt install python3-gi gir1.2-gtk-3.0")
    raise

APP_DIRS = [
    os.path.expanduser('~/.local/share/applications'),
    '/usr/share/applications',
]

ICON_SIZE = 64


def load_apps():
    apps = []
    seen = set()
    for d in APP_DIRS:
        if not os.path.isdir(d):
            continue
        for fn in os.listdir(d):
            if not fn.endswith('.desktop'):
                continue
            path = os.path.join(d, fn)
            try:
                info = Gio.DesktopAppInfo.new_from_filename(path)
            except Exception:
                continue
            if not info or not info.get_is_hidden():
                name = info.get_name() or os.path.splitext(fn)[0]
                # avoid duplicates by desktop id/name
                key = (info.get_id() or name).lower()
                if key in seen:
                    continue
                seen.add(key)
                apps.append({'name': name, 'info': info})
    # sort by name
    apps.sort(key=lambda a: a['name'].lower())
    return apps


class AppButton(Gtk.EventBox):
    def __init__(self, appinfo):
        super().__init__()
        self.appinfo = appinfo
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        vbox.set_halign(Gtk.Align.CENTER)
        # icon
        icon = appinfo.get_icon()
        pix = None
        try:
            theme = Gtk.IconTheme.get_default()
            if icon:
                # try load by Gio.Icon
                if isinstance(icon, Gio.ThemedIcon):
                    names = icon.get_names()
                    for n in names:
                        if theme.has_icon(n):
                            pix = theme.load_icon(n, ICON_SIZE, 0)
                            break
                elif isinstance(icon, Gio.FileIcon):
                    gfile = icon.get_file()
                    path = gfile.get_path()
                    pix = GdkPixbuf.Pixbuf.new_from_file_at_scale(path, ICON_SIZE, ICON_SIZE, True)
            # fallback to stock icon
            if pix is None:
                pix = theme.load_icon('application-x-executable', ICON_SIZE, 0)
        except Exception:
            pix = None
        if pix:
            image = Gtk.Image.new_from_pixbuf(pix)
        else:
            image = Gtk.Image.new_from_icon_name('application-x-executable', Gtk.IconSize.BUTTON)
        label = Gtk.Label(label=appinfo.get_name())
        label.set_max_width_chars(12)
        label.set_line_wrap(True)
        label.set_ellipsize(3)
        vbox.pack_start(image, False, False, 0)
        vbox.pack_start(label, False, False, 0)
        self.add(vbox)
        self.show_all()

    def activate(self):
        try:
            self.appinfo.launch([], None)
        except Exception as e:
            print('Failed to launch', self.appinfo.get_name(), e)


class StartMenu(Gtk.Window):
    def __init__(self):
        super().__init__(title='System7 Start Menu')
        self.set_default_size(800, 600)
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        box.set_margin_top(8)
        box.set_margin_bottom(8)
        box.set_margin_start(8)
        box.set_margin_end(8)
        self.add(box)

        # search
        self.search = Gtk.SearchEntry()
        self.search.set_placeholder_text('Search applications...')
        self.search.connect('search-changed', self.on_search)
        box.pack_start(self.search, False, False, 0)

        # scrolled area -> FlowBox for flexible layout
        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        scrolled.set_vexpand(True)
        box.pack_start(scrolled, True, True, 0)

        self.flow = Gtk.FlowBox()
        self.flow.set_max_children_per_line(8)
        self.flow.set_selection_mode(Gtk.SelectionMode.NONE)
        self.flow.connect('child-activated', self.on_child_activated)
        scrolled.add(self.flow)

        self.apps = load_apps()
        self.widgets = []
        self.populate(self.apps)

        # key handling
        self.connect('key-press-event', self.on_key)

    def populate(self, apps):
        for child in self.flow.get_children():
            self.flow.remove(child)
        self.widgets = []
        for a in apps:
            btn = AppButton(a['info'])
            # activation
            btn.connect('button-press-event', lambda w, e, info=a['info']: self.on_click(w, e, info))
            self.flow.add(btn)
            self.widgets.append((btn, a))
        self.show_all()

    def on_click(self, widget, event, info):
        # double click or single double-button
        if event.type.value_name == '2BUTTON_PRESS' or event.type.value_name == 'DOUBLE_BUTTON_PRESS':
            try:
                info.launch([], None)
            except Exception as e:
                print('Launch error:', e)

    def on_child_activated(self, flowbox, child):
        # Fallback
        try:
            child.appinfo.launch([], None)
        except Exception:
            pass

    def on_search(self, entry):
        text = entry.get_text().lower()
        if not text:
            visible = self.apps
        else:
            visible = [a for a in self.apps if text in a['name'].lower()]
        self.populate(visible)

    def on_key(self, win, event):
        key = Gdk.keyval_name(event.keyval)
        if key == 'Escape':
            self.close()
        return False


def main():
    app = StartMenu()
    app.connect('destroy', Gtk.main_quit)
    app.show_all()
    Gtk.main()


if __name__ == '__main__':
    main()
