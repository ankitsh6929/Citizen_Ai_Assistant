import MessageBubble from "./MessageBubble";
import { useEffect, useRef } from "react";

function ChatWindow({
  messages,
  typing
}) {


  console.log(
  "RENDERING MESSAGES:",
  messages
);

  const bottomRef = useRef(null);

  useEffect(() => {

    bottomRef.current?.scrollIntoView({
      behavior: "smooth"
    });

  }, [messages, typing]);

  return (

    <div
      style={{
        flex: 1,
        overflowY: "auto",
        padding: "20px",
        maxWidth: "1000px",
        margin: "auto"
      }}
    >

      {
        messages.map(
          (msg, index) => (

            <MessageBubble
              key={index}
              msg={msg}
            />

          )
        )
      }

    {
      typing && (

  <div
    style={{
      background: "#343541",
      color: "#fff",
      padding: "15px 20px",
      borderRadius: "16px",
      width: "fit-content",
      marginTop: "10px",
      fontSize: "18px"
    }}
  >
    🤖 Assistant is typing...
  </div>

)
    }

      <div ref={bottomRef}></div>

    </div>

  );

}

export default ChatWindow;