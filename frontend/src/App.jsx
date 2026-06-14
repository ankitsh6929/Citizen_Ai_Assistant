import Sidebar from "./components/Sidebar";

import { useState,useEffect } from "react";
import axios from "axios";

import ChatWindow from "./components/ChatWindow";
import ChatInput from "./components/ChatInput";
import VoiceRecorder from "./components/VoiceRecorder";

function App() {
  useEffect(() => {

  createNewChat();
  loadSessions();

}, []);

  const [query, setQuery] = useState("");
  const [messages, setMessages] = useState([]);

  const [typing, setTyping] = useState(false);

  const [audioFile, setAudioFile] =
    useState(null);

  const [language] =
    useState("hi-IN");

  const [mediaRecorder, setMediaRecorder] =
    useState(null);

  const [isRecording, setIsRecording] =
    useState(false);


  const [sessionId, setSessionId] =
    useState(null);  

  
  const [sessions, setSessions] =
    useState([]);








  const createNewChat = async () => {

  try {

    const res = await axios.post(
      "http://127.0.0.1:8000/new-chat"
    );

    setSessionId(
      res.data.session_id
    );

    setMessages([]);

    await loadSessions();

    console.log(
      "New Session:",
      res.data.session_id
    );

  } catch (error) {

    console.error(error);

  }

};








  const loadSessions = async () => {

  try {

    const res = await axios.get(
      "http://127.0.0.1:8000/sessions"
    );

    console.log(
      "SESSIONS:",
      res.data.sessions
    );

    setSessions(
      res.data.sessions
    );

  } catch (error) {

    console.error(error);

  }

};

 const loadChatHistory = async (sessionId) => {

  try {

    const res = await axios.get(
      `http://127.0.0.1:8000/history/${sessionId}`
    );

    console.log(
      "History Response:",
      res.data
    );

    const loadedMessages =
      res.data.messages || [];

    console.log(
      "Loaded Messages:",
      loadedMessages
    );

    setSessionId(sessionId);

    setMessages([
      ...loadedMessages
    ]);

  } catch (error) {

    console.error(error);

  }

};







  const sendMessage = async () => {

    if (!sessionId) {

  console.error(
    "NO SESSION ID FOUND"
  );

  return;
}

    if (!query.trim()) return;

    const userMessage = {
      role: "user",
      text: query
    };

    setMessages(prev => [
      ...prev,
      userMessage
    ]);

    setTyping(true);

    try {

      console.log({
  query,
  sessionId,
  type: typeof sessionId
});

      const res = await axios.post(
        "http://127.0.0.1:8000/chat",
        {
          query,
          session_id : sessionId
        }
      );

      const botMessage = {
        role: "assistant",
        text: res.data.response
      };

      setMessages(prev => [
        ...prev,
        botMessage
      ]);

    } catch (error) {

      console.error(error);

    }

    setTyping(false);

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

      const userMessage = {
        role: "user",
        text:
          res.data.user_text ||
          "Voice Message"
      };

      const botMessage = {
        role: "assistant",
        text:
          res.data.response_text,
        audio:
          res.data.audio_file
      };

      setMessages(prev => [
        ...prev,
        userMessage,
        botMessage
      ]);

    } catch (error) {

      console.error(error);

    }

  };

  const startRecording = async () => {

    const stream =
      await navigator.mediaDevices.getUserMedia({
        audio: true
      });

    const recorder =
      new MediaRecorder(stream);

    const chunks = [];

    recorder.ondataavailable =
      (event) => {

        chunks.push(
          event.data
        );

      };

    recorder.onstop =
      async () => {

        const blob =
          new Blob(
            chunks,
            {
              type:
                "audio/wav"
            }
          );

        const file =
          new File(
            [blob],
            "recording.wav",
            {
              type:
                "audio/wav"
            }
          );

        await uploadVoice(
          file
        );

      };

    recorder.start();

    setMediaRecorder(
      recorder
    );

    setIsRecording(
      true
    );

  };

  const stopRecording = () => {

    mediaRecorder?.stop();

    setIsRecording(
      false
    );

  };

 return (

  <div
    style={{
      background: "linear-gradient(180deg,#202123,#111827)",
      color: "white",
      minHeight: "100vh",
      display: "flex"
    }}
  >

    <Sidebar
      sessions={sessions}
      createNewChat={createNewChat}
      selectSession={loadChatHistory}
    />

    <div
      style={{
        flex: 1,
        display: "flex",
        flexDirection: "column"
      }}
    >

      <ChatWindow
        messages={messages}
        typing={typing}
      />

      <div
        style={{
          position: "sticky",
          bottom: 0,
          background: "#212121",
          padding: "20px",
          display: "flex",
          alignItems: "center",
          gap: "15px",
          borderTop: "1px solid #333"
        }}
      >

        <VoiceRecorder
          isRecording={isRecording}
          startRecording={startRecording}
          stopRecording={stopRecording}
        />

        <ChatInput
          query={query}
          setQuery={setQuery}
          sendMessage={sendMessage}
        />

      </div>

    </div>

  </div>

);

}

export default App;