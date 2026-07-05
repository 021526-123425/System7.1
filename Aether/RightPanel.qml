Rectangle {
    id: controls
    width: parent.width * 0.22
    Column {
        GlyphButton { glyph: "◯"; text: "Read Inbox" }
        GlyphButton { glyph: "≈"; text: "List Messages" }
        GlyphButton { glyph: "⟐"; text: "Purge Inbox" }
        GlyphButton { glyph: "✶"; text: "Trace Path" }

        Image { id: mindguardEye; source: "mindguard_eye.png" }
        Text { text: "Eye: " + mindguardState }
        ProgressBar { value: threatIndex / 7 }
        Text { text: "Filament: " + filamentStatus }
        Text { text: "Shadow‑Pressure: " + shadowPressure }
    }
}
