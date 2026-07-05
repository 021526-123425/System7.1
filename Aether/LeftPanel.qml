Rectangle {
    id: roster
    width: parent.width * 0.22
    color: "rgba(20,10,40,0.6)"  // cosmic glass
    Column {
        Text { text: "Sigils in the Aether" }
        ListView {
            model: sigilModel
            delegate: SigilChip { sigilName: model.name }
        }
        GlyphButton { glyph: "✧"; text: "Add Sigil" }
        GlyphButton { glyph: "✧✧"; text: "Release Sigil" }
    }
}
