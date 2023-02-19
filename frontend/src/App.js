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

  const [botmessages, setBotMessages] = useState([]);
  const [usermessages, setUserMessages] = useState([]);

  const [currentMessage, setCurrentMessage] = useState("");

  

  async function getResponse () {
    let value = await fetch('http://127.0.0.1:5000/response').then(response => response.json());
    //.then(data => this.setState({ totalReactPackages: data.total }));


    setBotMessages([...botmessages, value['response']])
    setUserMessages([...usermessages, currentMessage])
    
  }

  const handleChange = (e) => {
    setCurrentMessage(e.target.value)
  }


  return (
    <Div
      display="flex"
      h="100%"
      >
        
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
          overflow = "scroll"
          w="100%"
          h="90%"          
          //justify="flex-end"          
          overflowY="scroll"
          >

          <Div>

              <Div
                bg="#57caa26b"
                d="flex"
                align="left"
                w="50%"
                display="flex"                
                m={{ t: "1rem" }}
                h="auto"
                p={{ l: "2%", b: "2%", t: "2%" }}
                rounded="md"
                >
              "Hi, how are you?"
              </Div>
                  
            {botmessages.map((message,i) => (
              < >

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
                    key={i}
                    >
                    {usermessages[i] }

                  </Div>   
                  <Div
                    bg="#57caa26b"
                    d="flex"
                    align="left"
                    w="50%"
                    display="flex"                    
                    m={{ t: "1rem" }}
                    h="auto"
                    p={{ l: "2%", b: "2%", t: "2%" }}
                    rounded="md"                  
                    >
                  {message}
                  </Div>

                                
            </>
            ))}
                   
            
          </Div>          

          <Input
            placeholder="Search"
            m={{ t: "5%" }}
            onChange={handleChange}
            suffix={
              <Button
                pos="absolute"
                onClick={getResponse}
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
