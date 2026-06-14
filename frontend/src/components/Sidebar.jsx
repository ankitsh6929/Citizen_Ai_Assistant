import React from "react";

function Sidebar({
  sessions,
  createNewChat,
  selectSession
}) {

  return (

    <div
      style={{
        width: "260px",
        background: "#171717",
        borderRight: "1px solid #333",
        height: "100vh",
        padding: "10px",
        overflowY: "auto"
      }}
    >

      <button
        onClick={createNewChat}
        style={{
          width: "100%",
          padding: "12px",
          marginBottom: "15px",
          cursor: "pointer"
        }}
      >
        + New Chat
      </button>

      {sessions.map(session => (

        <div
          key={session.session_id}
          onClick={() =>
            selectSession(
              session.session_id
            )
          }
          style={{
            padding: "12px",
            marginBottom: "10px",
            background: "#202123",
            borderRadius: "8px",
            cursor: "pointer",
            color: "white"
          }}
        >
          <>
  {session.title}
  
</>
        </div>

      ))}

    </div>

  );

}

export default Sidebar;