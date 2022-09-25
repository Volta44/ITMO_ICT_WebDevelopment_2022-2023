import socket

lessons = [
  {'name': 'Math', 'description': 'exact science', 'marks' : [5,5,3,4,5]},
  {'name': 'IT', 'description': 'computers', 'marks' : [5,4,5,5,5,4,5]}
]

def post_split(post_msg):
  objs = post_msg.split('&')
  return [objs[0][7:], objs[1][5:], [int(i) for i in objs[2][6:].split('%2C')]]

def start_server():
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.bind(('127.0.0.1', 5500))
  server.listen(4)
  print('Server starting...')
  
  while True:
    client, addr = server.accept()

    with client:
      request = client.recv(1024).decode()
      request_method = request.split(' ')[0]
      request_msg = request.split(' ')[1][1:-1]
      header = 'HTTP/1.1 200 OK\r\nContent-Type: text.html; charset=UTF-8\r\n\r\n'
      body = '<html><head><title>Marks</title></head><body>'
      body += """
      <form method="get">
        <input type="submit" formaction="add" value="Add" />
        <input type="submit" formaction="show" value="Show" />
      </form>
      """
      if request_method == 'GET':
        if request_msg == 'show':
          body += get_mark()
        elif request_msg == 'add':
          body += add_mark()
      else:
        post_data = post_split(request.split(' ')[-1].split('\r\n\r\n')[1])
        lessons.append({'name': post_data[0], 'description': post_data[1], 'marks' : post_data[2]})
      
      body += "</body></html>"
      client.send(header.encode('utf-8') + body.encode('utf-8'))  
      
def get_mark():
  html = '<ul>'
  for lesson in lessons:
    html += f'<h1>Lesson: {lesson["name"]}</h1>'
    for mark in lesson['marks']:
      html += f'<li>Mark: {mark}</li>'
  html += '</ul>'
  return html

def add_mark():
  form = """
  <form action="/" method="post">
    <P>Lesson name: </p>
    <input type="text" name="lesson" value="IT" placeholder="IT"/>
    <P>Description: </p>
    <input type="text" name="desc" value="Cool" placeholder="Cool"/>
    <P>Marks(list grades separated by commas): </p>
    <input type="text" name="marks" value="4,5,5" placeholder="4,5,5"/>
    <br/><br/>
    <input type="submit" value="Send info"/>
  </form>"""
  return form
  
  
start_server();