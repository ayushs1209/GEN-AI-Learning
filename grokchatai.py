import os
from google import genai
from typing import Optional, Dict, Any, List
from dotenv import load_dotenv

load_dotenv()

class GeminiSDK:
    """A Python SDK for interacting with Google's Gemini API."""
    
    def __init__(self, api_key: str, model: str = "gemini-2.5-flash-preview-04-17"):
        """
        Initialize the Gemini SDK with an API key and model selection.
        
        Args:
            api_key (str): The Gemini API key from Google AI Studio.
            model (str): The Gemini model to use (default: gemini-2.5-flash).
        """
        self.api_key = api_key
        self.model = model
        self.client = genai.GenerativeModel(model_name=self.model)
    
    def generate_text(self, 
                     prompt: str, 
                     config: Optional[Dict[str, Any]] = None) -> str:
        """
        Generate text from a text prompt.
        
        Args:
            prompt (str): The input prompt for text generation.
            config (Optional[Dict[str, Any]]): Configuration options like temperature, max_tokens.
        
        Returns:
            str: The generated text response.
        """
        default_config = {
            "temperature": 1.0,
            "max_output_tokens": 2048,
            "top_p": 0.95,
            "top_k": 40
        }
        
        if config:
            default_config.update(config)
        
        try:
            response = self.client.generate_content(
                contents=prompt,
                generation_config=default_config
            )
            return response.text
        except Exception as e:
            raise Exception(f"Error generating text: {str(e)}")
    
    def generate_multimodal(self, 
                           contents: List[Any], 
                           config: Optional[Dict[str, Any]] = None) -> str:
        """
        Generate content from multimodal inputs (text, images, etc.).
        
        Args:
            contents (List[Any]): List of content parts (text, images, etc.).
            config (Optional[Dict[str, Any]]): Configuration options.
        
        Returns:
            str: The generated text response.
        """
        default_config = {
            "temperature": 1.0,
            "max_output_tokens": 2048,
            "top_p": 0.95,
            "top_k": 40
        }
        
        if config:
            default_config.update(config)
        
        try:
            response = self.client.generate_content(
                contents=contents,
                generation_config=default_config
            )
            return response.text
        except Exception as e:
            raise Exception(f"Error generating multimodal content: {str(e)}")
    
    def start_chat(self, history: List[Dict[str, str]] = None):
        """
        Start a chat session for multi-turn conversations.
        
        Args:
            history (List[Dict[str, str]]): Optional chat history.
        
        Returns:
            ChatSession: A chat session object for ongoing conversation.
        """
        try:
            chat = self.client.start_chat(history=history or [])
            return ChatSession(chat)
        except Exception as e:
            raise Exception(f"Error starting chat: {str(e)}")

class ChatSession:
    """Handles multi-turn conversations with the Gemini model."""
    
    def __init__(self, chat):
        self.chat = chat
    
    def send_message(self, message: str, stream: bool = False) -> str:
        """
        Send a message in the chat session.
        
        Args:
            message (str): The message to send.
            stream (bool): Whether to stream the response.
        
        Returns:
            str: The response text.
        """
        try:
            response = self.chat.send_message(message, stream=stream)
            return response.text
        except Exception as e:
            raise Exception(f"Error sending message: {str(e)}")
    
    def get_history(self) -> List[Dict[str, str]]:
        """
        Get the chat history.
        
        Returns:
            List[Dict[str, str]]: The conversation history.
        """
        return [{"role": msg.role, "content": msg.parts[0].text} 
                for msg in self.chat.history]

# Example usage
if __name__ == "__main__":
    # Set your API key (replace with your actual key)
    API_KEY = os.getenv("GOOGLE_API_KEY")
    
    # Initialize the SDK


    gemini = GeminiSDK(api_key=API_KEY)
    
    # Generate text from a prompt
    prompt = "Explain the significance of the Python programming language."
    response = gemini.generate_text(prompt, config={"temperature": 0.7})
    print("Text Response:", response)
    
    # Start a chat session
    chat_session = gemini.start_chat()
    response = chat_session.send_message("Hello, tell me about AI.")
    print("Chat Response:", response)
    
    # Continue the conversation
    response = chat_session.send_message("What are its applications?")
    print("Follow-up Response:", response)