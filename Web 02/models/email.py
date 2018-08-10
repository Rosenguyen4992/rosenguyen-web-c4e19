from gmail import GMail, Message

def email(email):
    gmail = GMail('Nhung nhúc <vequehomestay@gmail.com>','phong1910')

    html_content = """<p>Yêu cầu của bạn đã được xử lý, chúng tôi sẽ liên hệ với bạn trong thời gian sớm nhất. Cảm ơn bạn đã sử dụng dịch vụ của ‘Mùa Đông Không Lạnh’ </p>"""

    msg = Message('Confirmation email', to='User <email>', html=html_content, email = email)
    gmail.send(msg)
    print("Gửi thành công")

    gmail.send(msg)