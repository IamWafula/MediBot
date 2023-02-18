import logo from './logo.svg';
import './App.css';
import { Div, Button, Icon } from "atomize";


function App() {
  return (
    <>
      <Button
        h="2.5rem"
        w="2.5rem"
        bg="warning700"
        hoverBg="warning600"
        rounded="circle"
        m={{ r: "1rem" }}
        shadow="2"
        hoverShadow="4"
        >
        <Icon name="Search" size="20px" color="white" />
      </Button>
    </>
  );
}


export default App;
