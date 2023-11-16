from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def mail_sender(sender, password, receiver, subject, content):
	#Setup the MIME
	message = MIMEMultipart()
	message['From'] = sender
	message['To'] = receiver
	message['Subject'] = subject

	session = smtplib.SMTP('server136.web-hosting.com', 465) #use gmail with port
	session.starttls() #enable security
	session.login(sender, 'haemoglobin')#password)

	part2 = MIMEText(content, 'html')

	message.attach(part2)
	text = message.as_string()

	session.sendmail(sender, receiver, text)
	session.quit()
	print('Mail Sent')

confirm = '''
<html>
    <body>
        <div style="background-color: #fff6d4; width: 98%; margin: auto; border-radius: 8px;">
            <div style="background-color: #ffea99; width: 100%; margin: auto;">
                <img src="https://profixtraders.com/cdf-community.com/images/logo.png" alt="" style="width: 100%;">
            </div>
            <div style="width: 85%; margin: auto; text-align: center;">
                <h3 style="color: #feaf26; text-transform: uppercase;">RECEIPT FROM profix traders</h3>
                <p style="font-family: monospace; font-size: 1em; padding-bottom: 1em;">Your payment was successful and has been received by Profix Traders.</p>
                <h1>USD 3,607.00</h1>
                <div style="width: 70%; border-top: 2px solid #000; margin: auto;"></div>

                <h5 style="text-transform: uppercase;">payment details</h5>
                                <table style="background-color: #ffea99; width: 100%; margin: auto; border-radius: 8px; padding-left: 5%; padding-right: 5%; margin-bottom: 4em;">
                <tr>
                    <td><p style="text-align: left;">Amount paid</p></td>
                    <td><p style="text-align: right;">USD 1,578.00</p></td>
                </tr>

                <tr>
                    <td><p style="text-align: left;">Applicable fees</p></td>
                    <td><p style="text-align: right;">USD 0.00</p></td>
                </tr>

                <tr>
                    <td><p style="text-align: left;">Payment Method</p></td>
                    <td><p style="text-align: right;">BTC</p></td>
                </tr>

                <tr>
                    <td><p style="text-align: left;">Transaction Reference</p></td>
                    <td><p style="text-align: right;">PT_rg4rtryu35ng5u</p></td>
                </tr>
                </table>

                <table style="background-color: #ffea99; width: 100%; margin: auto; border-radius: 8px; padding-left: 5%; padding-right: 5%; margin-bottom: 4em;">
                <tr>
                    <td><p style="text-align: left;">Amount paid</p></td>
                    <td><p style="text-align: right;">USD 1,129.00</p></td>
                </tr>

                <tr>
                    <td><p style="text-align: left;">Applicable fees</p></td>
                    <td><p style="text-align: right;">USD 0.00</p></td>
                </tr>

                <tr>
                    <td><p style="text-align: left;">Payment Method</p></td>
                    <td><p style="text-align: right;">USDT</p></td>
                </tr>

                <tr>
                    <td><p style="text-align: left;">Transaction Reference</p></td>
                    <td><p style="text-align: right;">PT_rg4rtryu35ng5u</p></td>
                </tr>
                </table>


                                <table style="background-color: #ffea99; width: 100%; margin: auto; border-radius: 8px; padding-left: 5%; padding-right: 5%; margin-bottom: 4em;">
                <tr>
                    <td><p style="text-align: left;">Amount paid</p></td>
                    <td><p style="text-align: right;">USD 900.00</p></td>
                </tr>

                <tr>
                    <td><p style="text-align: left;">Applicable fees</p></td>
                    <td><p style="text-align: right;">USD 0.00</p></td>
                </tr>

                <tr>
                    <td><p style="text-align: left;">Payment Method</p></td>
                    <td><p style="text-align: right;">ETH</p></td>
                </tr>

                <tr>
                    <td><p style="text-align: left;">Transaction Reference</p></td>
                    <td><p style="text-align: right;">PT_rg4rtryu35ng5u</p></td>
                </tr>
                </table>

                <h5 style="text-transform: uppercase; padding-top: 1em;">Fri feb 03 2023</h5>
                <div style="width: 70%; border-top: 2px solid #000; margin: auto; padding-bottom: 4em;"></div>
            </div>
        </div>
    </body>
</html>
'''

mail_sender('admin@cryptoprofix.com', 'pwd', 'thenathancook77@gmail.com', 'Withdrawal Receipt', confirm)