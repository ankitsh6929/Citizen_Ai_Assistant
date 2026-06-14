function MessageBubble({ msg }) {

  return (

    <div
      style={{
        display: "flex",
        justifyContent:
          msg.role === "user"
            ? "flex-end"
            : "flex-start",
        marginBottom: "15px"
      }}
    >

      <div
        style={{
          background:
            msg.role === "user"
              ? "#2563eb"
              : "#343541",

          padding: "14px",
          borderRadius: "15px",
          maxWidth:  msg.role === "user" ? "60%" : "85%"
        }}
      >

        <div
          style={{
            display: "flex",
            alignItems: "flex-start",
            gap: "10px"
          }}
        >

          <div
            style={{
              fontSize: "24px"
            }}
          >
            {
              msg.role === "user"
                ? "🧑"
                : "🤖"
            }
          </div>

          <div>

            {msg.text}

            {msg.audio && (

              <div
                style={{
                  marginTop: "10px"
                }}
              >

                <audio controls>

                  <source
                    src={`http://127.0.0.1:8000/audio/${msg.audio}`}
                    type="audio/wav"
                  />

                </audio>

              </div>

            )}

          </div>

        </div>

      </div>

    </div>

  );

}

export default MessageBubble;