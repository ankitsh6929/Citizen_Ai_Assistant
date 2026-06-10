import { useState } from "react";
import axios from "axios";

function App() {

  const [loading, setLoading] = useState(false);
  const [typing, setTyping] = useState(false);

  const [query, setQuery] = useState("");
  const [messages, setMessages] = useState([]);

  const [audioFile, setAudioFile] = useState(null);
  const [audioResponse, setAudioResponse] = useState("");
  const [voiceText, setVoiceText] = useState("");

  const [language, setLanguage] =
    useState("hi-IN");

  const [mediaRecorder, setMediaRecorder] =
    useState(null);

  const [isRecording, setIsRecording] =
    useState(false);

  const sendMessage = async () => {

  if (!query.trim()) return;

  const userMessage = {
    role: "user",
    text: query
  };

  setMessages(prev => [
    ...prev,
    userMessage
  ]);

  setLoading(true);
  setTyping(true);

  try {

    const res = await axios.post(
      "http://127.0.0.1:8000/chat",
      {
        query: query
      }
    );

    setTimeout(() => {

      const botMessage = {
        role: "assistant",
        text: res.data.response
      };

      setMessages(prev => [
        ...prev,
        botMessage
      ]);

      setTyping(false);

    }, 1200);

  } catch (error) {

    console.error(error);

    setTyping(false);

  }

  setLoading(false);

  setQuery("");
};

  const uploadVoice = async (
    selectedFile = audioFile
  ) => {

    if (!selectedFile) return;

    const formData = new FormData();

    formData.append(
      "audio",
      selectedFile
    );

    formData.append(
      "language",
      language
    );

    try {

      const res = await axios.post(
        "http://127.0.0.1:8000/voice",
        formData,
        {
          headers: {
            "Content-Type":
              "multipart/form-data"
          }
        }
      );

      setAudioResponse(
        res.data.audio_file
      );

      setVoiceText(
        res.data.response_text
      );

    } catch (error) {

      console.error(error);

      alert(
        "Voice upload failed"
      );
    }
  };

  const startRecording = async () => {

    try {

      const stream =
        await navigator.mediaDevices.getUserMedia({
          audio: true
        });

      const recorder =
        new MediaRecorder(stream);

      const chunks = [];

      recorder.ondataavailable = (
        event
      ) => {
        chunks.push(event.data);
      };

      recorder.onstop = async () => {

        const blob = new Blob(
          chunks,
          {
            type: "audio/wav"
          }
        );

        const file = new File(
          [blob],
          "recording.wav",
          {
            type: "audio/wav"
          }
        );

        setAudioFile(file);

        await uploadVoice(file);
      };

      recorder.start();

      setMediaRecorder(recorder);

      setIsRecording(true);

    } catch (error) {

      console.error(error);

      alert(
        "Microphone permission denied"
      );
    }
  };

  const stopRecording = () => {

    if (mediaRecorder) {

      mediaRecorder.stop();

      setIsRecording(false);

    }
  };

  return (

    <div
    
      style={{
        background: "#0f172a",
        minHeight: "100vh",
        color: "white",
        padding: "20px"
      }}
    >
    <style>
{`
@keyframes pulse {

  0% {
    opacity: 0.3;
  }

  50% {
    opacity: 1;
  }

  100% {
    opacity: 0.3;
  }

}
`}
</style>
      <h1
        style={{
          textAlign: "center"
        }}
      >
        Citizen AI Assistant
      </h1>

      <div
        style={{
          display: "flex",
          justifyContent: "center",
          marginBottom: "20px"
        }}
      >

        <input
          type="text"
          value={query}
          onChange={(e) =>
            setQuery(e.target.value)
          }
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              sendMessage();
            }
          }}
          placeholder="Ask a question..."
          style={{
            width: "60%",
            padding: "12px"
          }}
        />


        {
  loading && (

    <p
      style={{
        textAlign: "center",
        color: "#38bdf8"
      }}
    >
      Processing...
    </p>

  )
}

        <button
          onClick={sendMessage}
          style={{
            marginLeft: "10px",
            padding: "12px"
          }}
        >
          Send
        </button>

        <button
  onClick={() => {
    setMessages([]);
    setVoiceText("");
    setAudioResponse("");
  }}
  style={{
    marginLeft: "10px",
    padding: "12px",
    background: "#dc2626",
    color: "white"
  }}
>
  Clear Chat
</button>

      </div>









      <div
  style={{
    maxWidth: "900px",
    margin: "auto"
  }}
>

  {messages.map((msg, index) => (

    <div
      key={index}
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
              : "#1e293b",
          padding: "14px",
          borderRadius: "15px",
          maxWidth: "70%",
          boxShadow:
            "0px 0px 10px rgba(0,0,0,0.3)"
        }}
      >

        <strong>
          {msg.role === "user"
            ? "You"
            : "Assistant"}
        </strong>

        <br />
        <br />

        {msg.text}

      </div>

    </div>

  ))}

  {typing && (

    <div
      style={{
        textAlign: "left",
        marginTop: "10px"
      }}
    >

      <div
        style={{
          display: "inline-block",
          background: "#1e293b",
          padding: "12px",
          borderRadius: "15px"
        }}
      >
        Assistant is typing...
      </div>

    </div>

  )}

</div>







      <hr
        style={{
          margin: "30px 0"
        }}
      />

      <h2
        style={{
          textAlign: "center"
        }}
      >
        Voice Assistant
      </h2>

      <div
        style={{
          textAlign: "center"
        }}
      >

        <select
          value={language}
          onChange={(e) =>
            setLanguage(e.target.value)
          }
          style={{
            padding: "10px",
            marginBottom: "15px"
          }}
        >

          <option value="hi-IN">Hindi</option>
          <option value="en-IN">English</option>
          <option value="bn-IN">Bengali</option>
          <option value="ta-IN">Tamil</option>
          <option value="te-IN">Telugu</option>

        </select>

        <br />

        <input
          type="file"
          accept=".wav"
          onChange={(e) =>
            setAudioFile(
              e.target.files[0]
            )
          }
        />

        <button
          onClick={() =>
            uploadVoice()
          }
          style={{
            marginLeft: "10px"
          }}
        >
          Upload Voice
        </button>

        <br />
        <br />

        <button
          onClick={startRecording}
          disabled={isRecording}
        >
          🎤 Start Recording
        </button>

        <button
          onClick={stopRecording}
          disabled={!isRecording}
          style={{
            marginLeft: "10px"
          }}
        >
          ⏹ Stop Recording
        </button>

        {
  isRecording ? (

    <div
      style={{
        marginTop: "20px"
      }}
    >

      <h3>
        🎤 Recording...
      </h3>

      <div
        style={{
          fontSize: "30px",
          animation:
            "pulse 1s infinite"
        }}
      >
        🎙️🎙️🎙️
      </div>

    </div>

  ) : (

    <p>
      ⚪ Idle
    </p>

  )
}

      </div>

      {voiceText && (

        <div
          style={{
            maxWidth: "900px",
            margin: "30px auto",
            background: "#1e293b",
            padding: "20px",
            borderRadius: "10px"
          }}
        >

          <h3>
            AI Response
          </h3>

          <p>
            {voiceText}
          </p>

        </div>

      )}

      {audioResponse && (

        <div
          style={{
            textAlign: "center"
          }}
        >

          <h3>
            Audio Response
          </h3>

          <audio
            controls
            autoPlay
          >
            <source
              src={`http://127.0.0.1:8000/audio/${audioResponse}`}
              type="audio/wav"
            />
          </audio>

        </div>

      )}

    </div>
  );
}

export default App;