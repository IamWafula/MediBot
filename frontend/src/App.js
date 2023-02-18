import './App.css';
import { Div, Button, Icon, Input } from "atomize";
import { useState } from 'react';

/*
    display: flex;
    position: absolute;
    flex-direction: column;
    width: 100%;
    height: 90%;
    justify-content: flex-end;
*/

function App() {

  const [botmessages, setBotMessages] = useState(["Hi, how are you?", "How's the weather today?"]);
  const [usermessages, setUserMessages] = useState(["I'am fine, thanks!", "The weather is great!"]);

  return (
    <Div
      display="flex"
      h="100%">
        
        <Div
          bg="#000000"
          display="absolute"
          textColor="#000000"
          h="auto"
          p={{ l: "2%", b: "2%", t: "2%" }}
          >
            '\200b' 
        </Div>



        <Div
          d="flex"
          pos="absolute"
          flexDir="column"
          w="100%"
          h="90%"
          justify="flex-end"
          overflow="visible scroll"
          >

          <Div>
          
            {botmessages.map((message,i) => (
              <>
                  <Div
                    bg="#57caa26b"
                    d="flex"
                    align="left"
                    w="50%"
                    display="flex"
                    justify="flex-start"
                    m={{ t: "1rem" }}
                    h="auto"
                    p={{ l: "2%", b: "2%", t: "2%" }}
                    rounded="md"
                    key={i}
                    >
                  {message}
                  </Div>

                  <Div
                    bg="#7b45a76b"
                    d="flex"
                    align="right"
                    w="50%"
                    display="flex"
                    m={{ l: "50%", t: "1rem" }}
                    h="auto"
                    p={{ l: "2%", b: "2%", t: "2%" }}
                    rounded="md"
                    >
                    {usermessages[i] }
    
                  </Div>       
            </>
            ))}
            

                 
            
          </Div>

          <Input
            placeholder="Search"
            m={{ t: "5%" }}
            suffix={
              <Button
                pos="absolute"
                onClick={() => console.log("clicked")}
                bg="info700"
                hoverBg="info800"
                w="3rem"
                top="0"
                right="0"
                rounded={{ r: "md" }}
              >
                <Icon name="RightArrow" size="20px" />
              </Button>
              }
            />      
        </Div>
  
    </Div>
  );
}


export default App;
