function VoiceRecorder({
  isRecording,
  startRecording,
  stopRecording
}) {

  return (

    <button
      onClick={() => {

        if (isRecording) {

          stopRecording();

        } else {

          startRecording();

        }

      }}
      style={{
        width: "50px",
        height: "50px",
        borderRadius: "50%",
        border: "none",
        background:
          isRecording
            ? "#ef4444"
            : "#2563eb",
        color: "white",
        fontSize: "22px",
        cursor: "pointer",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        transition: "all 0.3s ease",
        boxShadow:
          "0 4px 12px rgba(0,0,0,0.4)"
      }}
      title={
        isRecording
          ? "Stop Recording"
          : "Start Recording"
      }
    >

      {
        isRecording
          ? "⏹"
          : "🎤"
      }

    </button>

  );

}

export default VoiceRecorder;