Rectangle {
    id: stream
    width: parent.width * 0.56
    Column {
        Text { text: "Aetherlink → " + currentSigil }
        ListView {
            model: messageModel
            delegate: MessageBubble { ... }
        }
        Row {
            TextField { id: composer }
            GlyphButton { glyph: "✦"; text: "Send"; onClicked: sendMessage() }
            GlyphButton { glyph: "…"; text: "Whisper" }
            GlyphButton { glyph: "✦✦"; text: "Decree" }
        }
    }
}
