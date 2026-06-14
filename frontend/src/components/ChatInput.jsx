function ChatInput({
  query,
  setQuery,
  sendMessage
}) {

  return (

    <div
      style={{
        display: "flex",
        gap: "10px",
        padding: "20px",
        borderTop:
          "1px solid #333"
      }}
    >

      <input
        value={query}
        onChange={(e) =>
          setQuery(
            e.target.value
          )
        }
        onKeyDown={(e) => {

          if (
            e.key === "Enter"
          ) {

            sendMessage();

          }

        }}
        placeholder="Message Citizen AI Assistant..."
        style={{
  flex: 1,
  padding: "16px",
  fontSize: "16px",
  borderRadius: "12px",
  background: "#2d2d2d",
  color: "white",
  border: "1px solid #444"
}}
      />

      <button
        onClick={sendMessage}
      >
        ➤
      </button>

    </div>

  );

}

export default ChatInput;