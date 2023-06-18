import React, { useState } from 'react';
import axios from 'axios';
import { Button, Form, Container } from 'react-bootstrap';
import styled from 'styled-components';

const Heading = styled.h1`
  text-align: center;
  margin-bottom: 2rem;
`;

const StyledButton = styled(Button)`
  background-color: #007bff;
  color: #fff;
  border-radius: 5px;
  padding: 10px 20px;
  font-size: 16px;

  &:hover {
    background-color: #0056b3;
  }
`;

const StyledForm = styled(Form)`
  padding: 2rem;
  border: 1px solid #ccc;
  border-radius: 10px;
`;

const StyledFormGroup = styled(Form.Group)`
  margin-bottom: 1.5rem;
`;

const StyledFormControl = styled(Form.Control)`
  padding: 0.75rem;
`;

const StyledLabel = styled(Form.Label)`
  margin-bottom: 0.5rem;
`;

const StyledContainer = styled(Container)`
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
`;

function App() {
  const [problemName, setProblemName] = useState('');
  const [problemLink, setProblemLink] = useState('');
  const [solution, setSolution] = useState('');

  const createPythonFile = async () => {
    const response = await axios.post('http://localhost:5000/create_file', {
      problemName,
      problemLink,
      solution,
    });
    console.log(response.data);
  };

  return (
    <StyledContainer>
      <StyledForm>
        <Heading>LeetCode Automation</Heading>
        <StyledFormGroup controlId="problemName">
          <StyledLabel>Problem Name</StyledLabel>
          <StyledFormControl
            type="text"
            placeholder="Enter the problem name"
            value={problemName}
            onChange={(e) => setProblemName(e.target.value)}
          />
        </StyledFormGroup>
        <StyledFormGroup controlId="problemLink">
          <StyledLabel>Problem Link</StyledLabel>
          <StyledFormControl
            type="text"
            placeholder="Enter the problem link"
            value={problemLink}
            onChange={(e) => setProblemLink(e.target.value)}
          />
        </StyledFormGroup>
        <StyledFormGroup controlId="solution">
          <StyledLabel>Solution</StyledLabel>
          <StyledFormControl
            as="textarea"
            rows={5}
            placeholder="Enter the solution"
            value={solution}
            onChange={(e) => setSolution(e.target.value)}
          />
        </StyledFormGroup>
        <div className="text-center">
          <StyledButton variant="primary" onClick={createPythonFile}>
            Create Python File
          </StyledButton>
        </div>
      </StyledForm>
    </StyledContainer>
  );
}

export default App;
