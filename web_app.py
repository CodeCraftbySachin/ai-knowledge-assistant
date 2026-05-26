import http.server
import json
from chains.chatbot_chain import get_chatbot, get_context
from memory.memory import clear_session_history

class ChatHandler(http.server.BaseHTTPRequestHandler):
    chatbot = None

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('index.html', 'rb') as f:
                self.wfile.write(f.read())
        else:
            self.send_error(404)

    def do_POST(self):
        if self.path == '/api/chat':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)

            user_input = data.get('input', '')
            role_prompt = data.get('role_prompt', 'You are a helpful AI assistant.')
            session_id = data.get('session_id', 'web_user_1')

            if ChatHandler.chatbot is None:
                try:
                    ChatHandler.chatbot = get_chatbot()
                except Exception as e:
                    self._send_json({"error": str(e)}, 500)
                    return

            try:
                response = ChatHandler.chatbot.invoke(
                    {
                        "input": user_input,
                        "role": role_prompt,
                        "context": get_context(user_input)
                    },
                    config={"configurable": {"session_id": session_id}}
                )
                self._send_json({"content": response.content})
            except Exception as e:
                self._send_json({"error": str(e)}, 500)

        elif self.path == '/api/reset':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)
            session_id = data.get('session_id', 'web_user_1')
            clear_session_history(session_id)
            self._send_json({"message": "History cleared"})

    def _send_json(self, data, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

def run(port=3000):
    server_address = ('', port)
    httpd = http.server.HTTPServer(server_address, ChatHandler)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
