import React, { useState } from "react";
import styled from "styled-components"; // Import styled-components

// Styled components
const AppHeader = styled.header`
  background-color: #282c34;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: calc(10px + 2vmin);
  color: white;
`;

const PromptTextarea = styled.textarea`
  margin-top: 20px;
  padding: 10px;
  font-size: 16px;
  border-radius: 5px;
  border: 1px solid #ccc;
`;

const GenerateButton = styled.button`
  margin-top: 10px;
  padding: 10px 20px;
  font-size: 16px;
  border-radius: 5px;
  background-color: #61dafb;
  color: white;
  border: none;
  cursor: pointer;
`;

const OutputTextDiv = styled.div`
  margin-top: 20px;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f0f0f0;
  color: black;
  min-height: 50px;
  white-space: pre-wrap;
  word-wrap: break-word;
`;

function App() {
  const [prompt, setPrompt] = useState<string>("");
  const [outputText, setOutputText] = useState<string>("");

  const handleSubmit = async () => {
    setOutputText("Generating text... (Placeholder)");
    console.log("Prompt submitted:", prompt);
  };

  return (
    <div className="App">
      <AppHeader>
        {" "}
        {/* Use the styled component */}
        <h1>Welcome to the LLM Service!</h1>
        <p>Enter your prompt below to generate text:</p>
        <PromptTextarea // Use the styled component
          id="promptInput"
          rows={5}
          cols={50}
          placeholder="Type your prompt here..."
          value={prompt}
          onChange={(e: React.ChangeEvent<HTMLTextAreaElement>) =>
            setPrompt(e.target.value)
          }
        />
        <br />
        <GenerateButton onClick={handleSubmit}>
          Generate Text
        </GenerateButton>{" "}
        {/* Use the styled component */}
        <OutputTextDiv id="outputText" className="output-text">
          {" "}
          {/* Use the styled component */}
          {outputText}
        </OutputTextDiv>
      </AppHeader>{" "}
      {/* Use the styled component */}
    </div>
  );
}

export default App;
